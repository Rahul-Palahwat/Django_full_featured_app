from distutils.command.upload import upload
from email.policy import default
from django.db import models


# to handle image manipulation
from PIL import Image



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


    # this is to auto resize the image 
    def save(self):
        super().save()

        img = Image.open(self.image.path)

        if img.height>300 or img.width>300:
            output_size=(300,300)
            img.thumbnail(output_size)
            img.save(self.image.path)
