from django.urls import re_path
from .views import (
    index_view,
)

urlpatterns = [
    re_path('^$',index_view,name="index_view")
]