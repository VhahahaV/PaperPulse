from django.db import models

# Create your models here.
from django.db import models
from django.contrib.auth.models import User

class Paper(models.Model):
    title = models.CharField(max_length=250)
    abstract = models.TextField()
    data_collected_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class AnalysisResult(models.Model):
    paper = models.ForeignKey(Paper, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    summary = models.TextField()
    keywords = models.JSONField()  # 保存分析得到的关键词

    def __str__(self):
        return f"Analysis of {self.paper.title} by {self.user.username}"
