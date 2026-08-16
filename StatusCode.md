## Status Codes

Status codes are 3-digit numbers sent by the server in the HTTP response. They tell the client whether the request was successful or what went wrong.

---

## 200 - OK

This is used when the request is successful and the server returns the expected data.

### Common request methods
| Method | Usage |
|--------|-------|
| **GET** | Fetch a resource successfully |
| **PUT** | Update a resource successfully |
| **PATCH** | Partially update a resource successfully |
| **DELETE** | Delete a resource successfully (sometimes returns 200 with a message) |

### Request examples

**GET** - Fetch user details
```
GET /users/101
```

**PUT** - Full update
```
PUT /users/101
```
```json
{
    "name": "Amar S",
    "email": "amarshiva08@gmail.com",
    "age": 26,
    "city": "Mysore"
}
```

**PATCH** - Partial update
```
PATCH /users/101
```
```json
{
    "age": 26
}
```

**DELETE** - Remove resource
```
DELETE /users/101
```

### Django REST Framework snippet
```python
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK

@api_view(["GET"])
def get_user(request, user_id):
    user = {"id": user_id, "name": "Amar S", "age": 25}
    return Response(user, status=HTTP_200_OK)

@api_view(["PUT", "PATCH"])
def update_user(request, user_id):
    updated_user = {"id": user_id, **request.data}
    return Response(updated_user, status=HTTP_200_OK)

@api_view(["DELETE"])
def delete_user(request, user_id):
    return Response({"message": "User deleted successfully"}, status=HTTP_200_OK)
```

### Response example
```json
{
    "id": 101,
    "name": "Amar S",
    "email": "amarshiva08@gmail.com",
    "age": 26,
    "city": "Mysore"
}
```

---

## 201 - Created

This is used when a new resource is successfully created in the backend.

### Common request methods
| Method | Usage |
|--------|-------|
| **POST** | Create a new resource |

### Request example

**POST** - Create a new user
```
POST /users
```
```json
{
    "name": "Amar S",
    "email": "amarshiva08@gmail.com",
    "age": 25,
    "city": "Mysore"
}
```

### Django REST Framework snippet
```python
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.status import HTTP_201_CREATED

@api_view(["POST"])
def create_user(request):
    new_user = {
        "id": 101,
        "name": request.data.get("name"),
        "email": request.data.get("email"),
        "age": request.data.get("age"),
        "city": request.data.get("city"),
    }
    return Response(new_user, status=HTTP_201_CREATED)
```

### Response example
```json
{
    "id": 101,
    "name": "Amar S",
    "email": "amarshiva08@gmail.com",
    "age": 25,
    "city": "Mysore"
}
```

---

## 400 - Bad Request

This is used when the request sent by the client is invalid or malformed.

### Common request methods
| Method | Usage |
|--------|-------|
| **GET** | Invalid query parameters |
| **POST** | Missing or invalid body fields |
| **PUT** | Invalid or incomplete update data |
| **PATCH** | Invalid partial update data |

### Request examples

**GET** - Missing required query parameter
```
GET /addTwoNumbers/
```
Expected:
```
GET /addTwoNumbers/?a=10&b=5
```

**POST** - Missing required field
```
POST /users
```
```json
{
    "name": "Amar S"
}
```

**PUT / PATCH** - Invalid data type
```
PATCH /users/101
```
```json
{
    "age": "twenty-six"
}
```

### Django REST Framework snippet
```python
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.status import HTTP_400_BAD_REQUEST

@api_view(["GET"])
def add_two_numbers(request):
    a = request.query_params.get("a")
    b = request.query_params.get("b")

    if a is None or b is None:
        return Response(
            {"error": "Query parameters 'a' and 'b' are required"},
            status=HTTP_400_BAD_REQUEST,
        )

    try:
        result = int(a) + int(b)
    except ValueError:
        return Response(
            {"error": "Query parameters 'a' and 'b' must be numbers"},
            status=HTTP_400_BAD_REQUEST,
        )

    return Response({"sum": result})

@api_view(["POST"])
def create_user(request):
    required_fields = ["name", "email", "age", "city"]

    for field in required_fields:
        if field not in request.data:
            return Response(
                {"error": f"Missing required field: {field}"},
                status=HTTP_400_BAD_REQUEST,
            )

    return Response({"message": "User created"})
```

### Response example
```json
{
    "error": "Query parameters 'a' and 'b' are required"
}
```

---

## 401 - Unauthorized

This is used when the user is not authenticated (not logged in or invalid credentials).

### Common request methods
| Method | Usage |
|--------|-------|
| **GET** | Access protected resource without login |
| **POST** | Create resource without valid token |
| **PUT** | Update resource without valid token |
| **PATCH** | Partial update without valid token |
| **DELETE** | Delete resource without valid token |

