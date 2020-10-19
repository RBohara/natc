from django.urls import path
from . import views

urlpatterns = [
    path('', views.events, name='events'),
    path('<int:pk>/', views.event_details, name='event_details')
]
