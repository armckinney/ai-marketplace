---
name: interview-prep
description: >-
  Stage-aware interview preparation toolkit. Researches the target company,
  maps verified career achievements into a JD-aligned CAR story matrix, and
  builds standardized round subdirectories (recruiter, hiring-manager, coding,
  design, team-member, leadership-values, and optional final onsite bundles)
  with three progressive study tiers (review.md, cheatsheet.md, scan-sheet.md)
  plus a role README navigation hub. Use when preparing for an upcoming
  interview loop or specific interview round.
---

# Interview Prep

Prepare systematically for a target role using a **two-phase, standardized round-directory workflow**: build the shared research, CAR story matrix, and role navigation hub first, then generate progressive three-tier study artifacts inside dedicated round subdirectories on demand.

## Procedure

### 1. Intake & Context Resolution

- Require the **Target Company Name** and **Target Job Description** (pasted text, local JD snapshot inside the role folder, or non-login-gated URL).
- Determine which interview round(s) to prepare (`recruiter`, `hiring_manager`, `coding`, `design`, `team_member`, `leadership_values`, `final`, or `all`) and whether the user wants all 3 tiers or specific tier(s) (`review.md`, `cheatsheet.md`, `scan-sheet.md`). If unspecified, ask which upcoming round(s) to generate alongside Phase 1.
- Resolve output directory: `career-kit/docs/interview-prep/<company-slug>/<YYYY-MM>_<role-slug>/`.
- Read all available candidate context (**strictly read-only** except `career_profile.md`):
  - `career-kit/docs/refs/career_profile.md` (if missing, pre-draft from `master_resume.md`, `role-interests.csv`, and `base-interview-questions.md` when present, then interview the user to confirm gaps using [career_profile_template.md](../achievement-distiller/templates/career_profile_template.md))
  - `career-kit/docs/refs/master_resume.md` and `career-kit/docs/refs/linkedin_profile.md` (never scrape LinkedIn URLs; ask the user to paste/export text)
  - `career-kit/docs/refs/role-interests.csv` (values, role archetypes, domain interests, company targets)
  - `career-kit/docs/refs/base-interview-questions.md` (reusable career arc, push/pull motivations, default interviewer questions)
  - `career-kit/docs/refs/achievements_*.md` and `career-kit/docs/refs/achievement_stories.csv` (also check legacy spelling `archievement_stories.csv`)
  - All distilled files in `career-kit/docs/achievements/*.md` and any matching resume in `career-kit/docs/tailored-resumes/`
- **Raw Packet & Legacy File Discovery**:
  - Scan `<role-dir>/` for unmodified external files (`*.html`, `*.pdf`, `*.docx.md`, `[Candidate Prep]*`, `Candidate Prep_*`, and user scratchpads) and ingest them as authoritative loop context—**never modify or overwrite them**.
  - If `<role-dir>/relevant_achievements.md` exists, read it as a Phase 1 companion or legacy alias to `car_story_matrix.md` without forcing manual renaming. Similarly, read any pre-existing flat round files when upgrading an older role folder.

### 2. Phase 1: Core Foundation & Navigation Hub (Always Create or Update First)

Create or update these three foundational artifacts inside `<role-dir>/` before generating round subdirectories:

1. **`company_profile.md`** ([template](templates/company_profile.md)):
   - Synthesize public mission, core products, engineering blog insights, target tech stack, stated values, current engineering challenges, and interview loop structure (incorporating any preserved official prep packets).
   - Cite only verified public sources or provided packets; label inferred loop details explicitly.
2. **`car_story_matrix.md`** ([template](templates/car_story_matrix.md)):
   - Map the candidate's highest-fit verified achievements (from `achievements/`, `refs/`, and `relevant_achievements.md` if present) to the JD's top technical/domain mandates and behavioral competencies (Ownership & Initiative, Technical Complexity & Scale, Cross-Team Collaboration & Conflict, Failure & Incident Recovery).
   - Write natural **CAR** narratives (*Challenge/Context -> Action -> Result*) with 3-bullet triggers and confirmed **Leadership Principles**, **Technologies**, and **Domains** tags. Never invent metrics or guess unstated technologies.
3. **`README.md`** ([template](templates/role_readme.md)):
   - Create/update the role-level navigation hub indexing core foundation files, preserved external packets, every round directory and tier file, and a loop progress checklist. Keep `README.md` in sync whenever rounds or tiers are added.

### 3. Phase 2: Standardized Round Subdirectories & 3 Progressive Tiers

Every interview round lives in its own subdirectory under `<role-dir>/`:

| Round Key | Directory | Domain Blueprint Template |
| :--- | :--- | :--- |
| `recruiter` | `recruiter/` | [recruiter_screen.md](templates/recruiter_screen.md) |
| `hiring_manager` | `hiring-manager/` | [hiring_manager.md](templates/hiring_manager.md) |
| `coding` | `coding/` | [technical_interview.md](templates/technical_interview.md) |
| `design` | `design/` | [system_design.md](templates/system_design.md) |
| `team_member` | `team-member/` | [team_member.md](templates/team_member.md) |
| `leadership_values` | `leadership-values/` | [leadership_values.md](templates/leadership_values.md) |

#### Progressive Study Tiers (Per Round Directory)

Generate all three tiers inside `<role-dir>/<round>/` when a round is requested (unless the user asks for specific tier(s) only):

| Tier File | Reading Window | Purpose & Grounding |
| :--- | :--- | :--- |
| **`review.md`** | Days before | Deep-dive study guide following the round's domain blueprint template: full CAR stories, architecture/coding drills, tradeoffs, and self-quiz grounded in `company_profile.md`, `car_story_matrix.md`, and official prep packets. |
| **`cheatsheet.md`** | 10–15 min before | Condensed pre-call briefing modeled on [interview_cheat_sheet.md](templates/interview_cheat_sheet.md): phase clock, opening pitch, scored evaluation signals, top 3–6 CAR 3-bullet triggers, and prioritized interviewer questions. |
| **`scan-sheet.md`** | During live call | Ultra-dense telegraphic checklist modeled on [round_scan_sheet.md](templates/round_scan_sheet.md): single-screen cues, headline numbers, red-flag guards, and top closing questions. |

- **Personal Question & Values Calibration**: Pull reusable narrative framing and default candidate-to-interviewer questions from `refs/base-interview-questions.md` and role/culture alignment criteria from `refs/role-interests.csv` when drafting `recruiter/`, `hiring-manager/`, `team-member/`, and `leadership-values/`.
- **Optional `final/` Onsite Bundle**: When advancing to a multi-session virtual or onsite loop, optionally create `final/` containing `final/master_prep_plan.md` (loop schedule, cross-session story de-duplication map, energy/transition plan), `final/prep/` (deep session reviews), and `final/cheatsheet/` (pre-call sheets), and link it from `<role-dir>/README.md`.

### 4. Summary & Next Steps

- Report exact files created or updated with clickable links, confirm `<role-dir>/README.md` reflects the current loop state, and note which round directories remain ungenerated for later stages.