### Request examples

**GET** - No auth token sent
```
GET /users/101
```

**POST** - Invalid or expired token
```
POST /users
Authorization: Bearer invalid_token
```
```json
{
    "name": "Amar S",
    "email": "amarshiva08@gmail.com"
}
```

### Django REST Framework snippet
```python
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.status import HTTP_401_UNAUTHORIZED

@api_view(["GET"])
@permission_classes([IsAuthenticated])
def get_profile(request):
    return Response({"username": request.user.username})

# Manual check example
@api_view(["POST"])
def create_user(request):
    auth_header = request.headers.get("Authorization")

    if not auth_header:
        return Response(
            {"error": "Authentication credentials were not provided"},
            status=HTTP_401_UNAUTHORIZED,
        )

    return Response({"message": "User created"})
```

### Response example
```json
{
    "detail": "Authentication credentials were not provided."
}
```

---

## 403 - Forbidden

This is used when the user is authenticated but does not have permission to access the resource.

### Common request methods
| Method | Usage |
|--------|-------|
| **GET** | View resource without permission |
| **POST** | Create resource without permission |
| **PUT** | Update resource without permission |
| **PATCH** | Partial update without permission |
| **DELETE** | Delete resource without permission |

### Request examples

**GET** - Normal user accessing admin data
```
GET /admin/users
Authorization: Bearer user_token
```

**DELETE** - User trying to delete someone else's account
```
DELETE /users/101
Authorization: Bearer user_token
```

### Django REST Framework snippet
```python
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAdminUser
from rest_framework.response import Response
from rest_framework.status import HTTP_403_FORBIDDEN

@api_view(["GET"])
@permission_classes([IsAdminUser])
def admin_dashboard(request):
    return Response({"message": "Welcome Admin"})

# Manual permission check example
@api_view(["DELETE"])
def delete_user(request, user_id):
    if not request.user.is_staff:
        return Response(
            {"error": "You do not have permission to delete this user"},
            status=HTTP_403_FORBIDDEN,
        )

    return Response({"message": "User deleted"})
```

### Response example
```json
{
    "detail": "You do not have permission to perform this action."
}
```

---

## 404 - Not Found

This is used when the requested resource or URL does not exist on the server.

### Common request methods
| Method | Usage |
|--------|-------|
| **GET** | Resource does not exist |
| **PUT** | Update non-existing resource |
| **PATCH** | Partial update on non-existing resource |
| **DELETE** | Delete non-existing resource |

### Request examples

**GET** - User not found
```
GET /users/999
```

**PUT** - Update user that does not exist
```
PUT /users/999
```
```json
{
    "name": "Amar S",
    "email": "amarshiva08@gmail.com",
    "age": 26,
    "city": "Mysore"
}
```

**PATCH** - Partial update on missing user
```
PATCH /users/999
```
```json
{
    "age": 26
}
```

**DELETE** - Delete missing user
```
DELETE /users/999
```

### Django REST Framework snippet
```python
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.status import HTTP_404_NOT_FOUND

users = {
    101: {"id": 101, "name": "Amar S", "age": 25},
}

@api_view(["GET", "PUT", "PATCH", "DELETE"])
def user_detail(request, user_id):
    user = users.get(user_id)

    if not user:
        return Response(
            {"error": f"User with id {user_id} not found"},
            status=HTTP_404_NOT_FOUND,
        )

    if request.method == "GET":
        return Response(user)

    if request.method == "DELETE":
        del users[user_id]
        return Response({"message": "User deleted"})

    users[user_id] = {**user, **request.data}
    return Response(users[user_id])
```

### Response example
```json
{
    "error": "User with id 999 not found"
}
```

---

## 413 - Payload Too Large

This is used when the request body sent by the client is too large for the server to accept.

### Common request methods
| Method | Usage |
|--------|-------|
| **POST** | Create request with very large body |
| **PUT** | Full update with very large body |
| **PATCH** | Partial update with very large body |

### Request examples

**POST** - Upload very large JSON or file
```
POST /users
Content-Type: application/json
```
```json
{
    "name": "Amar S",
    "bio": "very long text repeated many times..."
}
```

**PUT** - Sending a huge profile update
```
PUT /users/101
Content-Type: application/json
```

### Django REST Framework snippet
```python
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.status import HTTP_413_REQUEST_ENTITY_TOO_LARGE

MAX_BODY_SIZE = 1024 * 1024  # 1 MB

@api_view(["POST", "PUT", "PATCH"])
def create_or_update_user(request):
    body_size = len(request.body)

    if body_size > MAX_BODY_SIZE:
        return Response(
            {"error": "Request body is too large"},
            status=HTTP_413_REQUEST_ENTITY_TOO_LARGE,
        )

    return Response({"message": "Request accepted"})
```

