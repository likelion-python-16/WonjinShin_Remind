from rest_framework.serializers import ModelSerializer
from .models import Todo
from rest_framework import serializers

class TodoSerializer(ModelSerializer):
    # ✅ 선언 필수!!
    like_count = serializers.SerializerMethodField() #
    is_liked = serializers.SerializerMethodField() #
    is_bookmarked   = serializers.SerializerMethodField() #
    bookmark_count = serializers.SerializerMethodField() #
    comment_count = serializers.SerializerMethodField() 

    class Meta:
        model = Todo
        fields = [  # ✅ 여기 명시적으로 선언!
            'id', 'name', 'description', 'complete', 'completed_at',
            'exp', 'image', 'created_at', 'updated_at',
            'like_count', 'is_liked', 'is_bookmarked', 'bookmark_count', 'comment_count', 
        ]
        read_only_fields = ['completed_at'] # ✅ 필드가 없어도 찾기 않고 읽고 넘기도록 처리

    # ✅ 오버라이딩 처리 필드 선언한 것에 대한 세부함수
    def get_like_count(self, obj):
        return obj.like_set.filter(is_like=True).count()  # 연결된 Like 모델 기준

    def get_is_liked(self, obj):
        user = self.context['request'].user
        return bool(user.is_authenticated and obj.like_set.filter(user=user, is_like=True).exists())

    def get_is_bookmarked(self, obj):
        user = self.context['request'].user
        return bool(user.is_authenticated and
                obj.bookmark_set.filter(user=user, is_marked=True).exists())

    def get_bookmark_count(self, obj):
        return obj.bookmark_set.filter(is_marked=True).count()

    def get_comment_count(self, obj):
        return obj.comment_set.count()