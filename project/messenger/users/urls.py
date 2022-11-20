from django.urls import path
from users.views import UserInfo

urlpatterns = [
    path('profile_user/<int:user_id>/', UserInfo.as_view(), name = 'profile_user')
]