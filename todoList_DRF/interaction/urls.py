from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .api_views import LikeViewSet, BookmarkViewSet, CommentViewSet, CommentLikeViewSet
from .views import todo_detail_with_interaction

router = DefaultRouter()
router.register(r"likes", LikeViewSet, basename="like")
router.register(r"bookmarks", BookmarkViewSet, basename="bookmark")
router.register(r"comments", CommentViewSet, basename="comment")  # ✅ 수정
#r은 경로에 백슬래시 나 정규식 기호가 들어가는 경우를 대비해서 습관적으로 r을 붙이는 것이 일반적입니다.
router.register(r'commentlikes', CommentLikeViewSet, basename='commentlike')  # ✅ 반드시 등록 필요


app_name ="interaction"

urlpatterns = [
    path("", include(router.urls)),
    path('todo/detail/<int:pk>/', todo_detail_with_interaction, name='todo_detail'),
]