from django.urls import path
from users import views

urlpatterns = [
    path('profile_user/', views.profile_user, name = 'profile_user')
]