from django.db import models
from todo.models import Todo
from django.contrib. auth.models import User

# 좋아요 모델
class Like(models.Model):

    # 공통필드
    # 개별필드
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    todo = models.ForeignKey(Todo, on_delete=models.CASCADE)
    is_like = models.BooleanField(default=True) # 좋아요 여부 
    
    class Meta: # 중복 방지
        unique_together = ("user", "todo")
        # todo, user 속성은 중복 데이터를 아예 저장하지 못하게 막아주는 제약조건
    
    def __str__(self):
        return f"{self.user.username} ❤️ {self.todo.name} "
        # admin ❤️ 공부하기
        
# 북마크 모델
class Bookmark(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    todo = models.ForeignKey(Todo, on_delete=models.CASCADE)
    is_marked = models.BooleanField(default=True)
    
    class Meta: # 중복 방지
        unique_together = ("user", "todo")
        # todo, user 속성은 중복 데이터를 아예 저장하지 못하게 막아주는 제약조건

    def __str__(self):
        return f"{self.user.username} 📌 {self.todo.name} "
        # admin 📌 공부하기 


# 댓글 모델
class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    todo = models.ForeignKey(Todo, on_delete=models.CASCADE) 
    content = models.TextField() # 댓글 내용
    created_at = models.DateTimeField(auto_now_add=True) # 댓글 작성 시간
    # 댓글을 좋아요를 누른 유저들을 저장하는 필드
    likes = models.ManyToManyField(User, through = "CommentLike", related_name="liked_comments", blank=True)
        
    def __str__(self):
        return f"{self.user.username} 💬 {self.content[:20]} "
        # admin 💬 공부하기
        
# 누가 어떤 댓글을 언제 좋아요 눌렀는지 기록
class CommentLike(models.Model):
   
    comment = models.ForeignKey(Comment, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    liked_at = models.DateTimeField(auto_now_add=True)
    # 사용자가 댓글에 좋아요를 누른 시간을 자동으로 저장하기 위한 필드
    
    is_like = models.BooleanField(default=True)
    # 현재 좋아요가 유효한지 여부의 bool값
    
    class Meta: # 중복 방지
        unique_together = ("user", "comment")
        
    def __str__(self):
        return f"{self.user.username} ❤️ {self.comment.id}"
    
    
# 모델의 역활
# - 비즈니스 로직을 처리한다.
# - 데이터 저장, 검증 처리
# - 어떤 값이 나와야 하는지 정의(처리)한다.