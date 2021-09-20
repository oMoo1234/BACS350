from django.views.generic import TemplateView


class ThemePage(TemplateView):
    template_name = "superhero_theme.html"


class BrolyPage(TemplateView):
    template_name = "broly.html"


class BuuPage(TemplateView):
    template_name = "buu.html"


class FriezaPage(TemplateView):
    template_name = "frieza.html"


class PicoloPage(TemplateView):
    template_name = "picolo.html"


class PopoPage(TemplateView):
    template_name = "popo.html"
