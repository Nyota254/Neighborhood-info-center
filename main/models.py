from django.db import models
from django.contrib.auth.models import User

class Neighborhood(models.Model):
    '''
    This models will contain all the names of the neighbourhoods created
    '''
    name = models.CharField(max_length=40)
    location = models.CharField(max_length=250)
    # occupants_count = models.IntegerField()
    admin = models.ForeignKey(User,on_delete=models.CASCADE)

    def create_neighborhood(self):
        self.save()

    def delete_neighborhood(self):
        self.delete()

    @classmethod
    def find_neighborhood(cls):
        pass

    @classmethod
    def update_neighborhood(cls):
        pass

    @classmethod
    def update_occupants(cls):
        pass

    def __str__(self):
        return f'{self.name} neighborhood'

class Neighborhood_buisnesses(models.Model):
    '''
    This class will contain the buisness in the neighbourhood
    '''
    buisness_name = models.CharField(max_length=40)
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    neighborhood = models.ForeignKey(Neighborhood,on_delete=models.CASCADE)
    buisness_email = models.EmailField()

    @classmethod
    def buisness_search(cls,pk):
        pass

    def __str__(self):
        return f'Buisness {self.buisness_name} Owned by {self.user.username}'

class Neighborhood_stories(models.Model):
    '''
    This class will contain the raising issues in the neighborhood (posts and info)
    '''
    title = models.CharField(max_length=30)
    headline = models.TextField(max_length=255)
    Story = models.TextField()
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    neighborhood = models.ForeignKey(Neighborhood,on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.title} story from {self.neighborhood.name} Neighborhood'

class Neighborhood_contact_info(models.Model):
    '''
    This class will contain the neighbourhood contact information such health department and police e.t.c
    '''
    department = models.CharField(max_length=30)
    contact_number = models.IntegerField()
    contact_email = models.EmailField()
    neighborhood = models.ForeignKey(Neighborhood,on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.department} department contact from {self.Neighborhood.name} neighborhood'

class Neighborhood_announcement(models.Model):
    '''
    Announcements model
    '''
    title = models.CharField(max_length=30)
    announcement = models.TextField()
    neighborhood = models.ForeignKey(Neighborhood,on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.title} Announcement for {self.neighborhood.name} Neighborhood' 
    
    
