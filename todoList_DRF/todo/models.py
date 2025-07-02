from django.db import models
from django.utils import timezone

class Todo(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    complete = models.BooleanField(default=False)
    exp = models.PositiveIntegerField(default=0)
    completed_at = models.DateTimeField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    #이미지 필드 추가
    image = models.ImageField(upload_to='todo_images/', null=True, blank=True)
    
    
    def __str__(self):
        return self.name
    
    # 기본 동작 보안: complete 값에 따라 자동으로 시간이 처리되게
    def save(self, *args, **kwargs):
        if self.complete and self.completed_at is None:
            self.completed_at = timezone.now()
        if not self.complete and self.completed_at is not None:
            self.completed_at = None
        super().save(*args, **kwargs)