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
    }]
    return JsonResponse({"chat_detail" : chat_info})

@csrf_exempt
@require_http_methods(['POST'])
def create_chat(request):
    data = json.loads(request.body)
    title = data.get('title')
    description = data.get('description')
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
def delete_chat(request):
    data = json.loads(request.body)
    deleted_chat = get_object_or_404(Chat, id=data.get('id'))
    if deleted_chat is not None:
        deleted_chat.delete()
        return JsonResponse({"delete_chat" : True})
    else:
        return JsonResponse({"delete_chat" : False})

@csrf_exempt
@require_http_methods(['POST'])
def add_member(request):
    data = json.loads(request.body)
    chat = get_object_or_404(Chat, id=data.get('chat_id'))
    user = get_object_or_404(User, id=data.get('user_id'))
    if ChatMember.objects.filter(user=user, chat=chat).first() is None:
        new_member = ChatMember.objects.create(chat=chat, user=user, role='Участник')
        new_member.save()
        return JsonResponse({"add_member" : True})
    else:
        return JsonResponse({"add_member" : "False, member alredy in chat"})

@csrf_exempt
@require_http_methods(['DELETE'])
def delete_member(request):
    data = json.loads(request.body)
    deleted_member = get_object_or_404(ChatMember, chat=data.get('chat_id'), user=data.get('user_id'))
    if deleted_member is not None:
        deleted_member.delete()
        return JsonResponse({"delete_member" : True})
    else:
        return JsonResponse({"delete_member" : False})
@csrf_exempt
@require_http_methods(['POST'])
def create_message(request):
    data = json.loads(request.body)
    chat = get_object_or_404(Chat, id=data.get('chat_id'))
    user = get_object_or_404(User, id=data.get('user_id'))
    content = data.get('content')
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
def delete_message(request):
    data = json.loads(request.body)
    deleted_message = get_object_or_404(Message, id=data.get('id'))
    if deleted_message is not None:
        deleted_message.delete()
        return JsonResponse({"delete_message" : True})
    else:
        return JsonResponse({"delete_message" : False})

@require_http_methods(['GET'])
def list_of_messages(request):
    data = json.loads(request.body)
    messages = []
    for message in Message.objects.filter(chat=data.get('chat_id')):
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