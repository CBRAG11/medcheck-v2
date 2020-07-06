# frontend/urls.py

from django.urls import path

from .views import index, MedDetailView
from . import views
urlpatterns = [
    path('', index, name='index'),
    path('edit/<int:pk>', MedDetailView.as_view()),
    path('delete/<int:pk>', views.deleteMed, name='delete'),
    path('predict', views.predict, name='predict'),
    path('custom-predict', views.customPrediction, name='custom-predict'),
]