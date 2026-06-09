# 📘 Assignment: Secure, Persistent REST APIs with FastAPI

## 🎯 Objective

Build a production-style REST API using FastAPI with SQLite persistence, token-based authentication, input validation with Pydantic, pagination/filtering, and containerized deployment using Docker.

## 📝 Tasks

### 🛠️ Design and implement the API core

#### Description
Create CRUD endpoints for a core resource `Item` and persist data in a SQLite database using SQLModel or SQLAlchemy (or the Python `sqlite3` module). Use Pydantic models for request/response validation.

#### Requirements
Completed program should:

- Provide endpoints to create, read (single + list), update, and delete `Item` resources.
- Store items in a SQLite database so data persists across server restarts.
- Use Pydantic models for request validation and response models.
- Return appropriate HTTP status codes for success and error cases.


### 🛠️ Add filtering, pagination, and authentication

#### Description
Extend the list endpoint to support query filtering and pagination. Add a simple token-based authentication requirement for admin endpoints.

#### Requirements
Completed program should:

- Support query parameters for searching by name and paginating results (`skip` and `limit`).
- Include at least one protected endpoint that requires an `X-Token` header.
- Validate tokens and return `401` for unauthorized access.


### 🛠️ Containerize and test

#### Description
Provide a `Dockerfile` to run the app in a container. Write integration tests using `TestClient`/`pytest` to verify create/read flows and auth behavior.

#### Requirements
Completed program should:

- Include a working `Dockerfile` that starts the FastAPI app with Uvicorn.
- Include at least 3 tests covering create, read, and unauthorized access.
- Provide `requirements.txt` and instructions to run the app, tests, and Docker image.
