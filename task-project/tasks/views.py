from datetime import datetime, timezone
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet, ViewSet
from rest_framework import status
from rest_framework.decorators import action, api_view
from rest_framework.request import Request
from rest_framework.response import Response

from tasks.models import Task, User
from tasks.serializers import LoginSerializer, TaskSerializer, UserSerializer
from tasks.services.json_util import read_json, write_json


USERS = "users.json"
TASKS = "tasks.json"

#----------------------------------#
# USERS
#----------------------------------#

# ViewSet
# 1. Listing all the entities of a certain type.
# 2. Get an entity by ID.
# 3. Create an entity in DB.
# 4. Delete
# 5. UPDATE

# CRUD operations
# C - Create | R - Retrieve / Read | U - Update | D - Delete

# Django provides a ViewSet class that helps us to implement the CRUD operations.

#  ModelViewSet is a class that provides the CRUD operations for a model, totally there will be 6 calls to the database.
#  1. list() -> GET /users/
#  2. retrieve() -> GET /users/<id>/
#  3. create() -> POST /users/
#  4. update() -> PUT /users/<id>/
#  5. destroy() -> DELETE /users/<id>/
#  6. partial_update() -> PATCH /users/<id>/
class UserViewSet(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    
    # if we want to write a create method we can override the method.
    # Any custom methods should be written from developer
    # Fetch by username - Get username/<username>
    @action(detail = False, methods = ["GET"], url_path=r"username/(?P<username>[\w.@+-]+)")
    def by_username(self,request: Request, username: str) -> Response:
        try:
            user = User.objects.get(username = username)
        except User.DoesNotExist:
            return Response('User with username: {username} Not Found',status=status.HTTP_404_NOT_FOUND)
        outgoing_data = UserSerializer(user).data
        return Response(data=outgoing_data,status=status.HTTP_200_OK)

    # GET /users/<id>/tasks/ — every task assigned to this user
    @action(detail=True, methods=["GET"])
    def tasks(self, request: Request, pk=None) -> Response:
        user = self.get_object()
        tasks = user.tasks.all()
        outgoing_data = TaskSerializer(tasks, many=True).data
        return Response(data=outgoing_data, status=status.HTTP_200_OK)


#  ViewSet is a class that provides the CRUD operations for a view, totally there will be 5 calls to the database.
#  1. list() -> GET /users/
#  2. retrieve() -> GET /users/<id>/
#  3. create() -> POST /users/
#  4. update() -> PUT /users/<id>/
#  5. destroy() -> DELETE /users/<id>/

# class UserViewSet(ViewSet):
    # list()  -> GET /users/

    # def list(self, request: Request) -> Response:
    #     users = User.objects.all()
        
    #     outgoing_data = UserSerializer(users, many=True).data
    #     return Response(data=outgoing_data, status=status.HTTP_200_OK)

    # # retrieve() -> GET /users/<id>/

    # def retrieve(self, request: Request, pk=None) -> Response:
    #     try:
    #         user = User.objects.get(id=pk)
    #     except User.DoesNotExist:
    #         return Response({"error": f"User with ID {pk} not found"},status=status.HTTP_404_NOT_FOUND)
    #     outgoing_data = UserSerializer(user).data
    #     return Response(data=outgoing_data, status=status.HTTP_200_OK)

    # # create()  -> POST /users/

    # def create(self, request: Request) -> Response:
    #     # Accept the data using a serializer
    #     serializer = UserSerializer(data=request.data)
    #     if not serializer.is_valid():
    #         return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    #     # Save the data to the database
    #     # INSERT INTO users (username, email, password) VALUES (1, "amar.s@example.com", "password")
    #     validated_data = serializer.validated_data
    #     try:
    #         created_user = User.objects.create(
    #             username=validated_data["username"],
    #             email=validated_data["email"],
    #             password=validated_data["password"]
    #         )
    #     except Exception as e:
    #         return Response(
    #             {"error":str(e)},
    #             status=status.HTTP_400_BAD_REQUEST
    #         )
    #     # Return the output data using a serializer
    #     output_data = UserSerializer(created_user).data
    #     return Response(data = output_data,status=status.HTTP_201_CREATED)

    # # update() -> PUT /users/<id>/
    # def update(self, request: Request, pk=None) -> Response:
    #     try:
    #         user = User.objects.get(id=pk)
    #     except User.DoesNotExist:
    #         return Response(
    #             {"error":f"User with id : {pk} was not found."},
    #             status=status.HTTP_404_NOT_FOUND
    #         )
    #         serializer = UserSerializer(user, data=request.data)
    #         if not serializer.is_valid():
    #             return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    #         validated_data = serializer.validated_data
    #         user.username = validated_data["username"]
    #         user.email = validated_data["email"]
    #         user.password = validated_data["password"]
    #         user.save()
    #         output_data = UserSerializer(user).data
    #         return Response(data=output_data,status=status.HTTP_200_OK)


    # # destroy()  -> DELETE/users/<id>/
    # def destroy(self, request: Request, pk=None) -> Response:
    #     try:
    #         user = User.objects.get(id=pk)
    #     except User.DoesNotExist:
    #         return Response(
    #             {"error":f"User with id : {pk} was not found."},
    #             status=status.HTTP_404_NOT_FOUND
    #         )
    #     user.delete()
    #     return Response(status=status.HTTP_204_NO_CONTENT)
    
    # # Fetch by username - Get username/<username>
    # @action(detail = False, methods = ["GET"], url_path=r"username/(?P<username>[\w.@+-]+)")
    # def by_username(self,request: Request, username: str) -> Response:
    #     try:
    #         user = User.objects.get(username = username)
    #     except User.DoesNotExist:
    #         return Response('User with username: {username} Not Found',status=status.HTTP_404_NOT_FOUND)
    #     outgoing_data = UserSerializer(user).data
    #     return Response(data=outgoing_data,status=status.HTTP_200_OK)

# List all users
# @api_view(["GET"])
# def users(request: Request) -> Response:
#     users = read_json(USERS)
#     return Response(data=users,status=status.HTTP_200_OK)

# @api_view(["GET"])
# def users(request: Request) -> Response:
#     # SELECT * FROM users;
#     users = User.objects.all()
#     outgoing_data = UserSerializer(users, many=True).data
#     return Response(data=outgoing_data, status=status.HTTP_200_OK)

# Get User by User ID
# users/1
# @api_view(["GET"])
# def user_detail(request: Request, user_id: int) -> Response:
#     users = read_json(USERS)
#     user = None
#     for individual_user in users:
#         if(individual_user["id"] == user_id):
#             user = individual_user
#             break
#     if user is None:
#         return Response({"error": f"User with ID {user_id} not found"},status=status.HTTP_404_NOT_FOUND)
#     return Response(user)

# @api_view(["GET"])
# def user_detail(request: Request, user_id: int) -> Response:
#     try:
#         user = User.objects.get(id=user_id)
#     except User.DoesNotExist:
#         return Response({"error": f"User with ID {user_id} not found"},status=status.HTTP_404_NOT_FOUND)
#     outgoing_data = UserSerializer(user).data
#     return Response(data=outgoing_data, status=status.HTTP_200_OK)

# Login using Username only
# @api_view(["POST"])
# def login(request: Request) -> Response:
#     username = request.data.get("username")
#     if not username:
#         return Response({"error": "Username is required"},status=status.HTTP_400_BAD_REQUEST)
#     users = read_json(USERS)
#     for u in users:
#         if u["username"] == username:
#             return Response(u,status=status.HTTP_200_OK)
    
#     return Response({"error": "Invalid username"},status=status.HTTP_404_NOT_FOUND)

# @api_view(["POST"])
# def login(request: Request) -> Response:
#     serializer = LoginSerializer(data=request.data)
#     if not serializer.is_valid():
#         return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
#     validated_data = serializer.validated_data
#     username = validated_data["username"]
#     try:
#         user = User.objects.get(username=username)
#     except User.DoesNotExist:
#         return Response({"error": "Invalid username"},status=status.HTTP_404_NOT_FOUND)
#     validated_data = UserSerializer(user).data
#     return Response(validated_data,status=status.HTTP_200_OK)

class LoginView(APIView):
    def post(self, request: Request) -> Response:
        serializer = LoginSerializer(data=request.data)
        
        if not serializer.is_valid():
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
        
        validated_data = serializer.validated_data
        username = validated_data["username"]
        
        try:
            user = User.objects.get(username=username)
        except User.DoesNotExist:
            return Response({"error": "Invalid username"},status=status.HTTP_404_NOT_FOUND)
        
        validated_data = UserSerializer(user).data
        return Response(validated_data,status=status.HTTP_200_OK)

# @api_view(["POST"]) and class LoginView(APIView) are the same, There are both same class based views are preferred over function based views but 1 drawback is u cannot have more than 1 action method in a class based view example u cannot have 2 post methods at once.

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

# @api_view(["POST"])
# def create_user(request) -> Response:
#     users : list = read_json(USERS)
#     username = request.data.get("username")
#     password = request.data.get("password")
#     email = request.data.get("email")

#     username_set : set[str] = set[str]()
#     email_set : set[str] = set[str]()
    
#     if not username or not password or not email:
#         return Response({"error": "Username, password, and email are required"},status=status.HTTP_400_BAD_REQUEST)
    
#     max_id = -1
#     for u in users:
#         max_id = max(max_id, u["id"])
#         username_set.add(u["username"])
#         email_set.add(u["email"])
    
#     if username in username_set or email in email_set:
#         return Response({"error":f"userName:  {username} or email: {email} is already taken"},status=status.HTTP_400_BAD_REQUEST)

#     new_id = max_id + 1
#     user = {
#         "id" : new_id,
#         "username" : username,
#         "password" : password,
#         "email" : email,
#     }

#     users.append(user)
#     write_json(USERS, users)
#     return Response(user,status=status.HTTP_201_CREATED)

# Create a New User Using Serializer
# @api_view(["POST"])
# def create_user(request) -> Response:
#     # Accept the data using a serializer
#     serializer = UserSerializer(data=request.data)
#     if not serializer.is_valid():
#         return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
#     # Save the data to the database
#     # INSERT INTO users (username, email, password) VALUES (1, "amar.s@example.com", "password")
#     validated_data = serializer.validated_data
#     try:
#         created_user = User.objects.create(
#             username=validated_data["username"],
#             email=validated_data["email"],
#             password=validated_data["password"]
#         )
#     except Exception as e:
#         return Response(
#             {"error":str(e)},
#             status=status.HTTP_400_BAD_REQUEST
#         )
#     # Return the output data using a serializer
#     output_data = UserSerializer(created_user).data
#     return Response(data = output_data,status=status.HTTP_201_CREATED)

# -----------------------------------------
# TASKS
# -----------------------------------------

# def _utc_now()->str:
#     return datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")

# def _user_exists(user_id: int)-> bool:
#     users = read_json(USERS)
#     for u in users:
#         if(u["id"] == user_id):
#             return True
#     return False

# #List All Tasks
# @api_view(["GET"])
# def tasks(request:Request)-> Response:
#     tasks = read_json(TASKS)
#     return Response(tasks)

# # Get Task by Task Id
# @api_view(["GET"])
# def task_detail(request:Request,task_id:int)->Response:
#     tasks = read_json(TASKS)
#     task = None
#     for t in tasks:
#         if t["id"] == task_id:
#             task = t
#             break
    
#     if task is None:
#         return Response(
#             {"error":f"Task with id: {task_id} was not found."},
#             status=status.HTTP_404_NOT_FOUND
#         )
    
#     return Response(task)

# #Create a new Task
# @api_view(["POST"])
# def create_task(request)-> Response:
#     tasks:list = read_json(TASKS)
#     user_id = request.data.get("user_id")
#     title = request.data.get("title")
#     description = request.data.get("description","")
#     iscompleted = request.data.get("iscompleted",False)
#     due_date = request.data.get("due_date")

#     if not user_id or not title:
#         return Response(
#             {"error":"user_id and title are required fields"},
#             status = status.HTTP_400_BAD_REQUEST,
#         )
    
#     if not _user_exists(user_id):
#         return Response(
#             {"error":f"User with id: {user_id} was not found."},
#             status = status.HTTP_400_BAD_REQUEST,
#         )
    
#     max_id = 0
#     for t in tasks:
#         max_id = max(max_id,t["id"])
    
#     now = _utc_now()
#     create_task = {
#         "id":max_id+1,
#         "user_id":user_id,
#         "title":title,
#         "description":description,
#         "iscompleted":iscompleted,
#         "created_at":now,
#         "updated_at":now,
#         "due_date":due_date
#     }

#     tasks.append(create_task)

#     write_json(TASKS,tasks)

#     return Response(create_task,status=status.HTTP_201_CREATED)

# # update an Existing Task
# @api_view(["PUT"])
# def update_task(request,task_id:int)-> Response:
#     tasks:list = read_json(TASKS)

#     task = None
#     for t in tasks:
#         if t["id"] == task_id:
#             task = t
#             break
#     if task is None:
#         return Response(
#             {"error":f"Task with id: {task_id} was not found."},
#             status=status.HTTP_404_NOT_FOUND,
#         )
    
#     user_id = request.data.get("user_id",task["user_id"])
#     title = request.data.get("title",task["title"])
#     description = request.data.get("description",task["description"])
#     iscompleted = request.data.get("iscompleted",task["iscompleted"])
#     due_date = request.data.get("due_date",task["due_date"])

#     if not user_id or not title:
#         return Response(
#             {"error":"user_id and title are required fields."},
#             status=status.HTTP_400_BAD_REQUEST
#         )
#     if not _user_exists(user_id):
#         return Response(
#             {"error":f"User with id: {user_id} was not found."},
#             status=status.HTTP_400_BAD_REQUEST
#         )
#     task["user_id"] = user_id
#     task["title"] = title
#     task["description"] = description
#     task["iscompleted"] = iscompleted
#     task["due_date"] = due_date
#     task["updated_at"] = _utc_now()

#     write_json(TASKS,tasks)
#     return Response(task)

# #delete an Existing Task.
# @api_view(["DELETE"])
# def delete_task(request,task_id:int) -> Response:
#     tasks:list = read_json(TASKS)

#     task = None
#     for t in tasks:
#         if t["id"] == task_id:
#             task = t
#             break
    
#     if task is None:
#         return Response(
#             {"error":f"Task with id: {task_id} was not Found."},
#             status=status.HTTP_404_NOT_FOUND,
#         )
#     tasks.remove(task)
#     write_json(TASKS, tasks)

#     return Response(
#         {"message":f"Task with id: {task_id} was deleted successfully!."},
#         status=status.HTTP_200_OK,
#     )

class TaskViewSet(ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer