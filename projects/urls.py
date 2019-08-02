from django.urls import path, re_path
from . import views
from django.views.generic import ListView, DetailView
from projects.models import Articles
from django.conf import settings

urlpatterns = [
    re_path(r'^$', views.listing, name='projects'),
    # re_path(r'^(?P<pk>\d+)$', DetailView.as_view(model=Articles, template_name='projects/post.html'))
]
