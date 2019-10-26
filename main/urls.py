from django.urls import re_path
from .views import (
    index_view,
    create_story,
)

urlpatterns = [
    re_path('^$',index_view,name="index_view"),
    re_path('^addstory/$',create_story,name="create_story")
]