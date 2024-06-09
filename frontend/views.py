import requests
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.http import JsonResponse

def chat(request):
    return render(request, 'chat.html')

# def get_response(request):
#      if request.method == 'POST':
#         message = request.POST.get('message')
#         if message:
#             # Make a POST request to the Flask chatbot API
#             response = requests.post('http://127.0.0.1:5000/api/chatbot', json={'message': message})
#             if response.status_code == 200:
#                 data = response.json()
#                 chatbot_response = data.get('response')
#                 return JsonResponse({'response': chatbot_response})

#             else:
#                 return JsonResponse({'error': 'Error from chatbot API'}, status=response.status_code)
#         else:
#             return JsonResponse({'error': 'Message parameter is missing.'}, status=400)
#     else:
#         return JsonResponse({'error': 'Only POST requests are allowed for this endpoint.'}, status=405)


def base(request):
    return render(request, 'base.html')

def signin(request):
    return render(request, 'signin.html')


def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('signin')  # Redirect to sign in page
    else:
        form = UserCreationForm()
    return render(request, 'frontend/signup.html', {'form': form})


# def logout(request):
#     auth.logout(request)
#     return render(request, 'logout.html')