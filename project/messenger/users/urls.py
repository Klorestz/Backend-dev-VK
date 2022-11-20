from django.urls import path
from users import views

urlpatterns = [
    path('profile_user/<int:user_id>/', views.profile_user, name = 'profile_user')
]