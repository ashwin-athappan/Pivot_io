from django.urls import path
from . import views

urlpatterns = [
    path('', views.PreferencesView.as_view(), name='preferences'),
]
