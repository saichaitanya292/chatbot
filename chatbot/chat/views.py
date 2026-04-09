from django.http import JsonResponse
from django.shortcuts import render

# Create your views here.

def chatbot_response(user_input):
    user_input = user_input.lower()
    if user_input == 'hello':
        return 'Hi ! How can I help you?'
    elif user_input == 'hi':
        return 'I am django chatbot'
    else:
        return 'Bye'

def chat_view(request):
    return render(request, 'chat.html')

def get_response(request):
    user_message = request.GET.get('message')
    response = chatbot_response(user_message)
    return JsonResponse({'response': response})

