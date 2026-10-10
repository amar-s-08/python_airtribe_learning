from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .views import TaskViewSet, UserViewSet, login,LoginView

router = DefaultRouter()
router.register("users", UserViewSet, basename="users")
router.register("tasks",TaskViewSet,basename="tasks")
urlpatterns = [
    # Users
    # path("users/",users),
    # path("users/<int:user_id>/tasks/",user_tasks),
    # path("users/<int:user_id>/",user_detail),
    # path("users/create/",create_user),
    # path("users/login/",login),
    path("users/login/",LoginView.as_view()),

    path("", include(router.urls)),

    # Tasks
    # path("tasks/",tasks),
    # path("tasks/<int:task_id>/",task_detail),
    # path("tasks/create/",create_task),
    # path("tasks/<int:task_id>/update/",update_task),
    # path("tasks/<int:task_id>/delete/",delete_task),
]