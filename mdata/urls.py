from django.urls import path
from .views import indexPageView, aboutPageView, statsPageView, displayPersonPageView
            
urlpatterns = [
    path("displayPerson/<int:id>/", displayPersonPageView, name="displayPerson"),
    path("about/", aboutPageView, name="about"),
    path("statistics/", statsPageView, name="stats"),
    path("", indexPageView, name="index"),    
] 