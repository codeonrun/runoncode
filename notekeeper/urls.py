from django.urls import path, include
from . import views

app_name = 'notekeeper'

urlpatterns = [
    path("", views.Index.as_view(), name='index'),
]
