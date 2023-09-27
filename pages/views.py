from django.views.generic.base import TemplateView


class RobotsTxtView(TemplateView):
    template_name = "robots.txt"


class HomePageView(TemplateView):
    template_name = "home.html"
