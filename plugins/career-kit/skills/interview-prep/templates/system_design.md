# System Design Prep: [Company Name] — [Role Title]

## 1. Time-Boxed 45-Minute Architecture Checklist

### Phase 1: Scope & Requirements (5 mins)
- [ ] **Functional Requirements**: Core user/system actions, inputs/outputs, and real-time vs. async workflows.
- [ ] **Non-Functional Requirements**:
  - [ ] Scale (DAU/MAU, read/write QPS, peak burst factor, payload sizes).
  - [ ] Consistency vs. Availability tradeoffs (strong vs. eventual consistency).
  - [ ] Latency targets (P50 / P99) and durability/retention guarantees.
- [ ] **Explicit Out of Scope**: Confirm what you are deferring so time stays focused.

### Phase 2: Back-of-the-Envelope Estimates (3–5 mins)
- [ ] Read/write QPS (average vs. peak 3–5x).
- [ ] Storage growth (daily/yearly bytes including indexes/replication).
- [ ] Cache working set (80/20 rule) and network bandwidth constraints.

### Phase 3: Interfaces & Data Model (7–10 mins)
- [ ] **API / Event Contracts**: Core REST/gRPC endpoints or event schemas, idempotency keys, pagination, and auth boundaries.
- [ ] **Storage & Schema Selection**: Relational vs. NoSQL vs. Object/Blob vs. Search/Vector vs. Cache—justify choices via access patterns, indexing, and partitioning keys.

### Phase 4: High-Level Architecture (10 mins)
- [ ] End-to-end request/data flow (Client -> CDN/Edge -> Load Balancer/API Gateway -> Services -> Cache -> Primary Store -> Async Queues/Workers).
- [ ] Separation of synchronous hot paths from asynchronous background pipelines.

### Phase 5: Deep Dives, Bottlenecks & Resiliency (15 mins)
- [ ] **Scaling & Hotspots**: Sharding/partitioning strategy, hot-key mitigation, read replicas, cache invalidation.
- [ ] **Failure Modes & Resiliency**: Single points of failure, rate limiting, backpressure, retries with jitter, dead-letter queues, circuit breakers, multi-AZ/multi-region failover.
- [ ] **Observability & Operations**: SLIs/SLOs, structured logging, distributed tracing, rollout/rollback safety.

---

## 2. Domain-Tailored Prompts & Architectural CAR Stories
*(Tailor this section dynamically to the target company's architecture from `company_profile.md` and candidate stories from `car_story_matrix.md`.)*

- **Likely System Design Scenarios for [Company Name]**:
  - [Scenario 1 grounded in the company's product/JD]
  - [Scenario 2 grounded in the company's scale or data challenges]
- **Relevant Candidate Architecture Stories to Reference**:
  - **[Story Title from `car_story_matrix.md`]**: [1-line tradeoff or scaling lesson you can cite naturally]
