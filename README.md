
🤖 Django Chatbot – Step-by-Step Guide


---

🚀 Step 1: Install Django

pip install django


---

📁 Step 2: Create Project

django-admin startproject chatbot_project
cd chatbot_project


---

📦 Step 3: Create App

python manage.py startapp chat


---

⚙️ Step 4: Register App

Open settings.py:

INSTALLED_APPS = [
    ...
    'chat',
]


---

🔗 Step 5: Configure URLs

➤ chatbot_project/urls.py

from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('chat.urls')),
]


---

➤ chat/urls.py (create this file)

from django.urls import path
from . import views

urlpatterns = [
    path('', views.chat_view, name='chat'),
    path('get/', views.get_response, name='get_response'),
]


---

🧠 Step 6: Create Chatbot Logic

➤ chat/views.py

from django.shortcuts import render
from django.http import JsonResponse

def chatbot_response(user_input):
    user_input = user_input.lower()

    if "hello" in user_input:
        return "Hi! How can I help you?"
    elif "hi" in user_input:
        return "I am a Django chatbot"
    elif "bye" in user_input:
        return "Goodbye!"
    else:
        return "Sorry, I didn't understand."

def chat_view(request):
    return render(request, 'chat.html')

def get_response(request):
    user_message = request.GET.get('message')
    response = chatbot_response(user_message)
    return JsonResponse({'response': response})


---

🎨 Step 7: Create Frontend

➤ Create folder:

chat/templates/

➤ Create file:

chat/templates/chat.html


---

➤ chat.html

<!DOCTYPE html>
<html>
<head>
    <title>Django Chatbot</title>

    <script>
        async function sendMessage() {
            let userInput = document.getElementById("userInput").value;

            let response = await fetch(`/get/?message=${encodeURIComponent(userInput)}`);
            let data = await response.json();

            let chatBox = document.getElementById("chatBox");

            chatBox.innerHTML += `<p><b>You:</b> ${userInput}</p>`;
            chatBox.innerHTML += `<p><b>Bot:</b> ${data.response}</p>`;

            document.getElementById("userInput").value = "";
        }
    </script>
</head>

<body>
    <h2>Django Chatbot</h2>

    <div id="chatBox" style="border:1px solid black; height:300px; overflow:auto;"></div>

    <input type="text" id="userInput" placeholder="Type message">
    <button onclick="sendMessage()">Send</button>
</body>
</html>


---

▶️ Step 8: Run Server

python manage.py runserver


---

🌐 Step 9: Open in Browser

http://127.0.0.1:8000/



⚠️ Common Errors (Important)

❌ 404 Error

✔ Check URL:

/get/?message=hello


---

❌ Variables not showing

✔ Use backticks:

`Hello ${userInput}`


---

❌ App not working

✔ Ensure:

'chat' in INSTALLED_APPS