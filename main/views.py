from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import (
    Neighborhood,
    Neighborhood_buisnesses,
    Neighborhood_contact_info,
    Neighborhood_stories,
    Neighborhood_announcement,
) 
from .forms import (
    NeighborhoodStoryForm,
    NeighborhoodCreationForm,
    NeighborhoodContactForm,
    NeighborhoodBuisnessesForm,
    NeighborhoodAnnouncementForm,
)

@login_required
def index_view(request):
    '''
    Main home page view
    '''
    current_user = request.user
    current_user_neighborhood = request.user.profile.neighborhood
    if current_user_neighborhood == None:
        messages.info(request,"Please join a neibourhood to engage by updating your profile") 
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

@login_required
def create_story(request):
    '''
    will handle the creation of neihbourhood storys
    '''
    current_user = request.user
    current_user_neighborhood = request.user.profile.neighborhood
    title = "Post a story"
    if current_user_neighborhood:
        if request.method == "POST":
            form = NeighborhoodStoryForm(request.POST)
            if form.is_valid():
                story = form.save(commit=False)
                story.user = current_user
                story.neighborhood = current_user_neighborhood
                story.save()
                return redirect(index_view)
        else:
            form = NeighborhoodStoryForm()
            return render(request,"main/post_story.html",{"form":form})
    else:
        messages.warning(request,"Please Join a neighbourhood to post a story")
        return redirect(index_view)

@login_required
def add_buisness(request):
    '''
    This view will handle user adding buisness to neighbourehood 
    '''
    current_user_neighborhood = request.user.profile.neighborhood
    if request.method == "POST":
        form = NeighborhoodBuisnessesForm(request.POST)
        if form.is_valid():
            buisness = form.save(commit=False)
            buisness.user = request.user
            buisness.neighborhood = current_user_neighborhood
            buisness.save()
            return redirect(index_view)
    else:
        form = NeighborhoodBuisnessesForm()
        return render(request,"main/buisness_form.html",{"form":form})

@login_required
def add_neighborhood(request):
    '''
    function view for adding neighborhood
    '''
    
    if request.method == "POST":
        form = NeighborhoodCreationForm(request.POST)
        if form.is_valid():
            neighborhood = form.save(commit=False)
            neighborhood.admin = request.user
            neighborhood.save()
            return redirect(index_view)
    else:
        form = NeighborhoodCreationForm()
        return render(request,"main/add_neighborhood.html",{"form":form})

@login_required
def add_contactinfo(request):
    '''
    function view for adding contact info
    '''
    if request.method == "POST":
        contact_form = NeighborhoodContactForm(request.POST)
        if contact_form.is_valid():
            new_contact = contact_form.save(commit=False)
            new_contact.neighborhood = request.user.profile.neighborhood
            new_contact.save()
    else:
        contact_form = NeighborhoodContactForm()

    if request.method == "POST":
        announcement_form = NeighborhoodAnnouncementForm(request.POST)
        if announcement_form.is_valid():
            announcement = announcement_form.save(commit=False)
            announcement.neighborhood = request.user.profile.neighborhood
            announcement.save()
    else:
        announcement_form = NeighborhoodAnnouncementForm()

    context = {
        "c_form":contact_form,
        "a_form":announcement_form,
        "title":"Admin dashboard"
    }

    return render(request,"main/neighborhood_admin.html",context)