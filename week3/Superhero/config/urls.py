from django.urls import path
from hero.views import MainPage, SuperPage, CenaPage, UndertakerPage

urlpatterns = [
    path("", MainPage.as_view()),
    path("undertaker.html", UndertakerPage.as_view()),
    path("cena.html", CenaPage.as_view()),
    path("super.html", SuperPage.as_view()),

]
