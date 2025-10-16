import datetime
from django.utils import timezone
from django.db import models
from django.forms import DateTimeField
from django.contrib.auth.models import User

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def was_updated_recently(self):
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.updated_at <= now


