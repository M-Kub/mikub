from django.urls import path

from . import views

urlpatterns = [
    path('webblog/', views.cover, name='cover'),
]
