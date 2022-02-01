from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Article(models.Model):
    title = models.CharField(max_length=50, blank=True, null=True)
    description = models.TextField(max_length=299, blank=True, null=True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)
    created_dt = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
