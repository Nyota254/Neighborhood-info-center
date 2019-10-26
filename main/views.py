from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import (
    Neighborhood,
    Neighborhood_buisnesses,
    Neighborhood_contact_info,
    Neighborhood_stories,
    Neighborhood_announcement,
) 

@login_required
def index_view(request):
    '''
    Main home page view
    '''
    current_user = request.user
    current_user_neighborhood = request.user.profile.neighborhood 
    title = "home"
    neighborhood_stories = Neighborhood_stories.objects.filter(neighborhood=current_user_neighborhood)
    neighborhood_contacts = Neighborhood_contact_info.objects.filter(neighborhood=current_user_neighborhood)
    neighborhood_buisnesses = Neighborhood_buisnesses.objects.filter(neighborhood=current_user_neighborhood)
    neighborhood_announcements = Neighborhood_announcement.objects.filter(neighborhood=current_user_neighborhood)

    context = {
        "title":title,
        "neighborhood_stories":neighborhood_stories,
        "neighborhood_contacts":neighborhood_contacts,
        "neighborhood_buisnesses":neighborhood_buisnesses,
        "neighborhood_announcements":neighborhood_announcements
    }

    return render(request,"main/index.html",context)
