from datetime import datetime, timezone

from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.request import Request
from rest_framework.response import Response

from tasks.services.json_util import read_json, write_json


USERS = "users.json"
TASKS = "tasks.json"

#----------------------------------#
# USERS
#----------------------------------#

# List all users
@api_view(["GET"])
def users(request: Request) -> Response:
    users = read_json(USERS)
    return Response(data=users,status=status.HTTP_200_OK)

# Get User by User ID
# users/1
@api_view(["GET"])
def user_detail(request: Request, user_id: int) -> Response:
    users = read_json(USERS)
    user = None
    for individual_user in users:
        if(individual_user["id"] == user_id):
            user = individual_user
            break
    if user is None:
        return Response({"error": f"User with ID {user_id} not found"},status=status.HTTP_404_NOT_FOUND)
    return Response(user)

# Get Tasks by User Id
@api_view(["GET"])
def user_tasks(request:Request,user_id:int) -> Response:
    if not _user_exists(user_id):
        return Response(
            {"error":f"User with id: {user_id} was not found."},
            status=status.HTTP_404_NOT_FOUND
        )
    tasks = read_json(TASKS)
    filtered_tasks = []
    for t in tasks:
        if t["user_id"] == user_id:
            filtered_tasks.append(t)
    return Response(filtered_tasks)

# Create a New User

@api_view(["POST"])
def create_user(request) -> Response:
    users : list = read_json(USERS)
    username = request.data.get("username")
    password = request.data.get("password")
    email = request.data.get("email")

    username_set : set[str] = set[str]()
    email_set : set[str] = set[str]()
    
    if not username or not password or not email:
        return Response({"error": "Username, password, and email are required"},status=status.HTTP_400_BAD_REQUEST)
    
    max_id = -1
    for u in users:
        max_id = max(max_id, u["id"])
        username_set.add(u["username"])
        email_set.add(u["email"])
    
    if username in username_set or email in email_set:
        return Response({"error":f"userName:  {username} or email: {email} is already taken"},status=status.HTTP_400_BAD_REQUEST)

    new_id = max_id + 1
    user = {
        "id" : new_id,
        "username" : username,
        "password" : password,
        "email" : email,
    }

    users.append(user)
    write_json(USERS, users)
    return Response(user,status=status.HTTP_201_CREATED)

# -----------------------------------------
# TASKS
# -----------------------------------------

def _utc_now()->str:
    return datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")

def _user_exists(user_id: int)-> bool:
    users = read_json(USERS)
    for u in users:
        if(u["id"] == user_id):
            return True
    return False

#List All Tasks
@api_view(["GET"])
def tasks(request:Request)-> Response:
    tasks = read_json(TASKS)
    return Response(tasks)

# Get Task by Task Id
@api_view(["GET"])
def task_detail(request:Request,task_id:int)->Response:
    tasks = read_json(TASKS)
    task = None
    for t in tasks:
        if t["id"] == task_id:
            task = t
            break
    
    if task is None:
        return Response(
            {"error":f"Task with id: {task_id} was not found."},
            status=status.HTTP_404_NOT_FOUND
        )
    
    return Response(task)

#Create a new Task
@api_view(["POST"])
def create_task(request)-> Response:
    tasks:list = read_json(TASKS)
    user_id = request.data.get("user_id")
    title = request.data.get("title")
    description = request.data.get("description","")
    iscompleted = request.data.get("iscompleted",False)
    due_date = request.data.get("due_date")

    if not user_id or not title:
        return Response(
            {"error":"user_id and title are required fields"},
            status = status.HTTP_400_BAD_REQUEST,
        )
    
    if not _user_exists(user_id):
        return Response(
            {"error":f"User with id: {user_id} was not found."},
            status = status.HTTP_400_BAD_REQUEST,
        )
    
    max_id = 0
    for t in tasks:
        max_id = max(max_id,t["id"])
    
    now = _utc_now()
    create_task = {
        "id":max_id+1,
        "user_id":user_id,
        "title":title,
        "description":description,
        "iscompleted":iscompleted,
        "created_at":now,
        "updated_at":now,
        "due_date":due_date
    }

    tasks.append(create_task)

    write_json(TASKS,tasks)

    return Response(create_task,status=status.HTTP_201_CREATED)

# update an Existing Task
@api_view(["PUT"])
def update_task(request,task_id:int)-> Response:
    tasks:list = read_json(TASKS)

    task = None
    for t in tasks:
        if t["id"] == task_id:
            task = t
            break
    if task is None:
        return Response(
            {"error":f"Task with id: {task_id} was not found."},
            status=status.HTTP_404_NOT_FOUND,
        )
    
    user_id = request.data.get("user_id",task["user_id"])
    title = request.data.get("title",task["title"])
    description = request.data.get("description",task["description"])
    iscompleted = request.data.get("iscompleted",task["iscompleted"])
    due_date = request.data.get("due_date",task["due_date"])

    if not user_id or not title:
        return Response(
            {"error":"user_id and title are required fields."},
            status=status.HTTP_400_BAD_REQUEST
        )
    if not _user_exists(user_id):
        return Response(
            {"error":f"User with id: {user_id} was not found."},
            status=status.HTTP_400_BAD_REQUEST
        )
    task["user_id"] = user_id
    task["title"] = title
    task["description"] = description
    task["iscompleted"] = iscompleted
    task["due_date"] = due_date
    task["updated_at"] = _utc_now()

    write_json(TASKS,tasks)
    return Response(task)

#delete an Existing Task.
@api_view(["DELETE"])
def delete_task(request,task_id:int) -> Response:
    tasks:list = read_json(TASKS)

    task = None
    for t in tasks:
        if t["id"] == task_id:
            task = t
            break
    
    if task is None:
        return Response(
            {"error":f"Task with id: {task_id} was not Found."},
            status=status.HTTP_404_NOT_FOUND,
        )
    tasks.remove(task)
    write_json(TASKS, tasks)

    return Response(
        {"message":f"Task with id: {task_id} was deleted successfully!."},
        status=status.HTTP_200_OK,
    )