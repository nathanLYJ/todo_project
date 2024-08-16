from django.db import models

# Create your models here.

class Todo(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    is_completed = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    priority = models.IntegerField(default=1)  # 기본값을 1로 설정

    def __str__(self):
        return self.title

