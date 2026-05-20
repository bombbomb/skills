#!/usr/bin/env python3
"""
BombBomb AI Learning Plan — Markdown → PDF converter.
Usage: python3 make_pdf_fixed.py <input.md> <output.pdf>
"""
import sys, re, textwrap
from reportlab.lib.pagesizes import letter
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import inch
from reportlab.lib import colors
from reportlab.platypus import (SimpleDocTemplate, Paragraph, Spacer,
                                 HRFlowable, Table, TableStyle, Preformatted)

BB_BLUE   = colors.HexColor("#1B4F8C")
BB_ORANGE = colors.HexColor("#E8622A")
LIGHT_BG  = colors.HexColor("#F4F7FB")
CODE_BG   = colors.HexColor("#1E1E2E")
CODE_FG   = colors.HexColor("#CDD6F4")
RULE_CLR  = colors.HexColor("#D0D9E8")
MID_GREY  = colors.HexColor("#6B7A99")

base = getSampleStyleSheet()

def S(name, parent="Normal", **kw):
    return ParagraphStyle(name, parent=base[parent], **kw)

STYLES = {
    "h1":        S("h1","Title", fontSize=26, textColor=BB_BLUE,
                    spaceAfter=6, spaceBefore=0, fontName="Helvetica-Bold"),
    "meta":      S("meta", fontSize=10, textColor=MID_GREY,
                    spaceAfter=18, fontName="Helvetica"),
    "h2":        S("h2", fontSize=16, textColor=BB_BLUE,
                    spaceBefore=22, spaceAfter=4, fontName="Helvetica-Bold"),
    "h3":        S("h3", fontSize=12, textColor=BB_ORANGE,
                    spaceBefore=12, spaceAfter=3, fontName="Helvetica-Bold"),
    "body":      S("body", fontSize=10, leading=15, spaceAfter=6,
                    fontName="Helvetica"),
    "bullet":    S("bullet", fontSize=10, leading=14, spaceAfter=3,
                    leftIndent=18, fontName="Helvetica"),
    "code_line": S("code_line", fontSize=8.5, leading=12, fontName="Courier",
                    textColor=CODE_FG, backColor=CODE_BG,
                    leftIndent=8, rightIndent=8),
    "table_hdr": S("table_hdr", fontSize=9, fontName="Helvetica-Bold",
                    textColor=colors.white),
    "table_cell":S("table_cell", fontSize=9, fontName="Helvetica", leading=13),
    "italic":    S("italic", fontSize=10, fontName="Helvetica-Oblique",
                    textColor=MID_GREY, spaceAfter=8),
}

# ---------------------------------------------------------------------------
# Code-block line wrapping
#
# Courier 8.5pt: each char is 8.5 * 0.6 = 5.1pt wide.
# Box inner width: 5.8in - (10+10)pt padding = 5.8*72 - 20 = 397.6pt
# Max chars: 397.6 / 5.1 ≈ 77  →  use 75 to be safe.
# ---------------------------------------------------------------------------
CODE_WRAP_WIDTH = 75

