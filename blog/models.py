from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Post (models.Model):
    title = models.CharField(max_length= 30)
    content = models.TextField()

    head_image = models.ImageField(upload_to='blog/%Y/%m/%d', blank=True)
    # blank = True 이 항목은 꼭 채우지 않아도 된다
    # models.py가 수정될 때마다 migration 해줘야함

    created = models.DateTimeField()
    author = models.ForeignKey(User, on_delete=True)

    def __str__(self):
        return '{} :: {}'.format (self.title, self.author)