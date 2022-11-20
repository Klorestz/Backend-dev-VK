from users.serializer import UserSerializer
from rest_framework.generics import ListAPIView
from users.models import User

class UserInfo(ListAPIView):
    serializer_class = UserSerializer

    def get_queryset(self):
        user_id = self.kwargs.get('user_id')
        return User.objects.filter(id=user_id)

