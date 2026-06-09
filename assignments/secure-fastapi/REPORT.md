# Report

Describe what you implemented, how to run it, and any trade-offs.

- Persistence: SQLite database at `data.db` for simplicity.
- Auth: Simple header `X-Token: secrettoken` for protected endpoint.
- Tests: `pytest` tests in `tests/`.
- Docker: build with `docker build -t secure-fastapi .` and run.
