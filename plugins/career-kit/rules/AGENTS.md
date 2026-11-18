# Career Kit Rules

Always-on guardrails and conventions applied when `career-kit` is active.

## Core Principles

1. **Plugin-Isolated Workspace Structure**:
   - Resolve and store all career context and deliverables relative to the active workspace under `career-kit/docs/`:
     - `career-kit/docs/refs/`: Baseline context (`career_profile.md`, `master_resume.md`, `linkedin_profile.md`, and any static `achievements_*.md`).
     - `career-kit/docs/achievements/`: Distilled CAR stories and XYZ bullet banks (`<company>.md`).
     - `career-kit/docs/tailored-resumes/`: Role-tailored resumes (`<company>_<role-slug>.md`).
     - `career-kit/docs/interview-prep/<company>/<YYYY-MM>_<role-slug>/`: Company intelligence, CAR story matrices, and round-specific prep sheets.
2. **Reference Immutability & Profile Bootstrapping**:
   - Treat `master_resume.md`, `linkedin_profile.md`, and existing `refs/achievements_*.md` as strictly read-only. Never overwrite or delete them.
   - If `career-kit/docs/refs/career_profile.md` is missing when a skill runs, interview the user to capture their contact details, target roles/levels, core strategic themes, and company-by-company growth arc, then persist `career_profile.md` for future sessions.
3. **Zero Fabrication & Clarification Gate**:
   - Never invent, extrapolate, or inflate metrics, technologies, titles, team sizes, or architectural scope.
   - When an initiative or Job Description (JD) requirement lacks concrete metrics or verifiable evidence in `refs/` or `achievements/`, **stop and ask targeted clarifying questions** before drafting.
4. **CAR + XYZ Narrative Standards**:
   - **CAR Format (Stories & Interview Prep)**: Structure multi-sentence narratives as **Challenge/Context** (problem, stakes, constraints, role) -> **Action** (specific technical and leadership decisions you drove) -> **Result** (quantified business, operational, or organizational outcome). Include three structured filter tags on every CAR story:
     - **Leadership Principles**: Inferred from the story and confirmed with the user (standard options: `Customer Focus`, `Continuous Improvement`, `Data Driven`, `Action Oriented`, `Dive Deep`, `Innovative`, `Ownership`, `Results Oriented`, `Collaborative`, `Adaptability`, `Prioritize Collective`, or custom principles in `career_profile.md`).
     - **Technologies**: Explicitly prompted and confirmed from the user (never guessed).
     - **Domains**: High-level discipline or outcome filter tags (inferred and confirmed against `career_profile.md` or the 18-tag standard taxonomy across Platform & Infrastructure, Data & AI/ML, Software & Architecture, Security & Operations, and Impact & Experience). Keep specific languages, databases, or tools (e.g., `SQL`, `PostgreSQL`, `Kubernetes`) in **Technologies**, not **Domains**.
   - **XYZ Formula (Resume Bullets)**: Structure single-bullet achievements as *Accomplished [X] as measured by [Y], by doing [Z]*.
   - Lead with varied, high-impact action verbs; use single quotes (`'`) instead of double quotes (`"`) inside XYZ bullets if quoting is needed; eliminate passive language, keyword stuffing, and generic corporate filler.
5. **Privacy & Web Scraping Boundaries**:
   - Do not introduce proprietary internal tool names, confidential data, or sensitive client details unless explicitly provided by the user for their local workspace.
   - Never attempt to scrape login-walled sites (such as LinkedIn); instruct the user to export or paste profile text into `career-kit/docs/refs/linkedin_profile.md`.
