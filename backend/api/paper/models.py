from django.db import models

# Create your models here.
from django.db import models

class Source(models.Model):
    name = models.CharField(max_length=100)
    url = models.URLField()

    def __str__(self):
        return self.name


class Keyword(models.Model):
    value = models.CharField(max_length=50)

    def __str__(self):
        return self.value


class Paper(models.Model):
    title = models.CharField(max_length=250)
    abstract = models.TextField()
    source = models.ForeignKey(Source, on_delete=models.CASCADE)
    keywords = models.ManyToManyField(Keyword)
    data_collected_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
