from django.db import models
from django.contrib.auth.models import User
from main.models import Neighborhood

class Profile(models.Model):
    '''
    class for user profiles
    '''
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    id_number = models.IntegerField(blank=True,null=True)
    profile_picture = models.ImageField(default="default.jpg",upload_to='profile_pics')
    bio = models.TextField()
    neighborhood = models.ForeignKey(Neighborhood,on_delete=models.CASCADE,blank=True,null=True)

    def __str__(self):
        return f'{self.user.username} profile'