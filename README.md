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
4. **Django REST Services**: Hands-on Django projects implementing production patterns including service-layer separation, custom JSON persistence, data validation, and RESTful routing.

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
    ├── config/                    # Project settings & root routing
    │   ├── settings.py            # Registered apps (rest_framework, tasks)
    │   └── urls.py                # Main URLconf delegating to tasks.urls
    └── tasks/                     # Core business application
        ├── urls.py                # RESTful endpoint routes (/api/users/, /api/tasks/)
        ├── views.py               # CRUD controllers, validation, and HTTP responses
        ├── services/              # Service & persistence layer
        │   └── json_util.py       # Safe JSON file I/O operations with context management
        └── data/                  # Persistent JSON storage
            ├── users.json         # User database records
            └── tasks.json         # Task database records
```

---

## Django Applications

### 1. Task Project (`task-project/`) — Full REST API

The **Task Project** is a fully functional, RESTful backend service for managing **Users** and their assigned **Tasks**. It is built with **Django** and **Django REST Framework (DRF)**, featuring a clean architectural separation between business controllers and file-based data persistence.

#### Architecture & Design Highlights

- **Service-Oriented Architecture (SOA)**:
  - Controller views (`tasks/views.py`) handle HTTP requests, validate input, and structure responses.
  - Data operations are delegated to a dedicated utility service (`tasks/services/json_util.py`), isolating persistence logic from API controllers.
- **Custom JSON Document Persistence**:
  - Instead of requiring an external database, data is stored in structured JSON documents (`users.json` and `tasks.json`).
  - Utilizes Python's `pathlib.Path` to compute file locations relative to `__file__`, ensuring path portability across macOS, Linux, and Windows.
- **Relational Integrity Simulation**:
  - Simulates foreign-key relationships between tasks and users (`user_id` on each task).
  - Enforces referential integrity: tasks cannot be created or reassigned to non-existent users (`_user_exists` check).
- **Safe Resource Management**:
  - Employs Python context managers (`with open(...)`) in `json_util.py` to prevent file handle leaks.
  - Indents JSON writes (`indent=2`) for human-readable auditability.
- **Strong Typing & Defensive Validation**:
  - Uses Python type hints (`request: Request -> Response`, `set[str]`, `user_id: int`).
  - Validates missing required fields, checks for duplicate usernames and emails using set operations, and returns precise error payloads.
- **Standardized UTC Timestamps**:
  - Records ISO-8601 timestamps (`%Y-%m-%dT%H:%M:%SZ`) using timezone-aware UTC dates (`_utc_now()`) for audit tracking (`created_at`, `updated_at`).

---

#### Core Capabilities & Specialties

| Capability | Implementation Detail | Specialty / Benefit |
|------------|-----------------------|---------------------|
| **Full CRUD for Tasks** | `GET`, `POST`, `PUT`, `DELETE` on `/api/tasks/` | Complete task lifecycle management with individual item endpoints. |
| **User Entity Management** | `GET`, `POST` on `/api/users/` | User creation with validation, uniqueness checks, and individual user queries. |
| **Relational Filtering** | `GET /api/users/<user_id>/tasks/` | Retrieves all tasks assigned to a specific user (foreign-key filtering). |
| **Duplicate Prevention** | `set[str]` comparison on `username` and `email` | Rejects duplicate usernames and emails with HTTP 400 Bad Request before writing. |
| **Foreign Key Enforcement** | `_user_exists(user_id)` helper | Prevents orphaned tasks by verifying user existence before task creation/update. |
| **Auto-Incrementing IDs** | Dynamic `max_id + 1` computation | Automatically generates consecutive primary keys for users and tasks. |
| **Automatic Timestamping** | `_utc_now()` using `datetime(timezone.utc)` | Sets `created_at` on insert and updates `updated_at` on modification. |
| **Explicit HTTP Statuses** | DRF `status.HTTP_*` constants | Returns semantic status codes (`200 OK`, `201 CREATED`, `400 BAD REQUEST`, `404 NOT FOUND`). |
| **Portable File Resolution** | `Path(__file__).resolve().parent.parent / "data"` | No hardcoded paths; works seamlessly across any developer's environment. |

---

#### Functions & Utilities Reference

##### Application Controllers (`tasks/views.py`)

- **`users(request: Request) -> Response`**
  - **Method**: `GET`
  - **Description**: Reads `users.json` via `read_json()` and returns all user records with status `200 OK`.
- **`user_detail(request: Request, user_id: int) -> Response`**
  - **Method**: `GET`
  - **Description**: Iterates through users to find a matching `id`. Returns the user object, or a `404 NOT FOUND` error if the user does not exist.
- **`user_tasks(request: Request, user_id: int) -> Response`**
  - **Method**: `GET`
  - **Description**: Verifies user existence via `_user_exists()`. If valid, filters `tasks.json` by `user_id` and returns the matching task list; otherwise returns `404 NOT FOUND`.
- **`create_user(request) -> Response`**
  - **Method**: `POST`
  - **Description**:
    1. Extracts `username`, `password`, and `email` from `request.data`.
    2. Validates that all three fields are present; returns `400 BAD_REQUEST` if any are missing.
    3. Scans existing users with sets (`username_set`, `email_set`) to check uniqueness; returns `400 BAD_REQUEST` if already taken.
    4. Computes next ID (`max_id + 1`), builds the record, persists with `write_json()`, and returns `201 CREATED`.
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
  - **Description**: Reads `users.json` and checks if any user record has `id == user_id`.

##### Persistence Layer (`tasks/services/json_util.py`)

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
| **Users** | `POST` | `/api/users/create/` | Register a new user | `201 Created`, `400 Bad Request` |
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

##### 2. Create Task (`POST /api/tasks/create/`)
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

##### 3. Update Task (`PUT /api/tasks/3/update/`)
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

2. Activate the virtual environment:
   - **macOS / Linux:**
     ```bash
     source .venv/bin/activate
     ```
   - **Windows:**
     ```bat
     .venv\Scripts\activate
     ```

3. Run database migrations (initializes core Django auth/admin tables):
   ```bash
   python manage.py migrate
   ```

4. Start the development server:
   ```bash
   python manage.py runserver
   ```
   The API will be available at `http://127.0.0.1:8000/api/`.

5. Test an endpoint with cURL:
   ```bash
   curl -X GET http://127.0.0.1:8000/api/tasks/
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

---

## Prerequisites & Setup

### Prerequisites
- **Python 3.8+** (Python 3.10+ recommended)
- **pip** (Python package installer)

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
   source .venv/bin/activate   # On Windows: .venv\Scripts\activate
   python manage.py runserver
   ```

---

## License

This repository is created for personal learning and demonstration purposes under the Airtribe curriculum.
