from django.urls import path
from users import views

urlpatterns = [
    path('create_user/', views.create_user, name = 'create_user'),
    path('profile_user/', views.profile_user, name = 'profile_user')
]