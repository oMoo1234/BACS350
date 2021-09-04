from django.urls import path
from hero.views import HulkView, IronmanView, BlackwidowView

urlpatterns = [
    path("hulk", HulkView.as_view()),
    path('ironman', IronmanView.as_view()),
    path('blackwidow', BlackwidowView.as_view()),
]
