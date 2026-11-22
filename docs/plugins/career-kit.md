# `career-kit` Plugin

- **Version**: `1.0.0`
- **License**: `Apache-2.0`
- **Source**: [`plugins/career-kit/`](../../plugins/career-kit)

## Purpose

Provides an isolated, token-efficient toolkit for career development workflows—distilling raw engineering initiatives into **CAR** (*Challenge/Context -> Action -> Result*) stories and **XYZ** resume bullets, curating tailored resumes with interactive JD gap verification, and generating stage-specific interview preparation packets. Keeping this workflow separate from `dev-essentials` prevents career rules and skill metadata from loading during routine coding sessions.

## What's Included

| Component | Path | Summary |
| :--- | :--- | :--- |
| **Ruleset** | [`rules/AGENTS.md`](../../plugins/career-kit/rules/AGENTS.md) | 5 always-on career workflow principles (3,548 bytes; auto-loaded in Antigravity). |
| **Skills (3)** | [`skills/`](../../plugins/career-kit/skills) | Cross-harness workflows for achievement distillation, resume curation, and stage-aware interview prep. |
| **Subagents** | — | None included (minimal token footprint). |

## Workspace Context Layout

All `career-kit` skills read and write relative to the user's active workspace under `career-kit/docs/`:

```text
career-kit/docs/
├── refs/                     # Baseline context (master_resume.md, linkedin_profile.md, career_profile.md)
├── achievements/             # Distilled CAR stories & XYZ bullet banks (<company-slug>.md)
├── tailored-resumes/         # Role-tailored resumes (<company-slug>_<role-slug>.md)
└── interview-prep/           # <company-slug>/<YYYY-MM>_<role-slug>/
    ├── company_profile.md
    ├── car_story_matrix.md
    └── <round>.md            # Requested round sheets (recruiter, hiring_manager, technical, system_design, etc.)
```

If `career-kit/docs/refs/career_profile.md` is missing, any `career-kit` skill will interview the user to bootstrap it from [`career_profile_template.md`](../../plugins/career-kit/skills/achievement-distiller/templates/career_profile_template.md).

## Top-Level Ruleset (`rules/AGENTS.md`)

1. **Plugin-Isolated Workspace Structure**: Standardizes inputs and deliverables under `career-kit/docs/`.
2. **Reference Immutability & Profile Bootstrapping**: Protects `master_resume.md`, `linkedin_profile.md`, and static `refs/achievements_*.md` as strictly read-only while bootstrapping `career_profile.md` when absent.
3. **Zero Fabrication & Clarification Gate**: Prohibits inventing or inflating metrics, tools, or scope; pauses to ask clarifying questions whenever evidence is missing.
4. **CAR + XYZ Narrative Standards**: Enforces **CAR** (tagged with **Leadership Principles**, confirmed **Technologies**, and the 18-tag **Domains** taxonomy for navigation/filtering) for behavioral stories and **XYZ** (*Accomplished [X] as measured by [Y], by doing [Z]*) for resume bullets, with single quotes inside bullets and active impact verbs.
5. **Privacy & Web Scraping Boundaries**: Never scrapes login-walled platforms (such as LinkedIn) and excludes confidential internal tooling unless explicitly provided by the user.

## Skills

| Skill | When to Use | Key Details | Templates |
| :--- | :--- | :--- | :--- |
| **`achievement-distiller`** | Capturing brag-doc work logs, PR summaries, or rough bullets into polished stories and resume lines. | Runs a diagnostic interview on Context/Action/Result facts plus **Leadership Principles** (11-principle taxonomy), **Technologies** (prompted, never guessed), and **Domains** (18-tag standard taxonomy); outputs 1 natural **CAR story** + **2–3 XYZ bullet variants** and appends to `career-kit/docs/achievements/<company-slug>.md`. | [`career_profile_template.md`](../../plugins/career-kit/skills/achievement-distiller/templates/career_profile_template.md), [`car_xyz_achievement_template.md`](../../plugins/career-kit/skills/achievement-distiller/templates/car_xyz_achievement_template.md) |
| **`resume-curator`** | Tailoring a resume or CV to a specific Job Description (JD). | Decomposes the JD, maps against `refs/` and `achievements/`, **pauses to verify critical gaps** before drafting, writes recency-weighted XYZ bullets to `career-kit/docs/tailored-resumes/<company-slug>_<role-slug>.md`, and outputs a Fit & Keyword Coverage table. | [`tailored_resume_template.md`](../../plugins/career-kit/skills/resume-curator/templates/tailored_resume_template.md) |
| **`interview-prep`** | Preparing for an interview loop or specific interview round. | Stage-aware 2-phase workflow: always writes `company_profile.md` and `car_story_matrix.md` first, then generates only the requested round sheet(s) (`recruiter_screen`, `hiring_manager`, `technical_interview`, `system_design`, `team_member`, `leadership_values`, `interview_cheat_sheet`). | [`templates/`](../../plugins/career-kit/skills/interview-prep/templates) |
