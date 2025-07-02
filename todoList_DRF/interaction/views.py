from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django. contrib.auth.decorators import login_required
from todo.models import Todo
from interaction.models import Like, Bookmark, Comment

# 로그인하지 않은 사용자가 이 뷰를 실행하지 못하도록 막아주는 데코레이션
@login_required # 로그인확인여부에 따라 접근금지 또는 로그인 페이지 보내기 역활
def todo_detail_with_interaction(request, pk):
    todo = get_object_or_404(Todo, pk=pk)  # todo 객체를 pk로 조회하고, 해당 객체가 없으면 404 에러를 발생시킴
    user = request.user
    
    like_obj = Like.objects.filter(todo=todo, is_like=True).first()
    is_liked = like_obj.is_like if like_obj else False
    # todo에 대한 좋아요 객체를 조회하고, 좋아요가 없는 경우 NONE을 반환한다.
    
    like_count = Like.objects.filter(todo=todo, is_like=True).count()
    # todo 에 대한 좋아요 개수를 조회한다.
    # is_like=True 조건을 통해 좋아요가 눌린 경우만 카운트 한다. 로그인한 사람이 눌렀기 때문.
    bookmark_obj = Bookmark.objects.filter(todo=todo, user=user).first()
    # todo에 대한 북마크 객체를 조회하고, 북마크가 없는 경우 NONE을 반환한다. 로그인한 사용자가 북마크를 눌렀기 때문.
    comments = Comment.objects.filter(todo=todo).order_by("-created_at")
    # todo에 대한 댓글들을 조회하고, 최신순으로 정렬한다.
    
    context = {
        "todo" :todo,
        "like_obj" : like_obj,
        "like_count" : like_count,
        "bookmark_obj" : bookmark_obj,
        "comments" : comments,
    } # 예시 =  {interaaction:like_obj}
    
    return render(request, "interaction/todo_detail.html", context)