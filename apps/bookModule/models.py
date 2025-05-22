from django.db import models
#import userModule.models
from userModule.models import User  # Assuming User model is in userModule

class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=100)
    published_date = models.DateField()
    isbn = models.CharField(max_length=13, unique=True)
    description = models.TextField(blank=True)
    user = models.ForeignKey(User)

    def __str__(self):
        return self.title