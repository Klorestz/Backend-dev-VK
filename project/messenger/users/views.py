from django.http import JsonResponse
from django.views.decorators.http import require_http_methods
import json
from django.shortcuts import get_object_or_404
from users.models import User

@require_http_methods(['GET'])
def profile_user(request):
    data = json.loads(request.body)
    user = get_object_or_404(User, id=data.get('id'))
    user_info = [
        {
            "id" : user.id,
            "first_name" : user.first_name,
            "last_name" : user.last_name,
            "bio" : user.bio,
            "birthday" : user.birthday,
            "status" : user.is_online,
            "last_visited" : user.last_visited,
        }
    ]
    return JsonResponse({"user_info" : user_info})
