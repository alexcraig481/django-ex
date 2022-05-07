from django.db import models
from django.contrib.auth.models import User


class Log(models.Model):
    """A log of unhealthy relationship experiences"""
    text = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    objects = models.Manager()

    def __str__(self):
        """Returns a string representation of the model"""
        return f"{self.text}"
