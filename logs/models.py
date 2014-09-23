from django.db import models


class Entry(models.Model):
    created_on = models.DateTimeField(auto_now_add=True)
    data = models.TextField()
