from django.urls import path
from app.views.cat import home, cat

urlpatterns = [
    path("", home, name='home'),
    path("cat/", cat, name='cat'),
]