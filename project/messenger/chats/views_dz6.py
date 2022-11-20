from django.shortcuts import render
from django.http import JsonResponse
from django.http import HttpResponse
from django.views.decorators.http import require_http_methods
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import get_object_or_404
from chats.models import Chat, Message, ChatMember
from users.models import User
import json

@require_http_methods(['GET'])
def chats_list(request, user_id):
    chats = []
    for chatmemeber in ChatMember.objects.filter(user=user_id):
        chats.append(
            {
                "title" : chatmemeber.chat.title,
                "description" : chatmemeber.chat.description,
            }
        )
    return JsonResponse({"chats_of_user" : chats})

@require_http_methods(['GET'])
def chat_detail(request, chat_id):
    chat = get_object_or_404(Chat, id=chat_id)
    users_of_chat = []
    chat_info = [{
        "id" : chat.id,
        "title" : chat.title,
        "description" : chat.description,
    }]
    for member in ChatMember.objects.filter(chat=chat_id):
        users_of_chat.append(
            {
             "first_name_of_user" : member.user.first_name,
             "last_name_of_user": member.user.last_name,
             "bio_of_user": member.user.bio,
             }
        )
    return JsonResponse({"chat_detail" : chat_info, "users_of_chat" : users_of_chat})

@csrf_exempt
@require_http_methods(['POST'])
def create_chat(request):
    title = request.POST.get('title')
    description = request.POST.get('description')
    created_chat = Chat.objects.create(title=title, description=description)
    created_chat.save()
    return JsonResponse({"is_created" : True})

@csrf_exempt
@require_http_methods(['PUT'])
def edit_chat(request):
    data = json.loads(request.body)
    edited_chat = get_object_or_404(Chat, id=data.get('id'))
    title = data.get('title')
    description = data.get('description')
    if title is not None:
        edited_chat.title = title
    if description is not None:
        edited_chat.description = description
    edited_chat.save()
    return JsonResponse({"is_edited" : True})

@csrf_exempt
@require_http_methods(['DELETE'])
def delete_chat(request, chat_id):
    deleted_chat = get_object_or_404(Chat, id=chat_id)
    deleted_chat.delete()
    return JsonResponse({"delete_chat" : True})

@csrf_exempt
@require_http_methods(['POST'])
def add_member(request):
    chat = get_object_or_404(Chat, id=request.POST.get('chat_id'))
    user = get_object_or_404(User, id=request.POST.get('user_id'))
    if ChatMember.objects.filter(user=user, chat=chat).exists():
        new_member = ChatMember.objects.create(chat=chat, user=user, role='Участник')
        new_member.save()
        return JsonResponse({"add_member" : True})
    else:
        return JsonResponse({"add_member" : "False, member alredy in chat"})

@csrf_exempt
@require_http_methods(['DELETE'])
def delete_member(request, chat_id, user_id):
    deleted_member = get_object_or_404(ChatMember, chat=chat_id, user=user_id)
    deleted_member.delete()
    return JsonResponse({"delete_member" : True})

@csrf_exempt
@require_http_methods(['POST'])
def create_message(request):
    chat = get_object_or_404(Chat, id=request.POST.get('chat_id'))
    user = get_object_or_404(User, id=request.POST.get('user_id'))
    content = request.POST.get('content')
    created_message = Message.objects.create(sender=user, chat=chat, content=content)
    created_message.save()
    return JsonResponse({"message_created" : True})

@csrf_exempt
@require_http_methods(['PUT'])
def edit_message(request):
    data = json.loads(request.body)
    edited_message = get_object_or_404(Message, id=data.get('id'))
    content = data.get('content')
    if content is not None:
        edited_message.content = content
        edited_message.save()
    return JsonResponse({"is_edited" : True})

@csrf_exempt
@require_http_methods(['PUT'])
def message_is_readen(request):
    data = json.loads(request.body)
    edited_message = get_object_or_404(Message, id=data.get('id'))
    edited_message.is_readen = True
    edited_message.save()
    return JsonResponse({"is_readen" : True})

@csrf_exempt
@require_http_methods(['DELETE'])
def delete_message(request, message_id):
    deleted_message = get_object_or_404(Message, id=message_id)
    deleted_message.delete()
    return JsonResponse({"delete_message" : True})

@require_http_methods(['GET'])
def list_of_messages(request, chat_id):
    messages = []
    for message in Message.objects.filter(chat=chat_id):
        messages.append(
            {
                "id" : message.id,
                "content" : message.content,
                "sender" : message.sender.id,
                "chat" : message.chat.id,
                "send_date" : message.send_date,
                "is_readen" : message.is_readen,
            }
        )
    return JsonResponse({"messages" : messages})