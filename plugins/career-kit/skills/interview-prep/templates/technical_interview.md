# Technical & Coding Interview Prep: [Company Name] — [Role Title]

## 1. Tactical Execution Protocol (Clarify -> Design -> Implement -> Verify)
1. **Clarify Requirements & Constraints**: Confirm inputs, outputs, mutability, concurrency, scale bounds, and expected error behavior before writing code.
2. **Enumerate Edge Cases**: Empty/null inputs, single-element inputs, duplicates, boundary values, ordering ties, and invalid states.
3. **Outline Concrete Test Cases**: Walk through 1 happy path and 2 edge cases manually.
4. **Propose Approach & Tradeoffs**: State brute-force vs. optimal time/space complexity and confirm alignment with the interviewer before coding.
5. **Write Clean, Modular Code**: Use clear naming, explicit typing/interfaces, and helper functions; narrate intent concisely as you code.
6. **Dry-Run & Complexity Audit**: Trace through your test cases line-by-line, verify off-by-one boundaries, and confirm Big-O time and space complexity.
7. **Discuss Production Hardening**: Mention concurrency safety, memory limits, observability, or streaming/sharding extensions if asked.

---

## 2. Target Stack & Language Idioms Quick-Ref
*(Populate dynamically from the candidate's chosen interview language and the target JD's practical technical focus—e.g., Python/Go/TypeScript/Java collections, concurrency primitives, async patterns, SQL window functions, or frontend state/rendering patterns.)*

- **Primary Interview Language**: [Language from `career_profile.md` / JD]
- **Core Data Structures & Standard Library Idioms**:
  - [Idiom 1: e.g., Hash maps / grouping / frequency counters]
  - [Idiom 2: e.g., Heaps / priority queues / top-K]
  - [Idiom 3: e.g., Queues / BFS / sliding window / LRU eviction]
  - [Idiom 4: e.g., Concurrency / async coordination / rate limiting]
- **Practical Domain Focus (From JD)**:
  - [e.g., API endpoint design, SQL optimization, React state/accessibility, or debugging broken tests]

---

## 3. Questions for Technical Interviewers
- **Technical Governance**:
  - "How are architectural decisions made here—collaborative RFCs and consensus reviews, or designated technical drivers for each domain?"
- **Quality & Testing Standards**:
  - "What does your testing and CI pipeline emphasize (unit, contract, integration, load tests), and how do teams balance velocity with test confidence?"
- **Reliability & Constraints**:
  - "What are the hardest correctness, performance, or failure-mode constraints your services deal with in production today?"
