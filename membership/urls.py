from django.urls import path
from . import views

urlpatterns = [
    path('', views.membership, name='membership'),
    path('upload_form/', views.uploadMembershipForm, name='upload_form'),
]
