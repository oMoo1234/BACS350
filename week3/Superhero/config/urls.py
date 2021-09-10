from django.urls import path
from hero.views import MainPage

urlpatterns = [
    path("", MainPage.as_view()),

]
