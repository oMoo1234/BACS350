from django.urls import path
from hero.views import MainPage, SuperPage, CenaPage, UndertakerPage, VirusPage

urlpatterns = [
    path("", MainPage.as_view()),
    path("undertaker", UndertakerPage.as_view()),
    path("cena", CenaPage.as_view()),
    path("super", SuperPage.as_view()),
    path("virus", VirusPage.as_view())
]
