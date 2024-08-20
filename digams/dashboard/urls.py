from django.urls import path
from . import views

urlpatterns = [
    path('', views.amr_dashboard, name='amr_dashboard'),
]
