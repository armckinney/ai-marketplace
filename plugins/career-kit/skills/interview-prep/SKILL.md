---
name: interview-prep
description: >-
  Stage-aware interview preparation toolkit. Researches the target company,
  maps verified career achievements into a JD-aligned CAR story matrix
  (Challenge/Context, Action, Result), and builds focused round-specific study
  sheets on demand (Recruiter, Hiring Manager, Technical/Coding, System Design,
  Peer/Team Member, Leadership/Values, and Quick-Scan Cheat Sheet). Use when
  preparing for an upcoming interview loop or specific interview round.
---

# Interview Prep

Prepare systematically for a target role using a **two-phase, stage-aware workflow**: always build the shared research and CAR story foundation first, then generate only the round-specific study guides needed for upcoming interviews.

## Procedure

1. **Intake & Context Resolution**:
   - Require the **Target Company Name** and **Target Job Description** (pasted text or non-login-gated URL).
   - Determine which interview stage(s) the user is preparing for (`recruiter`, `hiring_manager`, `technical`, `system_design`, `team_member`, `leadership_values`, `cheat_sheet`, or `all`). If unspecified, ask which upcoming round(s) to generate alongside the core foundation.
   - Read all available candidate context:
     - `career-kit/docs/refs/career_profile.md` (if missing, pause to bootstrap it using [career_profile_template.md](../achievement-distiller/templates/career_profile_template.md))
     - `career-kit/docs/refs/master_resume.md`
     - `career-kit/docs/refs/linkedin_profile.md` (never scrape LinkedIn URLs; instruct the user to paste/export text if missing)
     - `career-kit/docs/refs/achievements_*.md`
     - All distilled files in `career-kit/docs/achievements/*.md`
     - Any matching tailored resume in `career-kit/docs/tailored-resumes/`
   - Keep `master_resume.md`, `linkedin_profile.md`, and `refs/achievements_*.md` **strictly read-only**.
   - Resolve output directory: `career-kit/docs/interview-prep/<company-slug>/<YYYY-MM>_<role-slug>/`.

2. **Phase 1: Core Foundation (Always Generate or Update First)**:
   Create both foundational artifacts inside the role output directory before generating round sheets:
   - **`company_profile.md`** (follow [company_profile.md](templates/company_profile.md)):
     - Use web search and URL-reading tools (respecting login-wall limits) to synthesize the company's mission, core products, engineering blog insights, target tech stack, stated values/cultural pillars, current engineering challenges, and typical interview loop structure.
     - Cite only observed facts from public sources or the user's JD; mark any inferred loop details explicitly.
   - **`car_story_matrix.md`** (follow [car_story_matrix.md](templates/car_story_matrix.md)):
     - Extract the candidate's highest-fit achievements from `achievements/` and `refs/`.
     - Map stories to both the JD's top technical/domain requirements and core behavioral competencies (Ownership & Initiative, Technical Complexity & Scale, Cross-Team Collaboration & Conflict, Failure & Incident Recovery).
     - Write complete, natural **CAR** narratives (*Challenge/Context -> Action -> Result*) paired with rapid memory-trigger bullets and structured **Leadership Principles**, **Technologies**, and **Domains** tags on every story for quick filtering. Never invent metrics or guess unstated technologies; ask the user to confirm missing details.

3. **Phase 2: Stage-Specific Study Sheets (Generate On Demand)**:
   Generate only the requested round file(s) inside `career-kit/docs/interview-prep/<company-slug>/<YYYY-MM>_<role-slug>/`, grounding every talking point in `company_profile.md`, `car_story_matrix.md`, `career_profile.md`, and the JD:
   - **`recruiter_screen.md`** ([template](templates/recruiter_screen.md)): 60-second background pitch, company/role motivation hook, logistics/archetype clarifying questions, and compensation guardrails pulled from `career_profile.md` (omit comp specifics if not configured).
   - **`hiring_manager.md`** ([template](templates/hiring_manager.md)): 2-minute targeted narrative, top 3–4 JD-mapped CAR stories, and high-signal questions probing role archetype, 90-day priorities, ownership boundaries, and team operating model.
   - **`technical_interview.md`** ([template](templates/technical_interview.md)): 7-step tactical coding/debugging execution loop, language-specific idioms tailored dynamically to the target JD and candidate's primary interview language, and technical governance questions.
   - **`system_design.md`** ([template](templates/system_design.md)): Time-boxed 45-minute architecture checklist tailored to the target company's scale and domain, plus relevant architectural CAR stories to weave into tradeoffs.
   - **`team_member.md`** ([template](templates/team_member.md)): Peer collaboration focus, shared engineering practices, and questions probing code review/RFC culture, deployment velocity, operational load, and day-to-day friction points.
   - **`leadership_values.md`** ([template](templates/leadership_values.md)): Explicit mapping of candidate CAR stories to each of the company's cultural values from `company_profile.md`, plus strategic 2–3 year vision and organizational bottleneck questions.
   - **`interview_cheat_sheet.md`** ([template](templates/interview_cheat_sheet.md)): Single-page live-interview quick-scan sheet summarizing the 30-second pitch, CAR story 3-bullet triggers (`C` / `A` / `R`), domain reference numbers, and top questions to ask.

4. **Summary & Next Steps**:
   - Report the exact files created/updated with clickable links and note which optional round sheets remain ungenerated so the user can request them as their loop progresses.
