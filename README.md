# python_airtribe_learning

A comprehensive learning repository covering **Python Fundamentals**, **Data Structures**, **Object-Oriented Programming (OOP)**, **HTTP/REST API Concepts**, and **Django REST Framework (DRF) Web Services**, built as part of the [Airtribe](https://airtribe.live) curriculum.

---

## Table of Contents

- [Repository Overview](#repository-overview)
- [Project Structure](#project-structure)
- [Django Applications](#django-applications)
  - [1. Task Project (`task-project/`) — REST API + React UI](#1-task-project-task-project--rest-api--react-ui)
    - [Architecture & Design Highlights](#architecture--design-highlights)
    - [Core Capabilities & Specialties](#core-capabilities--specialties)
    - [Functions & Utilities Reference](#functions--utilities-reference)
    - [Learning Progression (Commented Code)](#learning-progression-commented-code)
    - [API Endpoints Reference](#api-endpoints-reference)
    - [Sample Payloads & Usage](#sample-payloads--usage)
    - [Running the Task Project](#running-the-task-project)
    - [React Frontend (`task-project/frontend/`)](#react-frontend-task-projectfrontend)
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
4. **Django REST Services**: Full-stack **Task Project** with **PostgreSQL**, **Django ORM** (`User`, `Task` with foreign key), **DRF `ModelViewSet`s** and **`DefaultRouter`**, class-based **login**, and a **React + Vite** UI that consumes the API.

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
└── task-project/                  # Task & User Management (API + UI)
    ├── manage.py                  # Django CLI runner
    ├── docker-compose.yml         # Local PostgreSQL (taskdb)
    ├── postgres_backup.sql        # SQL dump / backup reference
    ├── model.md                   # Notes on models vs entities (Django)
    ├── config/                    # Project settings & root routing
    │   ├── settings.py            # PostgreSQL, rest_framework, tasks app
    │   └── urls.py                # `/admin/`, `/api/` → tasks.urls
    ├── frontend/                  # React + Vite SPA (Taskboard UI)
    │   ├── package.json           # React 19, react-router-dom, Vite
    │   ├── vite.config.js         # Dev proxy: `/api` → Django :8000
    │   └── src/
    │       ├── api.js             # REST client (users, tasks)
    │       ├── auth.jsx           # Client-side session (localStorage)
    │       └── pages/             # Login, tasks, users management
    └── tasks/                     # Django app
        ├── models.py              # User + Task (FK user → tasks)
        ├── serializers.py         # UserSerializer, LoginSerializer, TaskSerializer
        ├── migrations/            # User + Task schema (e.g. 0004_task)
        ├── urls.py                # DefaultRouter + login route
        ├── views.py               # UserViewSet, TaskViewSet, LoginView
        ├── services/json_util.py  # Legacy JSON helpers (earlier exercises; commented in views)
        └── data/                  # Sample JSON from file-based prototype
```

---

## Django Applications

### 1. Task Project (`task-project/`) — REST API + React UI

The **Task Project** is a full-stack app for **Users** and **Tasks**, built with **Django 6.1**, **DRF**, and **PostgreSQL**. Both entities are Django models with a real **foreign key** (`Task.user` → `User`). The API uses **routers and viewsets**; a **React** frontend provides login, task boards, and user management. Earlier function-based and JSON-file implementations remain **commented** in `tasks/views.py` for comparison—see [model.md](task-project/model.md).

#### Architecture & Design Highlights

- **PostgreSQL + ORM**:
  - `User`: unique `username`, `email`, `password`.
  - `Task`: `ForeignKey` to `User` (`related_name="tasks"`), `title`, `description`, `completed`, `created_at`, `updated_at`, `due_date`.
- **DRF routing**:
  - `DefaultRouter` registers `UserViewSet` and `TaskViewSet` at `/api/users/` and `/api/tasks/`.
  - Standard `ModelViewSet` CRUD: list, retrieve, create, update, partial update (`PATCH`), destroy (`DELETE` → `204 No Content`).
- **Custom actions & auth-style login**:
  - `UserViewSet.by_username` → `GET /api/users/username/<username>/` (used by the React login screen).
  - `UserViewSet.tasks` → `GET /api/users/<id>/tasks/` (tasks for one user via ORM).
  - `LoginView` (`APIView`) → `POST /api/users/login/` with `LoginSerializer` (username lookup).
- **Serializers**:
  - `UserSerializer`, `TaskSerializer` (`ModelSerializer`); task `id`, `created_at`, `updated_at` are read-only.
- **React frontend**:
  - Vite dev server on port **5173** proxies `/api` to Django **8000**.
  - Client auth stores the signed-in user in **localStorage** (demo flow, not token/JWT).
- **Docker Compose**: Postgres `taskdb` on `localhost:5432`, aligned with `config/settings.py`.

---

#### Core Capabilities & Specialties

| Capability | Implementation Detail | Specialty / Benefit |
|------------|-----------------------|---------------------|
| **User CRUD** | `UserViewSet` + `UserSerializer` | Full REST CRUD on `/api/users/` with DB uniqueness constraints. |
| **Task CRUD** | `TaskViewSet` + `TaskSerializer` | Tasks persisted in PostgreSQL with FK to user. |
| **Nested tasks by user** | `@action tasks` on `UserViewSet` | `GET /api/users/<id>/tasks/` uses `user.tasks.all()`. |
| **Lookup by username** | `@action by_username` | `GET /api/users/username/<username>/` for sign-in from the UI. |
| **API login endpoint** | `LoginView` + `LoginSerializer` | `POST /api/users/login/` returns user JSON or `404`. |
| **Router URLs** | `DefaultRouter` | No manual `/create/` or `/update/` paths—RESTful resource URLs. |
| **Schema migrations** | `0001_initial` … `0004_task` | Evolves `User` and adds `Task` table. |
| **SPA** | `frontend/` React app | Taskboard: my tasks, all tasks, people, login/register. |

---

#### Functions & Utilities Reference

##### ViewSets & views (`tasks/views.py`)

- **`UserViewSet(ModelViewSet)`**
  - `queryset = User.objects.all()`, `serializer_class = UserSerializer`.
  - Inherits: `list`, `retrieve`, `create`, `update`, `partial_update`, `destroy`.
  - **`by_username`**: `GET` … `/users/username/<username>/` — fetch one user by username.
  - **`tasks`**: `GET` … `/users/<pk>/tasks/` — list tasks for that user (`TaskSerializer`, many=True).
- **`TaskViewSet(ModelViewSet)`**
  - `queryset = Task.objects.all()`, `serializer_class = TaskSerializer`.
  - Full CRUD on `/api/tasks/` and `/api/tasks/<pk>/`.
- **`LoginView(APIView)`**
  - `POST /api/users/login/` — validates `LoginSerializer`, returns serialized user or errors.

##### Serializers (`tasks/serializers.py`)

- **`UserSerializer`**: `id`, `username`, `email`, `password`.
- **`LoginSerializer`**: `username` (POST body for login).
- **`TaskSerializer`**: `id`, `user`, `title`, `description`, `completed`, `created_at`, `updated_at`, `due_date` (timestamps read-only).

##### Models (`tasks/models.py`)

- **`User`**: `username`, `email`, `password` (all unique where applicable).
- **`Task`**: `user` (FK, `CASCADE`, `related_name="tasks"`), `title`, `description`, `completed`, auto timestamps, optional `due_date`.

##### Routing (`tasks/urls.py`)

- `DefaultRouter` → `users`, `tasks` viewsets.
- `path("users/login/", LoginView.as_view())` before/ alongside router include.

#### Learning Progression (Commented Code)

The Task Project keeps earlier implementations **in comments** so you can compare approaches side by side. Active code is at the bottom of `tasks/views.py` (`UserViewSet`, `TaskViewSet`, `LoginView`); everything below walks through what those comments teach.

##### Stage 1 — JSON file storage (`tasks/services/json_util.py`, `tasks/data/`)

- **`read_json` / `write_json`**: Read and write lists of dicts under `tasks/data/` using `pathlib.Path` (portable paths via `Path(__file__).resolve().parent.parent / "data"`).
- **Context managers**: Files opened with `with open(...)` so handles close automatically (comments in `json_util.py` explain why bare `open` + `return json.load` is unsafe).
- **Sample data**: `users.json` and `tasks.json` powered the first version of the API before PostgreSQL.

##### Stage 2 — Function-based views (`@api_view`) and explicit URL paths

Commented in `tasks/views.py` and `tasks/urls.py`:

| HTTP | Old path (commented) | Handler idea |
|------|----------------------|--------------|
| `GET` | `/api/users/` | `read_json(USERS)` or later `User.objects.all()` + serializer |
| `GET` | `/api/users/<user_id>/` | Loop JSON or `User.objects.get` |
| `POST` | `/api/users/create/` | Create user (JSON append or `User.objects.create`) |
| `POST` | `/api/users/login/` | `@api_view` + `LoginSerializer` (replaced by `LoginView`) |
| `GET` | `/api/users/<user_id>/tasks/` | Filter `tasks.json` by `user_id` (see legacy `user_tasks` below) |
| `GET` | `/api/tasks/` | Return full `tasks.json` |
| `GET` | `/api/tasks/<task_id>/` | Scan list for matching `id` |
| `POST` | `/api/tasks/create/` | Append task with `max_id + 1` |
| `PUT` | `/api/tasks/<task_id>/update/` | Mutate dict in list, `write_json` |
| `DELETE` | `/api/tasks/<task_id>/delete/` | `list.remove`, confirmation `200` (not `204`) |

**JSON user create** (commented): required `username`, `password`, `email`; duplicate checks with `set` on usernames/emails; manual `max_id + 1`; `write_json(USERS, users)`.

**JSON task create** (commented): fields `user_id`, `title`, `description`, `iscompleted`, `due_date`; `_user_exists(user_id)` against **`users.json`**; timestamps via **`_utc_now()`** (`%Y-%m-%dT%H:%M:%SZ` UTC).

**Helpers** (commented): `_utc_now()`, `_user_exists()` — only needed for the file-based task flow.

> **Note:** `user_tasks` is still defined as an `@api_view` using JSON filtering, but it is **not** wired in `urls.py` anymore. User tasks are served by **`UserViewSet.tasks`** on the ORM.

##### Stage 3 — Serializers: manual vs `ModelSerializer` (`tasks/serializers.py`)

Commented **manual** serializer:

```python
# class UserSerializer(serializers.Serializer):
#     id = serializers.IntegerField(read_only=True)
#     username = serializers.CharField(max_length=100)
#     ...
```

Active **`ModelSerializer`** maps directly to the `User` / `Task` models and reduces boilerplate. Commented **`create_user`** shows the manual path: `serializer.is_valid()` → `User.objects.create(...)` → serialize response (same idea `ModelViewSet.create` handles for you).

##### Stage 4 — Login: function view vs class view

- **Commented:** `@api_view(["POST"]) def login(...)` with `LoginSerializer` and `User.objects.get(username=...)`.
- **Active:** `LoginView(APIView).post(...)` — same behavior.
- **Comment in code:** function-based and class-based views are equivalent for a single action; class-based views are preferred, but one class cannot define two `post` methods.

##### Stage 5 — `ViewSet` vs `ModelViewSet` (comments above `UserViewSet`)

**`ModelViewSet`** (active) — six operations wired to HTTP:

| ViewSet method | HTTP | Route |
|----------------|------|--------|
| `list` | `GET` | `/users/` |
| `retrieve` | `GET` | `/users/<id>/` |
| `create` | `POST` | `/users/` |
| `update` | `PUT` | `/users/<id>/` |
| `partial_update` | `PATCH` | `/users/<id>/` |
| `destroy` | `DELETE` | `/users/<id>/` |

**`ViewSet`** (commented `class UserViewSet(ViewSet)`) — you implement `list`, `retrieve`, `create`, `update`, `destroy` yourself (no built-in `partial_update`). Comments note **five** database-facing actions vs six on `ModelViewSet`.

Custom endpoints use **`@action`**: `by_username` (`detail=False`) and `tasks` (`detail=True`) — same pattern you would have added on the manual `ViewSet`.

##### Stage 6 — Current stack (what runs in production/dev)

| Layer | From → To |
|-------|-----------|
| Storage | `users.json` / `tasks.json` → **PostgreSQL** (`User`, `Task` FK) |
| Users API | `@api_view` + `/create/` → **`UserViewSet` + router** |
| Tasks API | JSON CRUD + `iscompleted` / `user_id` → **`TaskViewSet` + `completed` / `user` FK** |
| URLs | Manual `path(...)` list → **`DefaultRouter`** + `include(router.urls)` |
| Login | `@api_view` `login` → **`LoginView`** (router path unchanged: `/users/login/`) |

To study an old version, uncomment the relevant blocks in `views.py` / `urls.py` and comment out the `ViewSet` + router wiring (only one routing style should be active at a time).

---

#### API Endpoints Reference

Base path: `http://127.0.0.1:8000/api/` (or via Vite proxy at `http://localhost:5173/api/`).

| Resource | HTTP Method | Endpoint | Description |
|----------|-------------|----------|-------------|
| **Users** | `GET` | `/users/` | List users |
| **Users** | `POST` | `/users/` | Create user |
| **Users** | `GET` | `/users/<id>/` | Retrieve user |
| **Users** | `PUT` | `/users/<id>/` | Replace user |
| **Users** | `PATCH` | `/users/<id>/` | Partial update user |
| **Users** | `DELETE` | `/users/<id>/` | Delete user (`204`) |
| **Users** | `GET` | `/users/username/<username>/` | User by username (custom action) |
| **Users** | `GET` | `/users/<id>/tasks/` | Tasks for user (custom action) |
| **Users** | `POST` | `/users/login/` | Login with `{ "username": "..." }` |
| **Tasks** | `GET` | `/tasks/` | List tasks |
| **Tasks** | `POST` | `/tasks/` | Create task |
| **Tasks** | `GET` | `/tasks/<id>/` | Retrieve task |
| **Tasks** | `PUT` | `/tasks/<id>/` | Replace task |
| **Tasks** | `PATCH` | `/tasks/<id>/` | Partial update (e.g. toggle `completed`) |
| **Tasks** | `DELETE` | `/tasks/<id>/` | Delete task (`204`) |

---

#### Sample Payloads & Usage

##### 1. Create User (`POST /api/users/`)
**Request Body:**
```json
{
  "username": "john_doe",
  "email": "john@example.com",
  "password": "securepassword123"
}
```

##### 2. Sign in (API — `POST /api/users/login/`)
**Request Body:** `{ "username": "john_doe" }`  
**Response (`200 OK`):** User object from `UserSerializer`.

The React app signs in with **`GET /api/users/username/<username>/`** instead (see `frontend/src/api.js`).

##### 3. Create Task (`POST /api/tasks/`)
**Request Body:**
```json
{
  "user": 1,
  "title": "Build Django README",
  "description": "Document viewsets and the React UI.",
  "completed": false,
  "due_date": "2026-09-10T18:00:00Z"
}
```
`user` is the primary key of an existing `User`. `created_at` / `updated_at` are set by the model.

##### 4. Partial update (`PATCH /api/tasks/3/`)
**Request Body:**
```json
{
  "completed": true
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
   curl http://127.0.0.1:8000/api/users/
   curl http://127.0.0.1:8000/api/tasks/
   curl -X POST http://127.0.0.1:8000/api/users/login/ -H "Content-Type: application/json" -d "{\"username\":\"john_doe\"}"
   ```

#### React Frontend (`task-project/frontend/`)

**Taskboard** SPA: sign in or register, view **My tasks** / **All tasks**, manage **People** (users).

1. With Django running on port 8000, from `task-project/frontend`:
   ```bash
   npm install
   npm run dev
   ```
2. Open `http://localhost:5173`. API calls use `/api/...` and are proxied to Django (`vite.config.js`).

| File | Role |
|------|------|
| `src/api.js` | `usersApi`, `tasksApi`, date helpers |
| `src/auth.jsx` | `AuthProvider`, localStorage session |
| `src/pages/LoginPage.jsx` | Sign in (by username) or create account |
| `src/pages/TasksPage.jsx` | Task list/create/edit for current or all users |
| `src/pages/UsersPage.jsx` | User CRUD |

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
- **Node.js 18+** and **npm** for the Task Project React frontend
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

3. Run the Django Task Project (API + optional UI):
   ```bash
   cd task-project
   docker compose up -d
   source .venv/bin/activate   # On Windows: .venv\Scripts\activate
   python manage.py migrate
   python manage.py runserver
   cd frontend && npm install && npm run dev
   ```

---

## License

This repository is created for personal learning and demonstration purposes under the Airtribe curriculum.
