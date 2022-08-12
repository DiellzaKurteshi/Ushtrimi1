from django.urls import path
from .views import HomeView, School

urlpatterns = [
    path('', HomeView.as_view(), name = 'personal'),
    path('shkollimi/', School.as_view(), name = 'shkollimi'),
]