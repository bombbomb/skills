---
name: bb-onboarding
description: Creates a personalized AI learning plan for BombBomb employees. Use this skill whenever someone mentions "bb-onboarding", "AI onboarding", "AI learning plan", "get started with AI", "AI training plan", or asks how to learn AI for their role at BombBomb. Also trigger when a new team member or existing employee wants to understand how to use AI in their day-to-day work. This skill gathers the person's role and experience level, then spins up parallel research agents to produce a comprehensive, role-tailored AI learning roadmap. Use proactively any time someone seems to want structured AI guidance at BombBomb.
---

# BombBomb AI Onboarding Skill

This skill builds a personalized AI learning plan for a BombBomb employee. It tailors depth, focus areas, and practical recommendations to their specific role and current AI knowledge level.

## Step 1: Gather Information

Use `AskUserQuestion` with **two questions in a single call**:

**Question 1** — "What is your role at BombBomb?"
Options: Sales, Marketing, Customer Success, Engineering / Product, Leadership / Executive, HR / People Operations, Support / Operations, Other

**Question 2** — "What's your current AI knowledge level?"
Options:
- Beginner — Just getting started; mostly curious
- Intermediate — Use AI tools regularly but want to go deeper
- Advanced — Building workflows and want cutting-edge techniques

## Step 2: Load Supporting References

Before proceeding, read these two files (they are short — read both):
- `references/areas.md` — Full descriptions of the 10 learning areas
- `references/roles.md` — Role-to-area priority mapping and level guidance

## Step 3: Select Priority Areas

Using the role-to-priority mapping from `references/roles.md`, identify the **top 6 areas** for this person's role. The remaining 4 areas become "Bonus Learning" at the end of the plan.

## Step 4: Spawn Parallel Research Agents

Use the `Agent` tool to spawn **one research subagent per priority area** (6 agents total). Launch all 6 in the **same message** so they run in parallel — this is important for speed.

Use this prompt template for each agent, filling in the bracketed values:

---

You are a research agent for BombBomb's AI onboarding program.

Your task: Research the following AI learning area and produce a structured summary tailored to a specific BombBomb employee.

**Learning Area**: [AREA_TITLE — AREA_TAGLINE]
**Area Focus**: [AREA_DESCRIPTION from areas.md]
**Employee Role**: [ROLE]
**AI Knowledge Level**: [LEVEL]

BombBomb context: BombBomb is a video messaging platform that helps professionals build relationships through personal video. The company's mission centers on human-centered communication — helping salespeople, customer success teams, and other professionals connect authentically with customers and prospects through video.

Use WebSearch to find current (2024-2025) information. Then write the following structured summary:

## [AREA_TITLE]
### [AREA_TAGLINE]

### What This Is
2-3 sentences covering what this topic is and why it matters for AI-enabled professionals in 2025.

### Why It Matters for [ROLE] at BombBomb
3-4 sentences. Be concrete and specific — how does this topic apply to their actual day-to-day work? Reference video messaging, relationship selling, customer communication, or whatever is most relevant to the role.

### Core Concepts (for [LEVEL] learners)
A bulleted list of 5-7 key concepts, techniques, or mental models at the right depth:
- Beginners: foundational ideas, plain-language definitions, zero jargon
- Intermediate: practical patterns, workflow integration, real tool names
- Advanced: optimization techniques, edge cases, architectural considerations

### Quick Wins — Try This Today
2-3 specific, immediately actionable exercises with step-by-step instructions. Include at least one example prompt (in a code block) if the area involves prompting.

### BombBomb-Specific Applications
2-3 concrete ways this applies to BombBomb's products, internal workflows, or customer scenarios. Be specific — mention video scripts, follow-up sequences, customer health scoring, etc. as relevant.

### Resources to Go Deeper
3-5 high-quality resources (articles, tools, courses, communities) with URLs. Focus on resources that are free or widely accessible. Prefer 2024-2025 sources.

Return only the structured summary above — no preamble, no closing remarks.

---

## Step 5: Compile the Learning Plan

Once all 6 research agents return, read `references/prompts.md` for the role-specific prompt library, then compile everything into a single Markdown document using this structure:

```
# AI Learning Plan: [ROLE] at BombBomb
**Knowledge Level**: [LEVEL] | **Generated**: [DATE]

---

## Welcome to Your AI Journey

[3 paragraphs, warm and encouraging tone]
- Para 1: Why AI matters right now, especially at BombBomb
- Para 2: What this plan covers and how to use it  
- Para 3: A reminder that AI amplifies human connection — it doesn't replace it.

---

## Your Learning Path

[The 6 research summaries, in priority order]

---

## Bonus Areas to Explore Later

[For the remaining 4 areas: 2-3 sentence teaser for each]

---

## Your 30-60-90 Day Roadmap

### Week 1-2: Quick Wins (Start Here)
### Days 15-30: Building Habits
### Days 31-60: Going Deeper
### Days 61-90: Measuring Impact

---

## AI Toolkit: Your Starting Stack

[6-8 curated tools for this role with name, description, URL]

---

## Copy-Paste Prompts for [ROLE]

[6-8 ready-to-use prompts from references/prompts.md, formatted with "When to use" + code block]

---

## Staying Current

[Newsletters, communities, internal BombBomb channels]

---
*This plan was created for your specific role and experience level. Revisit every 90 days.*
```

## Step 6: Save and Deliver

1. Save the compiled learning plan as `bb-ai-learning-plan-[role-slug]-[level-slug].md` (e.g., `bb-ai-learning-plan-sales-beginner.md`)
2. Generate a PDF version using the bundled script:
   - Ensure `reportlab` is installed: `pip install reportlab --break-system-packages -q`
   - Run: `python3 <skill_base_dir>/scripts/make_pdf.py <path/to/plan.md> <path/to/plan.pdf>`
   - The output PDF will use BombBomb's blue/orange branding and handle all markdown formatting
3. Share **both** the `.md` and `.pdf` files with the user via `computer://` links — the PDF is the primary deliverable
4. Give a 3-5 sentence verbal summary highlighting the top 2-3 areas and the roadmap

## Quality Principles

**Be BombBomb-specific**: Every section should feel written for a BombBomb employee, not a generic tech worker. Connect every concept to video messaging, relationship selling, or BombBomb's human-first culture.

**Match the knowledge level precisely**:
- Beginners: no unexplained acronyms, focus on "why" before "how", lots of concrete examples
- Intermediate: assume ChatGPT familiarity, focus on workflow integration and combining tools
- Advanced: focus on optimization, tradeoffs, architecture, and emerging capabilities

**Stay actionable**: Every section should have something doable within 24 hours.

**Be encouraging**: Frame AI as a powerful ally for doing more meaningful work. BombBomb's human-first values apply here — AI amplifies authentic connection, it doesn't replace it.
