
from django.urls import path
from . import views

urlpatterns = [
    path('', views.reminder_view, name='reminder_view'),
    path('create/', views.create_reminder, name='create_reminder'),
]
