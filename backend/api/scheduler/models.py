from django.db import models

# Create your models here.
from django.db import models
from django.contrib.auth.models import User
from paper.models import Source


class ScheduledTask(models.Model):
    frequency_choices = (
        ('daily', 'Daily'),
        ('weekly', 'Weekly'),
        ('monthly', 'Monthly'),
    )

    frequency = models.CharField(max_length=20, choices=frequency_choices)
    last_run_at = models.DateTimeField(null=True, blank=True)
    next_run_at = models.DateTimeField()
    source = models.ForeignKey(Source, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.user.username}'s task for {self.source.name}"
