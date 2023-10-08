from django.urls import path
from . import views

urlpatterns = [
    path('independence/', views.display, name='display'),
]