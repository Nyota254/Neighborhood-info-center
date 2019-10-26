from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    '''
    class for user profiles
    '''
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    id_number = models.IntegerField(blank=True,null=True)
    profile_picture = models.ImageField(default="default.jpg",upload_to='profile_pics')
    bio = models.TextField()
    ############
    # TO-DO   neibourhood f-key
    ############
    # neighborhood = models.ForeignKey(Neighbourhood,on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.user.username} profile'