### Response example
```json
{
    "error": "Request body is too large"
}
```

---

## 500 - Internal Server Error

This is used when something goes wrong on the server side while processing the request.

### Common request methods
| Method | Usage |
|--------|-------|
| **GET** | Server crash while fetching data |
| **POST** | Server crash while creating data |
| **PUT** | Server crash while updating data |
| **PATCH** | Server crash while partially updating data |
| **DELETE** | Server crash while deleting data |

### Request examples

Any valid request can return 500 if the backend fails unexpectedly.

**GET**
```
GET /users/101
```

**POST**
```
POST /users
```
```json
{
    "name": "Amar S",
    "email": "amarshiva08@gmail.com"
}
```

### Django REST Framework snippet
```python
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.status import HTTP_500_INTERNAL_SERVER_ERROR

@api_view(["GET"])
def get_user(request, user_id):
    try:
        user = users[user_id]  # may raise KeyError
        return Response(user)
    except Exception:
        return Response(
            {"error": "Something went wrong on the server"},
            status=HTTP_500_INTERNAL_SERVER_ERROR,
        )
```

### Response example
```json
{
    "error": "Something went wrong on the server"
}
```

---

## 502 - Bad Gateway

This is used when the server acting as a gateway or proxy receives an invalid response from an upstream server.

### Common request methods
| Method | Usage |
|--------|-------|
| **GET** | Gateway cannot reach backend service |
| **POST** | Gateway fails while forwarding create request |
| **PUT** | Gateway fails while forwarding update request |
| **PATCH** | Gateway fails while forwarding partial update |
| **DELETE** | Gateway fails while forwarding delete request |

### Request examples

**GET**
```
GET /users/101
```

**POST**
```
POST /users
```

This usually happens in production when:
- Nginx / load balancer is running
- Backend service is down or crashing
- Backend returns an invalid response

### Example scenario
```
Client -> Nginx (Gateway) -> Django Backend (Down)
```

### Response example
```html
502 Bad Gateway
```

---

## Request Timed Out

This happens when the server takes too long to respond and the request exceeds the allowed time limit.

### Common request methods
| Method | Usage |
|--------|-------|
| **GET** | Slow database query while fetching data |
| **POST** | Long-running create operation |
| **PUT** | Long-running update operation |
| **PATCH** | Long-running partial update |
| **DELETE** | Long-running delete operation |

### Request examples

**GET** - Backend takes too long
```
GET /users
```

**POST** - Heavy processing request
```
POST /reports/generate
```
```json
{
    "from_date": "2025-01-01",
    "to_date": "2025-12-31"
}
```

### Django REST Framework snippet
```python
import time
from rest_framework.decorators import api_view
from rest_framework.response import Response

@api_view(["GET"])
def slow_api(request):
    time.sleep(30)  # Simulates a slow backend
    return Response({"message": "Done"})
```

If the client or gateway timeout is 10 seconds, this request may fail with a timeout error.

### Common timeout response
```
Request timed out
```

---

## Too Many Redirects

This happens when a URL keeps redirecting in a loop and never reaches the final destination.

### Common request methods
| Method | Usage |
|--------|-------|
| **GET** | Most common case |
| **POST** | Can happen after login/logout redirect loops |

### Request examples

**GET** - Redirect loop
```
GET /login
```

Example loop:
```
/login  -> redirects to /dashboard
/dashboard -> redirects to /login
/login  -> redirects to /dashboard
...
```

### Django example scenario
```python
from django.shortcuts import redirect

def login_view(request):
    return redirect("dashboard")

def dashboard_view(request):
    return redirect("login")
```

### Browser/client response example
```
Too many redirects
```

---

## Quick Reference

| Status Code | Meaning | Common Methods |
|-------------|---------|----------------|
| 200 | Success | GET, PUT, PATCH, DELETE |
| 201 | Created | POST |
| 400 | Bad Request | GET, POST, PUT, PATCH |
| 401 | Unauthorized | GET, POST, PUT, PATCH, DELETE |
| 403 | Forbidden | GET, POST, PUT, PATCH, DELETE |
| 404 | Not Found | GET, PUT, PATCH, DELETE |
| 413 | Payload Too Large | POST, PUT, PATCH |
| 500 | Internal Server Error | All methods |
| 502 | Bad Gateway | All methods |
| Timeout | Request took too long | All methods |
| Too Many Redirects | Redirect loop | Mostly GET |
