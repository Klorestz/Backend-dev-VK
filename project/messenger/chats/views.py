from django.shortcuts import render
from django.http import JsonResponse
from django.http import HttpResponse
from django.views.decorators.http import require_http_methods

def chats_list(request):
    if request.method == 'GET':
        data = [
            {"id_users" : 1, "names_of_chats" : ["Cat", "Dog"], "last_messages" : ["Meow", "Woof"]}
        ]
        return JsonResponse({"chats" : data})
    else:
        return HttpResponse(status=405)

@require_http_methods(['GET'])
def page_of_chat(request, chat_id):
    data = [
        {"id_chats" : chat_id, "name_of_chats" : "Cat", "Messages" : ["Meow", "Meow"]}
    ]
    return JsonResponse({"page_of_chat" : data})

@require_http_methods(['POST'])
def create_chat(request):
    data = [
        {"id_users" : 1, "id_chats" : 3, "name_of_chat" : "Cat"}
    ]
    return JsonResponse({"create_chat" : data})