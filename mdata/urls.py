from django.urls import path
from .views import indexPageView, aboutPageView, statsPageView
            
urlpatterns = [
    path("about/", aboutPageView, name="about"),
    path("statistics/", statsPageView, name="stats"),
    path("", indexPageView, name="index"),    
] 