from django.shortcuts import render
from django.http import JsonResponse
from django.http import HttpResponse
from django.views.decorators.http import require_http_methods
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import get_object_or_404
from chats.models import Chat, Message
import json
@require_http_methods(['GET'])
def chats_list(request, user_id):
    chats = []
    for chat in Chat.objects.filter(users=user_id):
        chats.append(
             chat.__str__()
        )
    return JsonResponse({"chats_of_user" : chats})
@require_http_methods(['GET'])
def chat_detail(request, chat_id):
    chat = get_object_or_404(Chat, id=chat_id)
    chat_info = [{
        "id" : chat.id,
        "title" : chat.title,
        "description" : chat.description,
        "users" : str(chat.users.all())
    }]
    return JsonResponse({"chat_detail" : chat_info})

@csrf_exempt
@require_http_methods(['POST'])
def create_chat(request):
    data = json.loads(request.body)
    title = data['title']
    description = data['description']
    users = data['users']
    created_chat = Chat.objects.create(title=title, description=description)
    for user in users:
        created_chat.users.add(user)
    created_chat.save()
    return JsonResponse({"is_created" : True})

@csrf_exempt
@require_http_methods(['PUT'])
def edit_chat(request):
    data = json.loads(request.body)
    if data.get('id') is None:
        return JsonResponse({"is_edited" : False})
    edited_chat = get_object_or_404(Chat, id=data.get('id'))
    title = data.get('title')
    description = data.get('description')
    users = data.get('users')
    if title is not None:
        edited_chat.title = title
    if description is not None:
        edited_chat.description = description
    if users is not None:
        for user in users:
            edited_chat.users.add(user)
    edited_chat.save()
    return JsonResponse({"is_edited" : True})

@csrf_exempt
@require_http_methods(['DELETE'])
def delete_chat(request):
    data = json.loads(request.body)
    if data.get('id') is None:
        return JsonResponse({"is_deleted" : False})
    deleted_chat = get_object_or_404(Chat, id=data.get('id'))
    if deleted_chat is not None:
        deleted_chat.delete()
    return JsonResponse({"is_deleted" : True})