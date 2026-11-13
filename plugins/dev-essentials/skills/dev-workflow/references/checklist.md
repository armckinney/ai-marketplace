# Pre-Commit Verification Checklist

- [ ] Material ambiguities were clarified before implementation
- [ ] Validation or tests were defined prior to (or alongside) implementation and verified *after* the final edit
- [ ] No tests, assertions, or lint rules were disabled or weakened to force a pass
- [ ] Diff contains only task-related changes (`git diff --stat`)
- [ ] No secrets, tokens, or local environment files are staged (`git status`)
- [ ] Docstrings, comments, and `README.md` links match changed behavior without leaving stale notes
