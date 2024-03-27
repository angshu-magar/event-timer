from django.db import models
from django.utils import timezone

# Create your models here.

class Event(models.Model):
    name = models.CharField(null=False, blank=False, max_length=100)
    date = models.DateTimeField(null=False, blank=False)

    @property
    def rem_time(self):
        diff = self.date - timezone.now()
        return diff.days

    @property
    def is_expired(self) -> bool:
        return timezone.now() > self.date
