from django.db import models

# for date time 
from django.utils import timezone

from django.contrib.auth.models import User



# Create your models here.
class Post(models.Model):
    title=models.CharField(max_length=100)
    content=models.TextField()
    # date_posted:models.DateTimeField(auto_now_add=True)
    date_posted=models.DateTimeField(default=timezone.now)
    # if the author is deleted from the database so to deal with the post of that user we use on_delete
    author=models.ForeignKey(User,on_delete=models.CASCADE)

    # these are called magic methods or double undescore method 
    def __str__(self):
        return self.title