from django.db import models


class Book(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    name = models.CharField(max_length=100, blank=True, default='')
    page = models.TextField(max_length=100, blank=True, default='')
    price = models.BooleanField()

    class Meta:
        ordering = ['created']

    
