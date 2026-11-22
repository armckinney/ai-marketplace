---
name: achievement-distiller
description: >-
  Interviews software engineers on raw work logs, PRs, design docs, CSV story
  catalogs, or rough draft bullets to distill concise CAR stories
  (Challenge/Context, Action, Result) and quantified XYZ resume bullet
  variants. Also bootstraps career_profile.md when missing. Use when capturing
  brag-doc entries, refining resume bullets, or turning engineering work into
  interview stories.
---

# Achievement Distiller (CAR + XYZ)

Transform raw engineering initiatives and rough work notes into crisp, evidence-backed **CAR stories** (for interviews and career memory) paired with **XYZ resume bullet variants** (for tailored resumes). Adapt framing dynamically to the user's target seniority and role archetype defined in `career-kit/docs/refs/career_profile.md`.

## Procedure

1. **Context Discovery & Smart Profile Bootstrap**:
   - Inspect `career-kit/docs/refs/` (`career_profile.md`, `master_resume.md`, `linkedin_profile.md`, `role-interests.csv`, `base-interview-questions.md`, `achievements_*.md`, and `achievement_stories.csv` / legacy `archievement_stories.csv`) plus existing files in `career-kit/docs/achievements/`.
   - Treat all files in `career-kit/docs/refs/` except `career_profile.md` as **strictly read-only**.
   - If `career-kit/docs/refs/career_profile.md` does not exist, pre-populate draft fields from `master_resume.md`, `role-interests.csv` (values, domain interests, target levels), and `base-interview-questions.md` (career progression arc) when present, then pause to interview the user to confirm and fill remaining gaps before persisting it using [career_profile_template.md](templates/career_profile_template.md).

2. **Raw Initiative Intake (Manual or Reference Import)**:
   - Collect the user's raw input—either pasted notes (brag-doc entry, PR/design doc summary, incident postmortem, draft bullet) OR selected raw rows/entries from read-only `refs/achievement_stories.csv` (or `refs/archievement_stories.csv`, e.g., `Title,Domains,Story`) and `refs/achievements_*.md`—along with the associated **Company**, **Role Title**, and **Timeframe**.
   - Cross-reference the company against the growth arc in `career_profile.md` so the narrative emphasizes the appropriate progression stage.

3. **Structured Diagnostic Interview (Stop & Ask Gate)**:
   - Audit the raw input against the three CAR/XYZ pillars and three structured navigation tags before drafting:
     - **Challenge / Context**: What problem, bottleneck, reliability risk, or scale constraint existed before your work? What were the baseline numbers or stakes?
     - **Action**: What specific technical design, implementation, tooling, process change, mentorship, or cross-team alignment did *you* drive? (Separate "we" from "I".)
     - **Result**: What changed measurably afterward (e.g., P99 latency, error rate, infrastructure cost, deploy frequency, onboarding time, engineering hours saved, adoption count, revenue impact)?
     - **Technologies (Prompt, Never Guess)**: Ask the user for the exact languages, frameworks, cloud services, datastores, and tools leveraged if not already stated explicitly.
     - **Leadership Principles & Domains (Propose & Confirm)**: Infer candidate **Leadership Principles** (from the 11-principle taxonomy—`Customer Focus`, `Continuous Improvement`, `Data Driven`, `Action Oriented`, `Dive Deep`, `Innovative`, `Ownership`, `Results Oriented`, `Collaborative`, `Adaptability`, `Prioritize Collective`—plus any custom principles in `career_profile.md`) and **Domains** from the 18-tag standard taxonomy (`Platform Engineering`, `Cloud & Compute`, `Containers & Serverless`, `Infrastructure as Code (IaC)`, `Networking`, `CI/CD & DevOps`, `Data Engineering & ELT`, `Analytics & BI`, `ML & AI Systems`, `Storage & Databases`, `System Architecture`, `APIs & Services`, `SDKs & Frameworks`, `Security & IAM`, `Observability & Reliability`, `Developer Experience (DevEx)`, `Cost & Efficiency Optimization`, `Product & UX Impact`), then ask the user to confirm or adjust them. Keep specific tools or languages (e.g., `SQL`, `PostgreSQL`) strictly in **Technologies**, not **Domains**.
   - If any pillar or tag lacks concrete details or confirmation, **STOP and ask 2–4 targeted questions**. If exact telemetry is unavailable, help the user calculate a defensible engineering estimate (e.g., hours/week saved x team size) and mark it clearly as an estimate (`~`). **Never fabricate metrics or guess unstated technologies.**

4. **Dual-Output Distillation (CAR + XYZ)**:
   - Follow [car_xyz_achievement_template.md](templates/car_xyz_achievement_template.md) to generate both outputs for the initiative:
     1. **CAR Story (1 concise narrative + filter tags)**:
        - Include the confirmed **Leadership Principles**, **Technologies**, and **Domains** tags at the top of the entry so stories can be filtered cleanly for portfolios, resumes, and interviews.
        - **Challenge / Context**: 1–2 sentences setting the problem, scale, and constraints naturally.
        - **Action**: 2–3 sentences (or sub-bullets) highlighting the decisive technical choices, tradeoffs considered, and leadership/collaboration mechanics.
        - **Result**: 1–2 sentences anchoring the quantified outcome and durable organizational impact.
        - Keep the tone conversational and authentic—ready to speak aloud in an interview without sounding scripted.
     2. **XYZ Resume Bullet Variants (2–3 options)**:
        - Strictly follow: *Accomplished [X] as measured by [Y], by doing [Z]*.
        - Tune each variant to a distinct strategic lens or leadership principle from `career_profile.md` (for example: Variant A emphasizing **Technical Depth & Scale**, Variant B emphasizing **Collaboration / Leadership**, Variant C emphasizing **Efficiency / Developer Experience**).
        - Lead every bullet with a distinct, strong action verb; use single quotes (`'`) instead of double quotes (`"`) inside bullets if quoting is needed; omit confidential internal tool names unless the user approves including them.

5. **Review, Polish & Persistence**:
   - Present the CAR story and XYZ variants to the user, verify factual accuracy of every metric and claim, and iterate if requested.
   - Once approved, write or append the finalized entry to `career-kit/docs/achievements/<company-slug>.md` (preserving all existing achievements in that file).
