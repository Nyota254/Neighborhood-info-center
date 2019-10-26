from django.contrib import admin
from .models import (
    Neighborhood,
    Neighborhood_buisnesses,
    Neighborhood_contact_info,
    Neighborhood_stories,
    Neighborhood_announcement,
)

admin.site.register(Neighborhood)
admin.site.register(Neighborhood_buisnesses)
admin.site.register(Neighborhood_contact_info)
admin.site.register(Neighborhood_stories)
admin.site.register(Neighborhood_announcement)
