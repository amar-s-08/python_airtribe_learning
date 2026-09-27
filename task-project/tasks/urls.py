from django.urls import path

from .views import create_task, delete_task, login, task_detail, tasks, update_task, user_tasks, users, user_detail, create_user
urlpatterns = [
    # Users
    path("users/",users),
    path("users/<int:user_id>/tasks/",user_tasks),
    path("users/<int:user_id>/",user_detail),
    path("users/create/",create_user),
    path("users/login/",login),

    # Tasks
    path("tasks/",tasks),
    path("tasks/<int:task_id>/",task_detail),
    path("tasks/create/",create_task),
    path("tasks/<int:task_id>/update/",update_task),
    path("tasks/<int:task_id>/delete/",delete_task),
]