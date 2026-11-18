# Distilled Achievement Entry Template & Examples

Use this structure when saving distilled achievements to `career-kit/docs/achievements/<company-slug>.md`. Each entry pairs a natural **CAR story** (tagged with **Leadership Principles**, **Technologies**, and **Domains** for filtering and navigation) with **2–3 XYZ resume bullet variants**.

---

## Entry Template

```markdown
## [Initiative / Project Short Title]
- **Role**: [Role Title]
- **Timeframe**: [YYYY-MM - YYYY-MM or Quarter]
- **Leadership Principles**: [Confirm with user: e.g., Customer Focus, Dive Deep, Ownership, Results Oriented]
- **Technologies**: [Prompt user—never guess: e.g., Python, PostgreSQL, Redis, Terraform]
- **Domains**: [Confirm with user from 18-tag taxonomy: e.g., `APIs & Services`, `Storage & Databases`, `Observability & Reliability`]

### CAR Story
- **Challenge / Context**: [1–2 sentences describing the problem, baseline metrics, scale, and constraints.]
- **Action**: [2–3 sentences or concise bullets detailing the technical decisions, architecture, and leadership/collaboration actions you drove.]
- **Result**: [1–2 sentences stating the measurable outcome and lasting impact.]

### XYZ Resume Bullet Variants
- **Variant A ([Lens 1, e.g., Scale & Performance])**: Accomplished [X] as measured by [Y], by doing [Z].
- **Variant B ([Lens 2, e.g., Leadership & Cross-Team Impact])**: Accomplished [X] as measured by [Y], by doing [Z].
- **Variant C ([Lens 3, e.g., Reliability / Developer Velocity])**: Accomplished [X] as measured by [Y], by doing [Z].
```

---

## Tagging Reference Guide

1. **Leadership Principles** *(propose from this list or `career_profile.md` and confirm with the user)*:
   - **Customer Focus**: Solving user/developer pain points, improving adoption, UX, or SLAs.
   - **Continuous Improvement**: Eliminating toil, automating manual steps, refining postmortems/CI.
   - **Data Driven**: Profiling, telemetry, benchmarks, A/B metrics, or cost analysis guiding decisions.
   - **Action Oriented**: Moving fast with pragmatic prototypes, unblocking stalled initiatives.
   - **Dive Deep**: Root-causing subtle bugs, inspecting low-level bottlenecks, auditing architecture.
   - **Innovative**: Designing novel abstractions, architectures, or creative solutions under constraints.
   - **Ownership**: Taking end-to-end accountability beyond immediate scope through production rollout.
   - **Results Oriented**: Driving measurable business, cost, reliability, or delivery velocity outcomes.
   - **Collaborative**: Aligning cross-functional stakeholders, mentoring peers, running RFCs/reviews.
   - **Adaptability**: Pivoting effectively under changing requirements, incidents, or scaling shifts.
   - **Prioritize Collective**: Putting team/org success, shared standards, or platform health above local wins.
   - *(Include additional principles if defined in `career_profile.md` or warranted by the story.)*

2. **Technologies** *(always prompt/confirm with the user—never infer unstated tools)*:
   - List exact languages, frameworks, cloud services, datastores, orchestrators, and CI/observability tools used directly in the initiative.

3. **Domains** *(propose 2–4 high-level filter tags from the 18-tag standard taxonomy below and confirm with the user; keep specific languages/tools like `SQL` or `PostgreSQL` in **Technologies**)*:
   - **Platform & Infrastructure**:
     - `Platform Engineering`: Internal developer platforms, shared abstractions, self-service tooling.
     - `Cloud & Compute`: Cloud accounts/subscriptions, VMs, clusters, compute provisioning.
     - `Containers & Serverless`: Docker, Kubernetes, serverless functions, container runtimes.
     - `Infrastructure as Code (IaC)`: Declarative provisioning, policy-as-code, environment automation.
     - `Networking`: Private links, VPC/hub-and-spoke topologies, DNS, ingress/egress routing.
     - `CI/CD & DevOps`: Build/deploy pipelines, release automation, artifact governance.
   - **Data & AI/ML**:
     - `Data Engineering & ELT`: Ingestion pipelines, batch/streaming transforms, data quality.
     - `Analytics & BI`: Metrics layers, reporting datasets, query performance, dashboards.
     - `ML & AI Systems`: Training/inference workflows, feature stores, LLM/agent infrastructure.
     - `Storage & Databases`: Relational/NoSQL data modeling, caching, lakehouse/object storage.
   - **Software & Architecture**:
     - `System Architecture`: End-to-end topology, service boundaries, distributed tradeoffs.
     - `APIs & Services`: Backend endpoints, gRPC/REST contracts, async job/event workers.
     - `SDKs & Frameworks`: Shared libraries, component kits, CLI/developer tooling frameworks.
   - **Security & Operations**:
     - `Security & IAM`: Zero-trust perimeters, RBAC/SCIM, secrets, compliance controls.
     - `Observability & Reliability`: Monitoring, tracing, alerting, SLOs, incident hardening.
   - **Impact & Experience**:
     - `Developer Experience (DevEx)`: Reclaimed engineering capacity, streamlined workflows, onboarding speed.
     - `Cost & Efficiency Optimization`: Compute/storage spend reductions, throughput or utilization gains.
     - `Product & UX Impact`: End-user conversion, UI quality, accessibility, customer-facing latency.

---

## Role-Agnostic Examples

### Example 1: Backend & Distributed Systems (Latency & Cost)
- **Raw Input**: Fixed slow checkout API queries that were timing out during traffic spikes and costing too much on our primary database.
- **Leadership Principles**: `Customer Focus`, `Data Driven`, `Dive Deep`, `Results Oriented`
- **Technologies**: `Python`, `FastAPI`, `PostgreSQL`, `Redis`, `Locust`
- **Domains**: `APIs & Services`, `Storage & Databases`, `Observability & Reliability`, `Cost & Efficiency Optimization`
- **CAR Story**:
  - **Challenge / Context**: During peak promotional events, the checkout pricing endpoint experienced P99 latency spikes above 2.5 seconds and caused primary relational database CPU saturation at 95%, triggering intermittent timeouts on ~4% of orders.
  - **Action**: Profiled the hot query paths, eliminated N+1 ORM joins with batched read queries, introduced a read-through Redis cache with versioned invalidation keys, and added circuit-breaker fallbacks so transient cache misses degraded gracefully. Coordinated rollout and load testing across the checkout and SRE teams using dark-launch traffic mirroring.
  - **Result**: Cut P99 endpoint latency from 2.5s to 180ms (93% reduction), eliminated peak-event database timeouts, and deferred a planned $120k/year database tier upgrade.
- **XYZ Resume Bullet Variants**:
  - **Scale & Performance**: Slashed checkout API P99 latency by 93% (2.5s to 180ms) and eliminated peak-traffic order timeouts by replacing N+1 relational queries with batched reads and a versioned Redis cache.
  - **Cost & Reliability**: Prevented a $120k/year database vertical scaling upgrade and stabilized peak-event availability at 99.99% by re-architecting pricing lookups with circuit-breaker fallbacks and dark-launch load validation.

### Example 2: Frontend / Full-Stack & Developer Velocity
- **Raw Input**: Rebuilt our fragmented form components and checkout validation logic so product teams could ship faster with fewer bugs.
- **Leadership Principles**: `Customer Focus`, `Collaborative`, `Continuous Improvement`, `Prioritize Collective`
- **Technologies**: `TypeScript`, `React`, `Zod`, `Playwright`, `Storybook`
- **Domains**: `SDKs & Frameworks`, `Developer Experience (DevEx)`, `Product & UX Impact`
- **CAR Story**:
  - **Challenge / Context**: Four product squads maintained duplicate form and validation logic across a React/TypeScript monorepo, causing inconsistent accessibility behavior, frequent regression bugs, and a 3-week average cycle time for launching new onboarding flows.
  - **Action**: Partnered with design systems and product engineers to design a schema-driven form SDK built on shared TypeScript validation contracts and accessible primitives, wrote migration codemods, and ran hands-on office hours to onboard all four squads without halting feature delivery.
  - **Result**: Reduced new onboarding flow delivery time from 3 weeks to 4 days, cut form-related UI bug reports by 60% over two quarters, and achieved 100% WCAG AA keyboard/screen-reader compliance across core signup paths.
- **XYZ Resume Bullet Variants**:
  - **Developer Velocity**: Accelerated new product onboarding delivery from 3 weeks to 4 days across four squads by architecting a schema-driven TypeScript form SDK with automated migration codemods.
  - **Quality & Cross-Team Alignment**: Reduced form-related UI regressions by 60% and achieved 100% WCAG AA accessibility compliance across core user flows by unifying four teams onto shared validation contracts and accessible UI primitives.
