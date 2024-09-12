# todo/models.py
from django.db import models
from .utils import resize_image

class Task(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    completed = models.BooleanField(default=False)
    image = models.ImageField(upload_to='task_images/', blank=True, null=True)

    def save(self, *args, **kwargs):
        # 画像が既に存在する場合、新しい名前を取得するためにリサイズ関数を呼び出します
        if self.image:
            self.image = resize_image(self.image, height=400)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title