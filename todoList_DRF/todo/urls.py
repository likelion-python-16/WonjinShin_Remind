from django.urls import path, include
from . import views
from . import api_views # api_views. To
from .api_views import (
    TodoListAPI,
    TodoCreateAPI,
    TodoRetrieveAPI,
    TodoUpdateAPI,
    TodoDeleteAPI,
    TodoGenericsListAPI, 
    TodoGenericsCreateAPI, 
    TodoGenericsRetrieveAPI, 
    TodoGenericsUpdateAPI,
    TodoGenericsDeleteAPI,
    TodoGenericsListCreateAPI,
    TodoGenericsRetrieveUpdateDeleteAPI,
    TodoViewSet,
    CustomLogoutAPI, 
    
)
from . api_views import *
from rest_framework.routers import DefaultRouter

app_name = "todo"  # 네임스페이스 설정

router = DefaultRouter()
router.register(r"view", TodoViewSet, basename="todo") #r 은 마지막 주소이다 라는 뜻 \ 안써도 됨



urlpatterns = [
    # path("list/", views.todo_list, name="todo_List"), # list 목록보기
    
    # 템플릿Views
    path("list/", views.TodoListViews.as_view(), name="todo_List"), # list 목록보기
    path("create/", views.TodoCreateViews.as_view(), name="todo_Create"),
    path("detail/<int:pk>/", views.TodoDetailViews.as_view(), name="todo_Detail"),
    path("update/<int:pk>/", views.TodoUpdateViews.as_view(), name="todo_Update"), 
    #path("delete/<int:pk>/", views.TodoDeleteViews.as_view(), name="todo_Update"), 
    
    # apiViews
    path("api/list/", api_views.TodoListAPI.as_view(), name="todo_api_list"),
    path("api/create/", api_views.TodoCreateAPI.as_view(), name="todo_api_create"),
    path("api/retrieve/<int:pk>/", api_views.TodoRetrieveAPI.as_view(), name="todo_api_retrieve"),
    path("api/update/<int:pk>/",api_views.TodoUpdateAPI.as_view(), name="todo_api_Update"),
    path("api/delete/<int:pk>/",api_views.TodoDeleteAPI.as_view(), name="todo_api_Delete"),
    
    #GenericAPIView
    path("generics/list/", TodoGenericsListAPI.as_view(), name="todo_api_list"),
    path("generics/create/", TodoGenericsCreateAPI.as_view(), name="todo_api_create"),
    path("generics/retrieve/<int:pk>/", TodoGenericsRetrieveAPI.as_view(), name="todo_api_retrieve"),
    path("generics/update/<int:pk>/",TodoGenericsUpdateAPI.as_view(), name="todo_api_update"),
    path("generics/delete/<int:pk>/",TodoGenericsDeleteAPI.as_view(), name="todo_api_delete"),
    
    #GenericAPIView + Mixin
    path("generics/", TodoGenericsListCreateAPI.as_view(), name="todo_generics_list_create"),
    path("generics/<int:pk>/", TodoGenericsRetrieveUpdateDeleteAPI.as_view(), name="todo_generics_detail"),
    
    # ViewSets
    path("viewsets/", include(router.urls)), #/todo/viewsets/view/
    path("api/custom-logout/", api_views.CustomLogoutAPI.as_view(), name="custom_logout"),
    # logout
    path("api/custom-logout/",CustomLogoutAPI.as_view(),name="custom-logout"),
]

    
    