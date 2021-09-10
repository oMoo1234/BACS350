from django.views.generic import TemplateView


class MainPage(TemplateView):
    template_name = "main.html"


class CenaPage(TemplateView):
    template_name = "cena.html"


class SuperPage(TemplateView):
    template_name = "super.html"


class UndertakerPage(TemplateView):
    template_name = "undertaker.html"


class VirusPage(TemplateView):
    template_name = "virus.html"
