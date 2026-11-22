---
name: resume-curator
description: >-
  Analyzes a target Job Description (JD) alongside a candidate's career profile,
  master resume, LinkedIn export, role interests, and distilled CAR/XYZ
  achievement bank to curate a tailored, high-impact resume. Pauses to verify
  critical JD gaps before drafting and outputs a Fit & Keyword Coverage
  summary. Use when tailoring, rewriting, or optimizing a resume or CV for a
  specific role.
---

# Resume Curator

Tailor a candidate's resume to a specific target Job Description (JD) using verified evidence from their career context. Calibrate framing dynamically to the role level and engineering archetype without inventing or inflating experience.

## Procedure

1. **Context Verification & Intake**:
   - Require the **Target Company Name** and **Target Job Description** (pasted text or non-login-gated URL).
   - Read all available baseline and distilled context:
     - `career-kit/docs/refs/career_profile.md` (if missing, pre-draft from `master_resume.md`, `role-interests.csv`, and `base-interview-questions.md` when present, then pause to confirm gaps using [career_profile_template.md](../achievement-distiller/templates/career_profile_template.md))
     - `career-kit/docs/refs/master_resume.md`
     - `career-kit/docs/refs/linkedin_profile.md` (if the user supplies a LinkedIn URL instead, remind them not to scrape LinkedIn and ask them to paste/export it here)
     - `career-kit/docs/refs/role-interests.csv` (if present — calibrate role-archetype, seniority, and domain priorities)
     - `career-kit/docs/refs/achievements_*.md` and `career-kit/docs/refs/achievement_stories.csv` (also check legacy spelling `archievement_stories.csv`) as auxiliary evidence sources
     - All distilled files under `career-kit/docs/achievements/*.md`
   - Keep all files in `career-kit/docs/refs/` except `career_profile.md` **strictly read-only**.

2. **JD Decomposition & Seniority Calibration**:
   - Analyze the target JD (cross-checking against `career_profile.md` and `refs/role-interests.csv`) and categorize requirements into:
     1. **Must-Have Technical Stack**: Primary languages, frameworks, infrastructure/cloud tooling, datastores, and operational practices.
     2. **System & Domain Challenges**: Core problems the team is hiring to solve (e.g., latency/throughput scaling, reliability/observability, product velocity, data/ML pipelines, security, migration).
     3. **Seniority & Archetype Signals**: Expected scope (hands-on builder, Tech Lead, cross-team Architect, Organizational Solver, or Engineering Manager) and leadership expectations (mentorship, RFC governance, stakeholder alignment).

3. **Evidence Mapping & Interactive Gap Gate**:
   - Map each decomposed JD requirement to specific verified experience, metrics, and **Leadership Principles / Technologies / Domains** tags across `refs/` and `achievements/`.
   - **Mandatory Pause on Critical Gaps**: If one or more high-priority JD requirements (core technology, architectural pattern, domain problem, or leadership scope) have no clear match or appear understated in existing files, **stop and ask the user** whether they have real, unrecorded experience covering those areas before drafting the resume.
   - If the user supplies newly surfaced details or metrics during this gap check, offer to persist them as a tagged CAR + XYZ entry in `career-kit/docs/achievements/<company-slug>.md`. **Never fabricate, extrapolate, or exaggerate unverified skills.**

4. **Prescriptive Curation & XYZ Drafting**:
   - **Professional Summary**: Write a dense, 3–4 sentence summary linking the candidate's proven scope and top quantified outcomes directly to the target company's domain challenges.
   - **Core Competencies**: Group skills logically (e.g., Languages, Frameworks & Runtime, Infrastructure & Cloud, Data & Messaging) and order technologies inside each category so the JD's top priorities appear first. Include only verified skills.
   - **Recency-Weighted Experience Bullets**:
     - Current / most recent relevant role: **3–5** XYZ bullets.
     - Mid-career relevant roles: **2–4** XYZ bullets.
     - Foundational / earlier roles: **1–2** concise XYZ bullets highlighting transferable engineering rigor or automation.
   - **Quality Checklist (Verify Before Writing)**:
     - Every bullet strictly follows the XYZ formula: *Accomplished [X] as measured by [Y], by doing [Z]*.
     - Every bullet opens with a distinct, active impact verb (zero duplicate opening verbs within the same role).
     - Metrics match source documents verbatim (never rounded up or inflated).
     - Single quotes (`'`) are used instead of double quotes (`"`) inside bullets if quoting is needed.
     - JD keywords are integrated naturally inside real technical explanations—never stuffed as ungrounded buzzword lists.

5. **Deliverable Generation & Fit Coverage Summary**:
   - Save the tailored resume to `career-kit/docs/tailored-resumes/<company-slug>_<role-slug>.md` using [tailored_resume_template.md](templates/tailored_resume_template.md).
   - Output a concise **JD Fit & Keyword Coverage Table** in chat mapping each core JD requirement to the exact tailored resume section/bullet supporting it, plus any remaining acknowledged gaps.
