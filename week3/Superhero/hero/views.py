from django.views.generic import TemplateView


class MainPage(TemplateView):
    template_name = "super.html"