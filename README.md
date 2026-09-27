# python_airtribe_learning

A comprehensive learning repository covering **Python Fundamentals**, **Data Structures**, **Object-Oriented Programming (OOP)**, **HTTP/REST API Concepts**, and **Django REST Framework (DRF) Web Services**, built as part of the [Airtribe](https://airtribe.live) curriculum.

---

## Table of Contents

- [Repository Overview](#repository-overview)
- [Project Structure](#project-structure)
- [Django Applications](#django-applications)
  - [1. Task Project (`task-project/`) — Full REST API](#1-task-project-task-project--full-rest-api)
    - [Architecture & Design Highlights](#architecture--design-highlights)
    - [Core Capabilities & Specialties](#core-capabilities--specialties)
    - [Functions & Utilities Reference](#functions--utilities-reference)
    - [API Endpoints Reference](#api-endpoints-reference)
    - [Sample Payloads & Usage](#sample-payloads--usage)
    - [Running the Task Project](#running-the-task-project)
  - [2. First Django Project (`first-django-project/`)](#2-first-django-project-first-django-project)
    - [Features & Endpoints](#features--endpoints)
- [Python Fundamentals & OOP Modules](#python-fundamentals--oop-modules)
- [Documentation & Study Notes](#documentation--study-notes)
- [Prerequisites & Setup](#prerequisites--setup)
- [License](#license)

---

## Repository Overview

This repository documents the transition from core Python programming concepts to architecting backend services with Django and Django REST Framework. It includes:

1. **Python Core & Data Structures**: Scripts covering control flow, primitive and non-primitive structures (lists, stacks, queues, linked lists, sets, dicts, tuples), and robust error handling.
2. **Object-Oriented Programming (OOP)**: Real-world implementations demonstrating the four pillars of OOP (Inheritance, Polymorphism, Abstraction, Encapsulation).
3. **HTTP & REST Fundamentals**: Detailed notes and references on HTTP methods, status codes, and request payloads.
4. **Django REST Services**: Hands-on Django projects with **PostgreSQL**, **Django ORM models**, **DRF serializers**, JSON-backed task storage (transitional), Docker Compose for local databases, and RESTful routing.

---

## Project Structure

```
python_airtribe_learning/
├── README.md                      # Comprehensive project documentation
├── RequestTypes.md                # HTTP methods (GET, POST, PUT, PATCH, DELETE) & request anatomy
├── StatusCode.md                  # Detailed HTTP status code reference guide
├── demo.py                        # Python basics: variables, conditionals, loops, functions
├── non_primitive.py               # Data structures: arrays, linked lists, stacks, queues
├── python_ds.py                   # Python collections: tuples, sets, dictionaries
├── exception_handling.py          # try/except, custom exceptions, error handling
├── amar.py                        # Practice scripts
├── test.py                        # Scratch test scripts
│
├── module01/                      # Object-Oriented Programming (OOP)
│   ├── oop.py                     # Classes, constructors, and objects
│   ├── inheritance.py             # Single and multi-level inheritance
│   ├── polymorphism.py            # Method overriding and duck typing
│   ├── abstraction.py             # Abstract Base Classes (ABC) and interfaces
│   └── encapsulation.py           # Private/protected members and getter/setter access
│
├── first-django-project/          # Introductory DRF API Project
│   ├── manage.py                  # Django CLI runner
│   ├── Django-Setup.md            # Complete setup guide (venv, django-admin, cross-platform)
│   ├── config/                    # Project settings and root URL routing
│   └── api/                       # API application
│       ├── urls.py                # App routing (/hello, /addTwoNumbers)
│       └── views.py               # Query parameter handling, math operations, status codes
│
└── task-project/                  # Task & User Management REST Service
    ├── manage.py                  # Django CLI runner
    ├── docker-compose.yml         # Local PostgreSQL (taskdb) for development
    ├── postgres_backup.sql        # SQL dump / backup reference
    ├── model.md                   # Notes on models vs entities (Django)
    ├── config/                    # Project settings & root routing
    │   ├── settings.py            # PostgreSQL config, rest_framework, tasks app
    │   └── urls.py                # Main URLconf delegating to tasks.urls
    └── tasks/                     # Core business application
        ├── models.py              # User Django model (PostgreSQL)
        ├── serializers.py         # UserSerializer, LoginSerializer
        ├── migrations/            # Django schema migrations (User table)
        ├── urls.py                # RESTful endpoint routes (/api/users/, /api/tasks/)
        ├── views.py               # User ORM + task JSON controllers
        ├── services/              # Persistence helpers
        │   └── json_util.py       # JSON file I/O for tasks (and legacy user checks)
        └── data/                  # JSON document storage
            ├── users.json         # Legacy/sample users (still used for task user_id checks)
            └── tasks.json         # Task records
```

---

## Django Applications

### 1. Task Project (`task-project/`) — Full REST API

The **Task Project** is a RESTful backend for **Users** and **Tasks**, built with **Django 6.1** and **Django REST Framework (DRF)**. User APIs persist to **PostgreSQL** via the Django ORM; task APIs still use **JSON files** while the schema is being migrated—see [model.md](task-project/model.md) for how models/entities fit together.

#### Architecture & Design Highlights

- **Hybrid persistence (learning migration)**:
  - **Users**: `User` model in PostgreSQL (`tasks/models.py`), exposed through `UserSerializer` and `LoginSerializer`.
  - **Tasks**: Stored in `tasks/data/tasks.json` via `read_json` / `write_json` in `tasks/services/json_util.py`.
  - Task endpoints validate `user_id` with `_user_exists()`, which currently reads **`users.json`**, not the database. After creating users through `POST /api/users/create/`, sync IDs in `users.json` or migrate task validation to the ORM so task creation matches DB users.
- **PostgreSQL via Docker Compose**:
  - `docker-compose.yml` runs Postgres (`taskdb`, user/password `postgres`) on port `5432`, matching `config/settings.py`.
- **DRF serializers**:
  - `UserSerializer` (`ModelSerializer`) validates and shapes create/list/detail responses.
  - `LoginSerializer` validates username-only login payloads.
- **REST controllers**:
  - Function-based views with `@api_view` in `tasks/views.py`; commented blocks preserve the earlier JSON-only implementation for comparison.
- **Tasks JSON layer**:
  - Auto-increment IDs, UTC timestamps (`_utc_now()`), and CRUD still mirror the original file-based design.

---

#### Core Capabilities & Specialties

| Capability | Implementation Detail | Specialty / Benefit |
|------------|-----------------------|---------------------|
| **User CRUD (database)** | `User.objects` + `UserSerializer` | PostgreSQL-backed users with unique `username` and `email`. |
| **Username login** | `POST /api/users/login/` + `LoginSerializer` | Validates input and returns user JSON or `404` for unknown username. |
| **Full CRUD for Tasks (JSON)** | `GET`, `POST`, `PUT`, `DELETE` on `/api/tasks/` | Task lifecycle in `tasks.json` with list/detail/create/update/delete routes. |
| **Relational filtering** | `GET /api/users/<user_id>/tasks/` | Filters tasks by `user_id` in JSON storage. |
| **Schema migrations** | `tasks/migrations/` | Django migrations create the `User` table (`0001_initial`, follow-ups). |
| **Local database** | `docker-compose.yml` | One-command Postgres for development. |
| **Task timestamps** | `_utc_now()` | ISO-8601 UTC on task create/update. |
| **Explicit HTTP statuses** | DRF `status.HTTP_*` | Semantic `200`, `201`, `400`, `404` responses. |

---

#### Functions & Utilities Reference

##### Application Controllers (`tasks/views.py`)

- **`users(request: Request) -> Response`**
  - **Method**: `GET`
  - **Description**: `User.objects.all()`, serialized with `UserSerializer(many=True)`, returns `200 OK`.
- **`user_detail(request: Request, user_id: int) -> Response`**
  - **Method**: `GET`
  - **Description**: `User.objects.get(id=user_id)` or `404 NOT FOUND` if missing; response via `UserSerializer`.
- **`login(request: Request) -> Response`**
  - **Method**: `POST`
  - **Description**: Validates body with `LoginSerializer`, looks up `User` by `username`, returns user JSON or `404 NOT FOUND`.
- **`user_tasks(request: Request, user_id: int) -> Response`**
  - **Method**: `GET`
  - **Description**: Verifies user via `_user_exists()` (JSON). Filters `tasks.json` by `user_id`; returns `404` if user not found in JSON.
- **`create_user(request) -> Response`**
  - **Method**: `POST`
  - **Description**: Validates with `UserSerializer`, creates row via `User.objects.create(...)`, returns `201 CREATED` or serializer/DB errors as `400 BAD REQUEST`.
- **`tasks(request: Request) -> Response`**
  - **Method**: `GET`
  - **Description**: Reads `tasks.json` and returns the list of all tasks with status `200 OK`.
- **`task_detail(request: Request, task_id: int) -> Response`**
  - **Method**: `GET`
  - **Description**: Searches for task matching `task_id`. Returns the task object or `404 NOT FOUND`.
- **`create_task(request) -> Response`**
  - **Method**: `POST`
  - **Description**:
    1. Extracts `user_id`, `title`, `description`, `iscompleted`, and `due_date`.
    2. Validates that `user_id` and `title` are provided (`400 BAD_REQUEST` on failure).
    3. Validates that `user_id` exists in `users.json` (`400 BAD_REQUEST` on failure).
    4. Generates an auto-incremented `id` and applies UTC timestamps (`created_at`, `updated_at`).
    5. Appends the task, writes back to `tasks.json`, and returns `201 CREATED`.
- **`update_task(request, task_id: int) -> Response`**
  - **Method**: `PUT`
  - **Description**:
    1. Locates the task by `task_id` (`404 NOT FOUND` if absent).
    2. Validates mandatory fields (`user_id`, `title`) and checks that `user_id` exists.
    3. Updates task attributes and refreshes `updated_at` with `_utc_now()`.
    4. Persists the updated list to `tasks.json` and returns the modified task.
- **`delete_task(request, task_id: int) -> Response`**
  - **Method**: `DELETE`
  - **Description**: Finds the task by `task_id` (`404 NOT FOUND` if absent), removes it from the list, writes back to `tasks.json`, and returns `200 OK` with a confirmation message.
- **`_utc_now() -> str`** *(Internal Helper)*
  - **Description**: Returns the current UTC time as an ISO-8601 formatted string (`YYYY-MM-DDTHH:MM:SSZ`).
- **`_user_exists(user_id: int) -> bool`** *(Internal Helper)*
  - **Description**: Reads `users.json` (not PostgreSQL) and checks if any record has `id == user_id`. Used by task routes during the JSON → ORM transition.

##### Serializers (`tasks/serializers.py`)

- **`UserSerializer`**: `ModelSerializer` for `User` — fields `id`, `username`, `email`, `password` (read/write on create).
- **`LoginSerializer`**: Accepts `username` for login validation.

##### Models (`tasks/models.py`)

- **`User`**: `username` (unique), `email` (unique), `password` — mapped to PostgreSQL via migrations.

##### JSON persistence (`tasks/services/json_util.py`)

- **`read_json(file_name: str) -> list`**
  - Uses `Path` resolution to target `tasks/data/<file_name>`.
  - Uses a `with open(..., "r")` context manager to read and deserialize JSON data safely without file descriptor leaks.
- **`write_json(file_name: str, data: list)`**
  - Opens target path with `with open(..., "w")`.
  - Serializes `data` with `json.dump(data, file, indent=2)` for structured, legible storage.

---

#### API Endpoints Reference

| Category | HTTP Method | Endpoint | Description | Status Codes |
|----------|-------------|----------|-------------|--------------|
| **Users** | `GET` | `/api/users/` | List all registered users | `200 OK` |
| **Users** | `GET` | `/api/users/<user_id>/` | Retrieve user details by ID | `200 OK`, `404 Not Found` |
| **Users** | `GET` | `/api/users/<user_id>/tasks/` | List all tasks assigned to a specific user | `200 OK`, `404 Not Found` |
| **Users** | `POST` | `/api/users/create/` | Register a new user (PostgreSQL) | `201 Created`, `400 Bad Request` |
| **Users** | `POST` | `/api/users/login/` | Login by username (returns user JSON) | `200 OK`, `400 Bad Request`, `404 Not Found` |
| **Tasks** | `GET` | `/api/tasks/` | List all tasks | `200 OK` |
| **Tasks** | `GET` | `/api/tasks/<task_id>/` | Retrieve task details by ID | `200 OK`, `404 Not Found` |
| **Tasks** | `POST` | `/api/tasks/create/` | Create a new task | `201 Created`, `400 Bad Request` |
| **Tasks** | `PUT` | `/api/tasks/<task_id>/update/` | Update an existing task | `200 OK`, `400 Bad Request`, `404 Not Found` |
| **Tasks** | `DELETE` | `/api/tasks/<task_id>/delete/` | Delete a task by ID | `200 OK`, `404 Not Found` |

---

#### Sample Payloads & Usage

##### 1. Create User (`POST /api/users/create/`)
**Request Body:**
```json
{
  "username": "john_doe",
  "email": "john@example.com",
  "password": "securepassword123"
}
```
**Response (`201 Created`):**
```json
{
  "id": 5,
  "username": "john_doe",
  "email": "john@example.com",
  "password": "securepassword123"
}
```

##### 2. Login (`POST /api/users/login/`)
**Request Body:**
```json
{
  "username": "john_doe"
}
```
**Response (`200 OK`):** Same shape as a single user object from `UserSerializer`.

##### 3. Create Task (`POST /api/tasks/create/`)
**Note:** `user_id` must exist in `tasks/data/users.json` for validation until task flows use the ORM.

**Request Body:**
```json
{
  "user_id": 1,
  "title": "Build Django README",
  "description": "Document all endpoints, functions, and architecture.",
  "iscompleted": false,
  "due_date": "2026-09-10T18:00:00Z"
}
```
**Response (`201 Created`):**
```json
{
  "id": 3,
  "user_id": 1,
  "title": "Build Django README",
  "description": "Document all endpoints, functions, and architecture.",
  "iscompleted": false,
  "created_at": "2026-09-06T17:15:30Z",
  "updated_at": "2026-09-06T17:15:30Z",
  "due_date": "2026-09-10T18:00:00Z"
}
```

##### 4. Update Task (`PUT /api/tasks/3/update/`)
**Request Body:**
```json
{
  "user_id": 1,
  "title": "Build Django README",
  "description": "Document all endpoints, functions, and architecture.",
  "iscompleted": true,
  "due_date": "2026-09-10T18:00:00Z"
}
```
**Response (`200 OK`):**
```json
{
  "id": 3,
  "user_id": 1,
  "title": "Build Django README",
  "description": "Document all endpoints, functions, and architecture.",
  "iscompleted": true,
  "created_at": "2026-09-06T17:15:30Z",
  "updated_at": "2026-09-06T17:20:10Z",
  "due_date": "2026-09-10T18:00:00Z"
}
```

---

#### Running the Task Project

1. Navigate to the `task-project` directory:
   ```bash
   cd task-project
   ```

2. Start PostgreSQL (Docker):
   ```bash
   docker compose up -d
   ```
   Database: `taskdb` on `localhost:5432` (user/password `postgres`), as configured in `config/settings.py`.

3. Activate the virtual environment and install dependencies (Django, DRF, PostgreSQL driver, for example `psycopg2-binary`):
   - **macOS / Linux:** `source .venv/bin/activate`
   - **Windows:** `.venv\Scripts\activate`

4. Apply migrations (Django system tables + `tasks.User`):
   ```bash
   python manage.py migrate
   ```

5. Start the development server:
   ```bash
   python manage.py runserver
   ```
   Base API URL: `http://127.0.0.1:8000/api/`

6. Example requests:
   ```bash
   curl -X GET http://127.0.0.1:8000/api/users/
   curl -X GET http://127.0.0.1:8000/api/tasks/
   curl -X POST http://127.0.0.1:8000/api/users/login/ -H "Content-Type: application/json" -d "{\"username\":\"Amar S\"}"
   ```

---

### 2. First Django Project (`first-django-project/`)

The foundational Django project used to master environment creation, project bootstrapping, and query-parameter handling with DRF.

#### Features & Endpoints

- **`hello` (`GET /api/hello/`)**:
  - Simple health/welcome check returning JSON: `{"message": "Hello from Airtribe"}`.
- **`add_two_numbers` (`GET /api/addTwoNumbers/?a=10&b=20`)**:
  - Demonstrates parsing query parameters from `request.query_params`.
  - Implements defensive type-casting with `try/except (TypeError, ValueError)`.
  - Returns `{"sum": 30}` with `200 OK` on valid input, or `{"error": "Both 'a' and 'b' must be valid numbers."}` with `400 BAD REQUEST` on invalid input.
- **Documentation**:
  - Includes [`Django-Setup.md`](first-django-project/Django-Setup.md) covering full virtual environment setup, package installations (`django`, `djangorestframework`), and CLI commands across macOS, Linux, and Windows.

---

## Python Fundamentals & OOP Modules

In addition to Django, this repository provides deep coverage of core Python concepts:

| Module / File | Core Concepts Covered | Key Functions / Classes |
|---------------|-----------------------|-------------------------|
| [`demo.py`](demo.py) | Variables, conditionals, loops, functions, lists, slicing | Basic algorithmic scripts and control flow |
| [`python_ds.py`](python_ds.py) | Python collections: tuples, sets, dictionaries | Immutable tuples, set unions/intersections, dict lookups |
| [`non_primitive.py`](non_primitive.py) | Custom data structures | `Node`, `LinkedList`, `Stack`, `Queue`, `insert_at_beginning`, `delete_node` |
| [`exception_handling.py`](exception_handling.py) | Error handling, custom exceptions, ternary operator | `InvalidAgeException`, `check_voting_eligibility`, `try/except/else/finally` |
| [`module01/oop.py`](module01/oop.py) | Classes and Objects | Constructor `__init__`, instance methods, self reference |
| [`module01/inheritance.py`](module01/inheritance.py) | Inheritance | `super()`, method overriding, base and derived classes |
| [`module01/polymorphism.py`](module01/polymorphism.py) | Polymorphism | Method overriding across sub-classes, duck typing |
| [`module01/abstraction.py`](module01/abstraction.py) | Abstraction | `abc.ABC`, `@abstractmethod`, enforcing contract interfaces |
| [`module01/encapsulation.py`](module01/encapsulation.py) | Encapsulation | Private variables (`__variable`), getters and setters |

---

## Documentation & Study Notes

- **[RequestTypes.md](RequestTypes.md)**: Deep dive into HTTP methods (`GET`, `POST`, `PUT`, `PATCH`, `DELETE`), comparison of full updates (`PUT`) vs partial updates (`PATCH`), and anatomy of requests (Body, Query params, Path params, Headers).
- **[StatusCode.md](StatusCode.md)**: Comprehensive guide detailing standard HTTP response codes (`2xx Success`, `3xx Redirection`, `4xx Client Errors`, `5xx Server Errors`) with real-world scenarios.
- **[Django-Setup.md](first-django-project/Django-Setup.md)**: Step-by-step setup guide for creating virtual environments, installing dependencies, configuring Django settings, and running development servers across different operating systems.
- **[model.md](task-project/model.md)**: Short notes on **models** vs **entities**, and how Django models map to database schema.

---

## Prerequisites & Setup

### Prerequisites
- **Python 3.8+** (Python 3.10+ recommended; Task Project targets **Django 6.1**)
- **pip** (Python package installer)
- **Docker Desktop** (or local PostgreSQL) for `task-project` database
- Python packages for Task Project: `django`, `djangorestframework`, and a PostgreSQL adapter (for example `psycopg2-binary`)

### Quick Start

1. Clone the repository:
   ```bash
   git clone https://github.com/amar-s-08/python_airtribe_learning.git
   cd python_airtribe_learning
   ```

2. Run standalone Python scripts:
   ```bash
   python demo.py
   python exception_handling.py
   python module01/oop.py
   ```

3. Run the Django Task Project:
   ```bash
   cd task-project
   docker compose up -d
   source .venv/bin/activate   # On Windows: .venv\Scripts\activate
   python manage.py migrate
   python manage.py runserver
   ```

---

## License

This repository is created for personal learning and demonstration purposes under the Airtribe curriculum.
