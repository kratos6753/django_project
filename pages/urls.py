from django.urls import path

from .views import HomePageView, RobotsTxtView

urlpatterns = [
    path("robots.txt", RobotsTxtView.as_view(content_type="text/plain"), name="robots"),
    path("", HomePageView.as_view(), name="home"),
]
