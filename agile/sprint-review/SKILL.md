---
name: sprint_review
description: Generates a comprehensive Sprint Review document for the bi-weekly Sprint Review agile meeting. Runs every two weeks on Wednesday.
---

# Sprint Review Skill

## Overview
This skill automatically generates a structured Sprint Review document to support the bi-weekly Sprint Review agile ceremony. It produces a consistent, comprehensive document that covers all key aspects of the sprint review meeting.

## Schedule
- **Frequency:** Every two weeks on Wednesday
- **Time:** 10:00 AM (local time)
- **Automation ID:** c8ad569e-9d4a-4e7f-b213-d4d65a783892

## Usage
This skill is triggered automatically on a bi-weekly Wednesday schedule. It can also be invoked manually by asking:
> "Generate a Sprint Review document for today's sprint."

## Output
The skill produces a fully structured Sprint Review document saved as a note titled `Sprint Review – [Today's Date]`.

## Document Sections
1. 📋 **Sprint Overview** — Sprint goal, dates, team, Scrum Master, Product Owner
2. ✅ **Completed Work** — Table of done user stories/tasks with story points
3. ❌ **Incomplete Work** — Carried-over items with reasons
4. 📊 **Sprint Metrics** — Velocity, completion rate, bug counts
5. 🎯 **Sprint Goal Assessment** — Outcomes vs. expectations
6. 🚀 **Product Increment / Demo Highlights** — Features delivered and demo notes
7. 💬 **Stakeholder Feedback** — Feedback captured during the review
8. 🔄 **Backlog Updates** — New, reprioritized, or removed backlog items
9. 🔍 **Key Decisions & Action Items** — Owners and due dates
10. 📅 **Next Sprint Preview** — Draft goal, start date, high-priority items

## Prompt

```
Generate a comprehensive Sprint Review document for today's Sprint Review meeting. The document should be well-structured and include the following sections:

# 🏁 Sprint Review — [Sprint Name/Number] | [Today's Date]

## 1. 📋 Sprint Overview
- **Sprint Goal:** [State the sprint goal]
- **Sprint Dates:** [Start Date] – [End Date]
- **Team:** [Team name or members]
- **Scrum Master:** [Name]
- **Product Owner:** [Name]

## 2. ✅ Completed Work (Done)
A table or list of all user stories / tasks completed this sprint:
| Story/Task | Description | Story Points | Status |
|---|---|---|---|
| [ID] | [Summary] | [Points] | ✅ Done |

## 3. ❌ Incomplete Work (Not Done / Carried Over)
List any items that were planned but not completed, with a brief reason:
| Story/Task | Description | Story Points | Reason |
|---|---|---|---|
| [ID] | [Summary] | [Points] | [Reason] |

## 4. 📊 Sprint Metrics
- **Total Story Points Planned:** [X]
- **Total Story Points Completed:** [Y]
- **Velocity:** [Y pts]
- **Sprint Completion Rate:** [Y/X * 100]%
- **Number of Bugs Fixed:** [N]
- **Number of New Bugs Introduced:** [N]

## 5. 🎯 Sprint Goal Assessment
Did the team achieve the sprint goal? Provide a brief summary of outcomes vs. expectations.

## 6. 🚀 Product Increment / Demo Highlights
Key features or functionality delivered and demonstrated to stakeholders:
- **Feature 1:** [Brief description and value delivered]
- **Feature 2:** [Brief description and value delivered]
- **Live Demo Notes:** [Any notes from the demo]

## 7. 💬 Stakeholder Feedback
Capture feedback received from stakeholders during the review:
- [Stakeholder name/role]: "[Feedback]"

## 8. 🔄 Backlog Updates
Changes to the product backlog as a result of this sprint review:
- **New Items Added:** [List]
- **Items Reprioritized:** [List]
- **Items Removed:** [List]

## 9. 🔍 Key Decisions & Action Items
| # | Decision/Action | Owner | Due Date |
|---|---|---|---|
| 1 | [Description] | [Name] | [Date] |

## 10. 📅 Next Sprint Preview
Brief overview of what's planned for the next sprint:
- **Next Sprint Goal (Draft):** [Goal]
- **Tentative Start Date:** [Date]
- **High-Priority Items:** [List top 3–5 items]

---

*Document prepared for the Sprint Review meeting on [Today's Date]. Please update all placeholder fields with actual sprint data before distributing.*

Save this document as a note titled "Sprint Review – [Today's Date]".
```

## Notes
- Update all placeholder fields with actual sprint data before distributing.
- Can be customized to include your team name, sprint naming convention, or additional sections specific to your workflow.
