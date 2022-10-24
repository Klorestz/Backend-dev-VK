from django.http import JsonResponse
from django.views.decorators.http import require_http_methods

@require_http_methods(['POST'])
def create_user(request):
    data = [
        {"id_user" : 1, "name_of_user" : "Danila"}
    ]
    return JsonResponse({"create_user" : data})

@require_http_methods(['GET'])
def profile_user(request):
    data = [
        {"id_user" : 2, "name_of_user" : "Gleb"}
    ]
    return JsonResponse({"create_user" : data})
