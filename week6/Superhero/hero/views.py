from django.db import models
from django.db.models import fields
from django.views.generic import ListView, TemplateView, CreateView, UpdateView
from django.views.generic.edit import DeleteView
from .models import Hero
from django.urls import reverse_lazy


class IndexPage(TemplateView):
    model = Hero
    template_name = 'index.html'


class HeroListView(ListView):
    model = Hero
    template_name = 'hero_list.html'


class CreateHero(CreateView):
    model = Hero
    template_name = 'add_hero.html'
    fields = ["name", "description", "identity",
              "strength", "weakness", "image"]


class UpdateHero(UpdateView):
    template_name = "edit_hero.html"
    model = Hero
    fields = ["name", "description", "identity",
              "strength", "weakness", "image"]


class DeleteHero(DeleteView):
    model = Hero
    template_name = 'delete_hero.html'
    success_url = reverse_lazy('hero_list')


class HeroDetailView(TemplateView):
    model = Hero
    template_name = 'hero_detail.html'

    def get_context_data(self, **kwargs):
        hero_id = kwargs['pk']
        hero = Hero.objects.get(pk=hero_id)
        return {'hero': hero}
