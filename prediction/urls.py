from django.urls import path
from . import views

urlpatterns = [
    path('dropout/', views.predict_dropout, name='dropout_prediction'),
]
