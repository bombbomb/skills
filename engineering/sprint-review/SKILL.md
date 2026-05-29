---
name: sprint_review
description: Generates a comprehensive Sprint Review document for the bi-weekly Sprint Review agile meeting, auto-populated with live data from Jira (bombbomb.atlassian.net). Runs every two weeks on Wednesday.
---

# Sprint Review Skill

## Overview
This skill automatically generates a structured Sprint Review document to support the bi-weekly Sprint Review agile ceremony. It queries live sprint data from Jira and produces a consistent, comprehensive document covering all key aspects of the sprint review meeting.

## Schedule
- **Frequency:** Every two weeks on Wednesday
- **Time:** 10:00 AM (local time)
- **Automation ID:** c8ad569e-9d4a-4e7f-b213-d4d65a783892

## Jira Integration
- **Instance:** bombbomb.atlassian.net
- **Cloud ID:** 2ff71add-6cd0-40ce-98ca-c13c32cc9e9a
- **Primary Project:** ENGI (Product Engineering)
- **Additional Projects:** MOB (Mobile), EX (FUNdations), VX (Foundations Team), MON (Money) — optional, add as needed
- **Sprint Query:** `project = ENGI AND sprint in openSprints() ORDER BY status ASC`
- **Done Items Query:** `project = ENGI AND sprint in openSprints() AND status = Done ORDER BY updated DESC`
- **Incomplete Items Query:** `project = ENGI AND sprint in openSprints() AND status != Done ORDER BY status ASC`

## Usage
This skill is triggered automatically on a bi-weekly Wednesday schedule. It can also be invoked manually by asking:
> "Generate a Sprint Review document for today's sprint."

When run, it will:
1. Query Jira for all issues in the current open sprint(s)
2. Separate issues into **Done** and **Not Done** categories
3. Calculate sprint metrics from the live data
4. Populate the Sprint Review document template with real issue data
5. Save the result as a note titled `Sprint Review – [Today's Date]`

## Output
The skill produces a fully structured Sprint Review document saved as a note titled `Sprint Review – [Today's Date]`.

## Document Sections
1. 📋 **Sprint Overview** — Sprint goal, dates, team, Scrum Master, Product Owner
2. ✅ **Completed Work** — Live table of Done issues from Jira with issue key, summary, type, and assignee
3. ❌ **Incomplete Work** — Live table of In Progress / To Do / Pending issues with status
4. 📊 **Sprint Metrics** — Issue counts, bugs fixed, critical bugs, story points (if available)
5. 🎯 **Sprint Goal Assessment** — Outcomes vs. expectations
6. 🚀 **Product Increment / Demo Highlights** — Key completed features with Jira links
7. 💬 **Stakeholder Feedback** — Captured during the review meeting
8. 🔄 **Backlog Updates** — New, reprioritized, or removed backlog items
9. 🔍 **Key Decisions & Action Items** — Owners and due dates
10. 📅 **Next Sprint Preview** — Carry-over items, draft goal, tentative start date

## Prompt

```
You are generating a Sprint Review document for today's Sprint Review meeting.

Today's date is: [Today's Date]
Jira instance: bombbomb.atlassian.net
Cloud ID: 2ff71add-6cd0-40ce-98ca-c13c32cc9e9a
Primary Project: ENGI (Product Engineering)

Step 1 — Query Jira for active sprint data:
- Fetch all issues in the open sprint: `project = ENGI AND sprint in openSprints() ORDER BY status ASC`
- Separate issues into two groups:
  - DONE: status = "Done"
  - NOT DONE: status in ("To Do", "In Progress", "Code Review", "Ready for Prod", "Pending Approval")

Step 2 — Calculate sprint metrics:
- Count total issues, done issues, and not-done issues
- Count bugs fixed (Done + issuetype = Bug)
- Count critical/high bugs still in progress
- Sum story points if available (customfield_10016); note "Not tracked" if null

Step 3 — Generate the Sprint Review document using the structure below, populating all sections with real Jira data. Include Jira issue links in the format: https://bombbomb.atlassian.net/browse/[ISSUE-KEY]

---

# 🏁 Sprint Review — ENGI | [Today's Date]

## 1. 📋 Sprint Overview
- **Sprint Goal:** [To be filled in by Scrum Master]
- **Sprint Dates:** [Sprint start date] – [Today's Date]
- **Team:** Product Engineering (ENGI)
- **Scrum Master:** [To be filled in]
- **Product Owner:** [To be filled in]

## 2. ✅ Completed Work (Done)
| Issue | Summary | Type | Assignee |
|---|---|---|---|
[Populate from Jira Done issues]

## 3. ❌ Incomplete Work (Not Done / Carried Over)
| Issue | Summary | Type | Assignee | Status |
|---|---|---|---|---|
[Populate from Jira Not Done issues]

## 4. 📊 Sprint Metrics
- **Total Issues in Sprint:** [N]
- **Issues Completed (Done):** [N]
- **Issues Remaining:** [N]
- **Bugs Fixed:** [N]
- **Critical/High Bugs Still In Progress:** [N]
- **Story Points Completed:** [N or "Not tracked"]

## 5. 🎯 Sprint Goal Assessment
[To be filled in during the meeting]

## 6. 🚀 Product Increment / Demo Highlights
[List the top completed features/fixes from Jira Done items, with issue links and a brief description of value delivered]

## 7. 💬 Stakeholder Feedback
[To be filled in during the meeting]

## 8. 🔄 Backlog Updates
- **New Items Added:** [To be filled in]
- **Items Reprioritized:** [To be filled in]
- **Items Removed:** [To be filled in]

## 9. 🔍 Key Decisions & Action Items
| # | Decision/Action | Owner | Due Date |
|---|---|---|---|
[Populate carry-over critical/high items from Jira Not Done list as suggested action items]

## 10. 📅 Next Sprint Preview
- **Next Sprint Goal (Draft):** [To be filled in]
- **Tentative Start Date:** [Today's Date + 1 business day]
- **Carry-Over High Priority Items:**
[List top carry-over items from Jira Not Done, prioritized by Critical > High priority]

---

*Document auto-generated from Jira project ENGI (Product Engineering) active sprint data on [Today's Date]. Please complete all [placeholder] sections before distributing.*

Save this document as a note titled "Sprint Review – [Today's Date]".
```

## Notes
- Fields marked `[To be filled in]` should be completed during or after the Sprint Review meeting.
- Story points are stored in Jira custom field `customfield_10016`; they are often null in this project.
- To include additional projects (MOB, EX, VX, MON), extend the JQL query: `project in (ENGI, MOB, EX) AND sprint in openSprints()`.
- Jira issue links follow the format: `https://bombbomb.atlassian.net/browse/[ISSUE-KEY]`
