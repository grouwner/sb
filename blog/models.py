from django.db import models
from django.utils import timezone


class Post(models.Model):
    author = models.ForeignKey('auth.User')
    title = models.CharField(max_length=200)
    text = models.TextField()
    tag = models.CharField(max_length=100000000000, blank=False, null=False, default="",)
    minuti = models.CharField(max_length=100000000000, blank=False, null=False, default="",)
    image = models.ImageField(blank=True, null=True, upload_to='static', default="",)
    created_date = models.DateTimeField(
            default=timezone.now)
    published_date = models.DateTimeField(
            blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title