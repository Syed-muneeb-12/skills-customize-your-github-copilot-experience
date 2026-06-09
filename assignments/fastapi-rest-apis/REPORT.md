# Report

Describe what you implemented, any deviations from the spec, and trade-offs.

- Implemented CRUD endpoints for `Item` with Pydantic models.
- In-memory storage used for simplicity; recommend adding a database for persistence.
- Simple token header auth added for `/admin/secure-action`.
- Tests provided in `tests/test_api.py`.
