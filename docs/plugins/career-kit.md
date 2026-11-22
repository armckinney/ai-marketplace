# `career-kit` Plugin

- **Version**: `1.0.0`
- **License**: `Apache-2.0`
- **Source**: [`plugins/career-kit/`](../../plugins/career-kit)

## Purpose

Provides an isolated, token-efficient toolkit for career development workflows—distilling raw engineering initiatives into **CAR** (*Challenge/Context -> Action -> Result*) stories and **XYZ** resume bullets, curating tailored resumes with interactive JD gap verification, and generating standardized multi-tier interview preparation packets. Keeping this workflow separate from `dev-essentials` prevents career rules and skill metadata from loading during routine coding sessions.

## What's Included

| Component | Path | Summary |
| :--- | :--- | :--- |
| **Ruleset** | [`rules/AGENTS.md`](../../plugins/career-kit/rules/AGENTS.md) | 5 always-on career workflow principles (auto-loaded in Antigravity). |
| **Skills (3)** | [`skills/`](../../plugins/career-kit/skills) | Cross-harness workflows for achievement distillation, resume curation, and standardized multi-tier interview prep. |
| **Subagents** | — | None included (minimal token footprint). |

## Workspace Context Layout

All `career-kit` skills read and write relative to the user's active workspace under `career-kit/docs/`:

```text
career-kit/docs/
├── refs/                     # Read-only baseline context (master_resume.md, linkedin_profile.md,
│                             # role-interests.csv, base-interview-questions.md, achievements_*.md,
│                             # achievement_stories.csv / archievement_stories.csv) + editable career_profile.md
├── achievements/             # Distilled CAR stories & XYZ bullet banks (<company-slug>.md)
├── tailored-resumes/         # Role-tailored resumes (<company-slug>_<role-slug>.md)
├── application-answers/      # Screening & essay responses (<company-slug>_<role-slug>.md)
├── resignations/             # Career transition plans (<company-slug>/)
├── hiring/                   # Interviewer scorecards & calibration rubrics (distinct from interview-prep/)
└── interview-prep/           # <company-slug>/<YYYY-MM>_<role-slug>/
    ├── README.md             # Role navigation hub & loop stage checklist
    ├── company_profile.md    # Phase 1 company intelligence
    ├── car_story_matrix.md   # Phase 1 JD-mapped CAR stories (honors legacy relevant_achievements.md)
    ├── <external packets>    # Preserved read-only JDs (.html/.pdf/.docx.md) & [Candidate Prep]* files
    ├── <round>/              # recruiter/, hiring-manager/, coding/, design/, team-member/, leadership-values/
    │   ├── review.md         # Deep study guide (days before)
    │   ├── cheatsheet.md     # Condensed pre-call briefing (10–15 min before)
    │   └── scan-sheet.md     # Ultra-dense telegraphic live-call checklist (during call)
    └── final/                # Optional onsite bundle (master_prep_plan.md, prep/, cheatsheet/)
```

If `career-kit/docs/refs/career_profile.md` is missing, any `career-kit` skill pre-populates draft fields from `master_resume.md`, `role-interests.csv`, and `base-interview-questions.md` when available before interviewing the user to confirm gaps from [`career_profile_template.md`](../../plugins/career-kit/skills/achievement-distiller/templates/career_profile_template.md).

## Top-Level Ruleset (`rules/AGENTS.md`)

1. **Plugin-Isolated Workspace Structure**: Standardizes inputs and deliverables across all 7 career lifecycle directories under `career-kit/docs/`.
2. **Reference Immutability & Smart Profile Bootstrapping**: Protects all baseline `refs/` files (except `career_profile.md`) and raw external JD / `[Candidate Prep]*` packets as strictly read-only, while smart-bootstrapping `career_profile.md` when absent.
3. **Zero Fabrication & Clarification Gate**: Prohibits inventing or inflating metrics, tools, or scope; pauses to ask clarifying questions whenever evidence is missing.
4. **CAR + XYZ Narrative Standards**: Enforces **CAR** (tagged with **Leadership Principles**, confirmed **Technologies**, and the 18-tag **Domains** taxonomy for navigation/filtering) for behavioral stories and **XYZ** (*Accomplished [X] as measured by [Y], by doing [Z]*) for resume bullets, with single quotes inside bullets and active impact verbs.
5. **Privacy & Web Scraping Boundaries**: Never scrapes login-walled platforms (such as LinkedIn) and excludes confidential internal tooling unless explicitly provided by the user.

## Skills

| Skill | When to Use | Key Details | Templates |
| :--- | :--- | :--- | :--- |
| **`achievement-distiller`** | Capturing brag-doc work logs, PR summaries, CSV story rows (`achievement_stories.csv` / `archievement_stories.csv`), or rough bullets into polished stories and resume lines. | Runs a diagnostic interview on Context/Action/Result facts plus **Leadership Principles** (11-principle taxonomy), **Technologies** (prompted, never guessed), and **Domains** (18-tag standard taxonomy); outputs 1 natural **CAR story** + **2–3 XYZ bullet variants** and appends to `career-kit/docs/achievements/<company-slug>.md`. | [`career_profile_template.md`](../../plugins/career-kit/skills/achievement-distiller/templates/career_profile_template.md), [`car_xyz_achievement_template.md`](../../plugins/career-kit/skills/achievement-distiller/templates/car_xyz_achievement_template.md) |
| **`resume-curator`** | Tailoring a resume or CV to a specific Job Description (JD). | Decomposes the JD calibrated against `career_profile.md` and `refs/role-interests.csv`, maps across `refs/` (including CSV stories) and `achievements/`, **pauses to verify critical gaps** before drafting, writes recency-weighted XYZ bullets to `career-kit/docs/tailored-resumes/<company-slug>_<role-slug>.md`, and outputs a Fit & Keyword Coverage table. | [`tailored_resume_template.md`](../../plugins/career-kit/skills/resume-curator/templates/tailored_resume_template.md) |
| **`interview-prep`** | Preparing for an interview loop or specific interview round. | Standardized 2-phase workflow: creates/updates `company_profile.md`, `car_story_matrix.md` (honoring `relevant_achievements.md`), and role `README.md` hub while ingesting read-only raw JDs and `[Candidate Prep]*` packets; builds round directories (`recruiter/`, `hiring-manager/`, `coding/`, `design/`, `team-member/`, `leadership-values/`, optional `final/`) with 3 progressive tiers (`review.md`, `cheatsheet.md`, `scan-sheet.md`). | [`templates/`](../../plugins/career-kit/skills/interview-prep/templates) (includes [`role_readme.md`](../../plugins/career-kit/skills/interview-prep/templates/role_readme.md), [`round_scan_sheet.md`](../../plugins/career-kit/skills/interview-prep/templates/round_scan_sheet.md)) |
