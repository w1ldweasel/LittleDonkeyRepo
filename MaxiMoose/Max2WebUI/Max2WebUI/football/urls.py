from django.urls import path, re_path

from . import views

urlpatterns = [
    path('', views.football, name='football'),
    path('match', views.match, name='match'),
    path('nuts', views.nuts, name='nuts'),
]

