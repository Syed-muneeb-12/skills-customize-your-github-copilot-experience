# Building REST APIs with FastAPI

## Overview
In this assignment you'll design and implement a RESTful API using the FastAPI framework. You'll build endpoints, validate input with Pydantic models, document the API using automatic docs, and write basic tests.

## Learning Objectives
- Understand FastAPI request/response model and routing
- Use Pydantic for data validation and typing
- Implement CRUD endpoints and proper HTTP status codes
- Add query parameters, pagination, and error handling
- Use automated docs (Swagger UI / Redoc) and run the app with Uvicorn
- Write basic unit tests for API endpoints

## Requirements
- Python 3.10+ (or 3.9+)
- `pip` and virtual environment support

## Setup
1. Create and activate a virtual environment:

```bash
python3 -m venv venv
source venv/bin/activate
```

2. Install dependencies:

```bash
pip install -r requirements.txt
```

3. Run the app locally:

```bash
uvicorn starter-code:app --reload
```

Open `http://127.0.0.1:8000/docs` for the interactive Swagger UI.

## Tasks

1. Explore the provided starter app in `starter-code.py` and run it.
2. Extend the API with the following endpoints and features:
   - Create, Read (single + list), Update, Delete for a core resource (e.g., `Item`).
   - Input validation and response models using Pydantic.
   - Filtering and pagination for the list endpoint (query params).
   - Proper error handling with informative HTTP status codes.
3. Add at least one endpoint that accepts a complex payload (nested models or lists).
4. Add simple authentication for one endpoint (token-based using a header).
5. Write at least 3 unit tests covering create, read, and error case.

## Deliverables
- A working FastAPI project in this folder.
- A short `REPORT.md` or the top of this README describing what you implemented and any trade-offs.
- Tests and instructions to run them.

## Grading Rubric (suggested)
- Functionality (40%): Endpoints implemented and behaving correctly.
- Validation & Error handling (20%): Correct use of Pydantic and HTTP codes.
- Documentation (15%): README, interactive docs, and run instructions.
- Tests (15%): At least 3 unit tests demonstrating correctness.
- Bonus (10%): Auth, pagination, persistent storage, or CI integration.

## Hints & Resources
- FastAPI docs: https://fastapi.tiangolo.com/
- Pydantic docs: https://docs.pydantic.dev/
- Uvicorn: https://www.uvicorn.org/

Good luck — build something you can demo!