def _wrap_code_line(line):
    """
    Hard-wrap a single code line at CODE_WRAP_WIDTH characters.
    Continuation lines get a 4-space indent (or match the original indent
    if that's deeper) so the visual structure is preserved.
    """
    if len(line) <= CODE_WRAP_WIDTH:
        return [line]

    leading_spaces = len(line) - len(line.lstrip(' '))
    # continuation indent = original indent + 4 spaces, but never wider than
    # half the wrap width so we always make forward progress
    cont = ' ' * min(leading_spaces + 4, CODE_WRAP_WIDTH // 2)

    chunks = []
    remaining = line
    first = True
    while len(remaining) > CODE_WRAP_WIDTH:
        split_at = CODE_WRAP_WIDTH
        # Prefer to break at a space so we don't cut mid-token when possible
        space_pos = remaining.rfind(' ', 0, CODE_WRAP_WIDTH)
        if space_pos > (CODE_WRAP_WIDTH // 2):
            split_at = space_pos
        chunks.append(remaining[:split_at])
        tail = remaining[split_at:].lstrip(' ') if space_pos > CODE_WRAP_WIDTH // 2 else remaining[split_at:]
        remaining = cont + tail
        first = False
    chunks.append(remaining)
    return chunks

def wrap_code_buf(lines):
    """Apply _wrap_code_line to every line in the code buffer."""
    result = []
    for line in lines:
        result.extend(_wrap_code_line(line))
    return result

# ---------------------------------------------------------------------------

def esc(t):
    return t.replace("&","&amp;").replace("<","&lt;").replace(">","&gt;")

def inline(t):
    t = esc(t)
    t = re.sub(r'\*\*(.+?)\*\*', r'<b>\1</b>', t)
    t = re.sub(r'`([^`]+)`',
               r'<font name="Courier" color="#E8622A">\1</font>', t)
    t = re.sub(r'\[([^\]]+)\]\(([^)]+)\)', r'<u>\1</u>', t)
    return t

def parse_table(lines):
    rows = []
    for ln in lines:
        ln = ln.strip()
        if not ln or re.match(r'^\|[-| ]+\|$', ln):
            continue
        cells = [c.strip() for c in ln.strip("|").split("|")]
        rows.append(cells)
    if not rows:
        return None
    col_n = max(len(r) for r in rows)
    rows = [r + [""] * (col_n - len(r)) for r in rows]
    tbl_data = []
    for i, row in enumerate(rows):
        st = STYLES["table_hdr"] if i == 0 else STYLES["table_cell"]
        tbl_data.append([Paragraph(inline(c), st) for c in row])
    col_w = [5.8 * inch / col_n] * col_n
    if col_n == 4:
        col_w = [1.1*inch, 1.4*inch, 1.0*inch, 2.0*inch]
    t = Table(tbl_data, colWidths=col_w, repeatRows=1)
    t.setStyle(TableStyle([
        ("BACKGROUND", (0,0),(-1,0), BB_BLUE),
        ("TEXTCOLOR",  (0,0),(-1,0), colors.white),
        ("ROWBACKGROUNDS",(0,1),(-1,-1),[colors.white, LIGHT_BG]),
        ("GRID",(0,0),(-1,-1), 0.4, RULE_CLR),
        ("TOPPADDING",(0,0),(-1,-1),5),
        ("BOTTOMPADDING",(0,0),(-1,-1),5),
        ("LEFTPADDING",(0,0),(-1,-1),6),
        ("RIGHTPADDING",(0,0),(-1,-1),6),
        ("VALIGN",(0,0),(-1,-1),"TOP"),
    ]))
    return t

def convert(md_path, pdf_path):
    doc = SimpleDocTemplate(pdf_path, pagesize=letter,
                             leftMargin=0.85*inch, rightMargin=0.85*inch,
                             topMargin=0.9*inch,  bottomMargin=0.9*inch)
    with open(md_path, encoding="utf-8") as f:
        lines = f.readlines()

    story = []
    in_code, code_buf, table_buf, in_table = False, [], [], False

    def flush_code():
        if not code_buf:
            return
        # Wrap long lines before rendering so nothing overflows the box
        wrapped = wrap_code_buf(code_buf)
        pre = Preformatted("\n".join(wrapped), STYLES["code_line"])
        t = Table([[pre]], colWidths=[5.8*inch])
        t.setStyle(TableStyle([
            ("BACKGROUND",(0,0),(-1,-1), CODE_BG),
            ("TOPPADDING",(0,0),(-1,-1),8),
            ("BOTTOMPADDING",(0,0),(-1,-1),8),
            ("LEFTPADDING",(0,0),(-1,-1),10),
            ("RIGHTPADDING",(0,0),(-1,-1),10),
        ]))
        story.append(Spacer(1,4))
        story.append(t)
        story.append(Spacer(1,6))
        code_buf.clear()

    def flush_table():
        if not table_buf:
            return
        t = parse_table(table_buf)
        if t:
            story.append(Spacer(1,6))
            story.append(t)
            story.append(Spacer(1,10))
        table_buf.clear()

    i = 0
    while i < len(lines):
        raw = lines[i].rstrip("\n")
        s   = raw.strip()

        if s.startswith("```"):
            if in_code:
                in_code = False; flush_code()
            else:
                in_code = True
            i += 1; continue
        if in_code:
            code_buf.append(raw); i += 1; continue

        if s.startswith("|"):
            in_table = True; table_buf.append(s); i += 1; continue
        elif in_table:
            in_table = False; flush_table()

        if re.match(r'^-{3,}$', s):
            story.append(Spacer(1,4))
            story.append(HRFlowable(width="100%", thickness=1,
                                     color=RULE_CLR, spaceAfter=4))
            i += 1; continue

        if s.startswith("# ") and not s.startswith("## "):
            story.append(Paragraph(esc(s[2:]), STYLES["h1"]))
            i += 1
            if i < len(lines) and lines[i].strip().startswith("**"):
                story.append(Paragraph(inline(lines[i].strip()), STYLES["meta"]))
                story.append(HRFlowable(width="100%", thickness=2,
                                         color=BB_ORANGE, spaceAfter=12))
                i += 1
            continue

        if s.startswith("### "):
            story.append(Paragraph(inline(s[4:]), STYLES["h3"])); i += 1; continue
        if s.startswith("## "):
            story.append(Spacer(1,6))
            story.append(HRFlowable(width="100%", thickness=1.5,
                                     color=BB_BLUE, spaceAfter=3))
            story.append(Paragraph(esc(s[3:]), STYLES["h2"])); i += 1; continue

        m = re.match(r'^\s*[-*]\s+(.*)', s)
        if m:
            story.append(Paragraph("• " + inline(m.group(1)), STYLES["bullet"]))
            i += 1; continue

        m = re.match(r'^\d+\.\s+(.*)', s)
        if m:
            story.append(Paragraph("• " + inline(m.group(1)), STYLES["bullet"]))
            i += 1; continue

        if s.startswith("*") and s.endswith("*") and not s.startswith("**"):
            story.append(Paragraph(esc(s.strip("*")), STYLES["italic"]))
            i += 1; continue

        if not s:
            story.append(Spacer(1,5)); i += 1; continue

        story.append(Paragraph(inline(s), STYLES["body"]))
        i += 1

    flush_code(); flush_table()
    doc.build(story)
    print(f"PDF written → {pdf_path}")

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python3 make_pdf_fixed.py <input.md> <output.pdf>")
        sys.exit(1)
    convert(sys.argv[1], sys.argv[2])
