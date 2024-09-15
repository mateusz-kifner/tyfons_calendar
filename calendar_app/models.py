from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Event(models.Model):
  title = models.CharField(max_length=200)
  description = models.TextField()
  start_time = models.DateTimeField()
  end_time = models.DateTimeField()
  created_at = models.DateTimeField(auto_now_add=True)
  created_by = models.ForeignKey(User, on_delete=models.CASCADE,related_name="event_created_by")
  updated_at = models.DateTimeField(auto_now=True)
  updated_by = models.ForeignKey(User, on_delete=models.CASCADE,related_name="event_updated_by")

  def __str__(self):
    return self.title