# Career Kit Rules

Always-on guardrails and conventions applied when `career-kit` is active.

## Core Principles

1. **Plugin-Isolated Workspace Structure**:
   Resolve and store all career context and deliverables relative to the active workspace under `career-kit/docs/`:

   | Directory | Purpose & Naming |
   | :--- | :--- |
   | `career-kit/docs/refs/` | Read-only baseline context (`master_resume.md`, `linkedin_profile.md`, `achievements_*.md`, `role-interests.csv`, `base-interview-questions.md`, `achievement_stories.csv` / `archievement_stories.csv`) plus editable `career_profile.md`. |
   | `career-kit/docs/achievements/` | Distilled CAR stories and XYZ bullet banks (`<company-slug>.md`). |
   | `career-kit/docs/tailored-resumes/` | Role-tailored resumes (`<company-slug>_<role-slug>.md`). |
   | `career-kit/docs/interview-prep/<company-slug>/<YYYY-MM>_<role-slug>/` | Role `README.md` hub, `company_profile.md`, `car_story_matrix.md` (or legacy `relevant_achievements.md`), preserved external JD/prep packets, standardized round subdirectories (`<round>/{review.md, cheatsheet.md, scan-sheet.md}`), and optional `final/` onsite bundle. |
   | `career-kit/docs/application-answers/` | Application screening and essay responses (`<company-slug>_<role-slug>.md`). |
   | `career-kit/docs/resignations/<company-slug>/` | Career transition artifacts (strategy, notice speech, formal letter, exit interview notes). |
   | `career-kit/docs/hiring/` | Interviewer scorecards, evaluation rubrics, and calibration templates (kept distinct from candidate-side `interview-prep/`). |

2. **Reference Immutability & Smart Profile Bootstrapping**:
   - Treat all baseline inputs in `career-kit/docs/refs/` except `career_profile.md` (`master_resume.md`, `linkedin_profile.md`, `achievements_*.md`, `role-interests.csv`, `base-interview-questions.md`, `achievement_stories.csv` / `archievement_stories.csv`) as **strictly read-only**. Never overwrite or delete them.
   - Treat unmodified external files inside `interview-prep/` role folders (`*.html`, `*.pdf`, `*.docx.md`, `[Candidate Prep]*`, `Candidate Prep_*`) as **strictly read-only** authoritative loop context.
   - If `career-kit/docs/refs/career_profile.md` is missing when a skill runs, pre-populate draft fields from `master_resume.md`, `role-interests.csv`, and `base-interview-questions.md` when available, then interview the user to confirm and capture remaining details (contact info, target roles/levels, strategic themes, and company growth arc) before persisting `career_profile.md`.

3. **Zero Fabrication & Clarification Gate**:
   - Never invent, extrapolate, or inflate metrics, technologies, titles, team sizes, or architectural scope.
   - When an initiative or Job Description (JD) requirement lacks concrete metrics or verifiable evidence in `refs/` or `achievements/`, **stop and ask targeted clarifying questions** before drafting.

4. **CAR + XYZ Narrative Standards**:
   - **CAR Format (Stories & Interview Prep)**: Structure multi-sentence narratives as **Challenge/Context** (problem, stakes, constraints, role) -> **Action** (specific technical and leadership decisions you drove) -> **Result** (quantified business, operational, or organizational outcome). Tag every CAR story with:
     - **Leadership Principles**: Inferred and confirmed with the user (`Customer Focus`, `Continuous Improvement`, `Data Driven`, `Action Oriented`, `Dive Deep`, `Innovative`, `Ownership`, `Results Oriented`, `Collaborative`, `Adaptability`, `Prioritize Collective`, or custom principles in `career_profile.md`).
     - **Technologies**: Explicitly prompted and confirmed from the user (never guessed).
     - **Domains**: High-level discipline/outcome tags (inferred and confirmed against `career_profile.md` or the 18-tag standard taxonomy). Keep specific languages, databases, or tools (e.g., `SQL`, `PostgreSQL`, `Kubernetes`) in **Technologies**, not **Domains**.
   - **XYZ Formula (Resume Bullets)**: Structure single-bullet achievements as *Accomplished [X] as measured by [Y], by doing [Z]*.
   - Lead with varied, high-impact action verbs; use single quotes (`'`) instead of double quotes (`"`) inside XYZ bullets if quoting is needed; eliminate passive language, keyword stuffing, and generic corporate filler.

5. **Privacy & Web Scraping Boundaries**:
   - Do not introduce proprietary internal tool names, confidential data, or sensitive client details unless explicitly provided by the user for their local workspace.
   - Never attempt to scrape login-walled sites (such as LinkedIn); instruct the user to export or paste profile text into `career-kit/docs/refs/linkedin_profile.md`.
