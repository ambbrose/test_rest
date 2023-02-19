from django.urls import path

from .views import HeroView

app_name = 'hero'

urlpatterns = [
    path('hero', HeroView.as_view(), name='hero_view')
]
