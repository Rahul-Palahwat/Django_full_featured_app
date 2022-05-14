from distutils.command.upload import upload
from email.policy import default
from django.db import models

# here we are importing default model
from django.contrib.auth.models import User


# Create your models here.

# here we are inheriting models 
class Profile(models.Model):
    # cascade means if a user is deleted then delete the profile also ,but if profile is deleted then there is no need to delete the user
    user=models.OneToOneField(User, on_delete=models.CASCADE)
    image=models.ImageField(default='default.jpg', upload_to='profile_pics')
    def __str__(self):
        return f'{self.user.username} Profile'