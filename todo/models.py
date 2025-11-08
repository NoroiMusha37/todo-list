from django.db import models
from django.utils import timezone


class Tag(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Task(models.Model):
    content = models.TextField()
    created = models.DateTimeField(default=timezone.now)
    deadline = models.DateTimeField(null=True, blank=True)
    complete = models.BooleanField(default=False)
    tags = models.ManyToManyField(Tag, blank=True)

    def __str__(self):
        return self.content

    class Meta:
        ordering = ['complete', '-created']

    def toggle(self):
        self.complete = not self.complete
        self.save()
