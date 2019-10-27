from django.urls import re_path
from .views import (
    index_view,
    create_story,
    add_buisness,
    add_neighborhood,
)

urlpatterns = [
    re_path('^$',index_view,name="index_view"),
    re_path('^addstory/$',create_story,name="create_story"),
    re_path('^addbuisness/$',add_buisness,name="add_buisness"),
    re_path('^addneighborhood',add_neighborhood,name="add_neighborhood")
]