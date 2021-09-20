from django.urls import path
from hero.views import ThemePage, BrolyPage, BuuPage, FriezaPage, PicoloPage, PopoPage
from django.contrib import admin

urlpatterns = [
    # path("/admin/", admin.site.urls),
    path("", ThemePage.as_view()),
    path("broly", BrolyPage.as_view()),
    path("buu", BuuPage.as_view()),
    path("frieza", FriezaPage.as_view()),
    path("picolo", PicoloPage.as_view()),
    path("popo", PopoPage.as_view())


]
