from django.db import models
from django.views.generic import ListView, TemplateView
from .models import Hero


class IndexPage(TemplateView):
    model = Hero
    template_name = 'index.html'


class HeroListView(ListView):
    model = Hero
    template_name = 'hero_list.html'


class HeroDetailView(TemplateView):
    model = Hero
    template_name = 'hero_detail.html'

    def get_context_data(self, **kwargs):
        hero_id = kwargs['pk']
        hero = Hero.objects.get(pk=hero_id)
        return {'hero': hero}
