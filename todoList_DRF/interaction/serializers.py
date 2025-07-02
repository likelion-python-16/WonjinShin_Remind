from .models import Like, Bookmark, Comment, CommentLike
from rest_framework import serializers



# user.username, todo.name

class LikeSerializer(serializers.ModelSerializer):
    username = serializers.CharField(source='user.username', read_only=True)
    # user의 외래키를 통해출력 전용이라 응답용을만 사용한다. 즉 이 필드는 확인용으로 읽기 전용이라 요청용으로 사용하지않는다.
    todo_name = serializers.CharField(source='todo.name', read_only=True)
    
    class Meta:
        model = Like
        fields = ["id", "todo", "todo_name", "user", "username", "is_like"]
        read_only_fields = ["user"]
        
# read_only=True: 이 필드느 출력전용으로 클라이언트가 값을 보내도 저장에는 사용되지 않는다.

class BookmarkSerializer(serializers.ModelSerializer):
    username = serializers.CharField(source='user.username', read_only=True)
    todo_name = serializers.CharField(source='todo.name', read_only=True)
    
    class Meta:
        model = Bookmark
        fields = ["id", "todo", "todo_name", "user", "username", "is_marked"]
        read_only_fields = ["user"]
    
class CommentSerializer(serializers.ModelSerializer):
    username = serializers.CharField(source='user.username', read_only=True)
    todo_name = serializers.CharField(source='todo.name', read_only=True)
    
    like_count = serializers.SerializerMethodField()
    is_liked = serializers.SerializerMethodField()
     
    class Meta:
        model = Comment
        fields = ["id", "todo", "todo_name", "user", "username", "content", "created_at", "like_count", "is_liked"]
        read_only_fields = ["todo", "user", "created_at"]
        # 폼에서 사용자가 수정할 수 없어야 하는 필드를 명확이 구분해주기 위한 용도
        
    def get_like_count(self, obj):
        return obj.likes.count()
        # 댓글에 좋아요를 누른 유저들의 수를 반환하는 메서드
        
    def get_is_liked(self, obj):
        # 현재 사용자가 이 댓글을 좋아요 눌렀는지 여부를 반환하는 메서드
        request = self.context.get('request')
        if request and request.user.is_authenticated:
            return obj.likes.filter(id=request.user.id).exists()
        return False
        
        
# 시리얼라이저의 역활
# - 직렬화 : 모델 인스턴스를 JSON으로 변환
# - 역직렬화 : JSON을 모델 인스턴스로 변환
# - 유효성 검사 : 클라이언트가 보낸 데이터의 유효성을 검사
# - 권한 설정 : 특정 필드에 대한 읽기/쓰기 권한을 설정
# - 필드 지정 : 어떤 필드를 직렬화할지 지정
# - 필드 변환 : 모델 필드를 다른 형식으로 변환
# -------------------------------------
# - 유효성 검증, 프레젠테이션 로직 처리
# - 화면에 표시되는 방식 스타일과 관련된 로직을 처리한다.
# - 값이 올바른지 확인하고, 잘못된 경우 오류 메시지를 반환한다.( 그 값을 어떻게 보여줄것이냐?)

# M2M 추가

# 댓글 좋아요(M2M) 직렬화
from.models import CommentLike

class CommentLikeSerializer(serializers.ModelSerializer):
    username = serializers.CharField(source='user.username', read_only=True)
    comment_content = serializers.CharField(source='comment.content', read_only=True)
    

    class Meta:
        model = CommentLike
        fields = ["id", "user", "username", "comment", "comment_content", "is_like", 'liked_at']
        read_only_fields = ["user", 'liked_at']

    # def get_like_count(self, obj):
    #     return obj