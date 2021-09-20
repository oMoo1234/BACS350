from django.urls import path
from hero.views import ThemePage, BrolyPage, BuuPage, FriezaPage, PicoloPage, PopoPage
from django.contrib import admin

urlpatterns = [
    # path("/admin/", admin.site.urls),
    path("hero/", ThemePage.as_view()),
    path("hero/broly", BrolyPage.as_view()),
    path("hero/buu", BuuPage.as_view()),
    path("hero/frieza", FriezaPage.as_view()),
    path("hero/picolo", PicoloPage.as_view()),
    path("hero/popo", PopoPage.as_view())


]
