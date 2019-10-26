from django import forms
from .models import (
    Neighborhood,
    Neighborhood_buisnesses,
    Neighborhood_announcement,
    Neighborhood_stories,
    Neighborhood_contact_info,
)

class NeighborhoodCreationForm(forms.ModelForm):
    '''
    Form for creating neighbourhood
    '''
    class Meta:
        model = Neighborhood
        fields = ["name","location"]

class NeighborhoodAnnouncementForm(forms.ModelForm):
    '''
    Form for creatinga announcements
    '''
    class Meta:
        model = Neighborhood_announcement
        fields = ["title","announcement"]

class NeighborhoodBuisnessesForm(forms.ModelForm):
    '''
    Form for advertising a a buisness
    '''
    class Meta:
        model = Neighborhood_buisnesses
        fields = ["buisness_name","buisness_email"]

class NeighborhoodContactForm(forms.ModelForm):
    '''
    Form for adding contacts to the neighbourhood
    '''
    class Meta:
        model = Neighborhood_contact_info
        fields = ["department","contact_number","contact_email"]

class NeighborhoodStoryForm(forms.ModelForm):
    '''
    Form for creating stories about the neighbourhood
    '''
    class Meta:
        model = Neighborhood_stories
        fields = ["title","headline","Story"]

    