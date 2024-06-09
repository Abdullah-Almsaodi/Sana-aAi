from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .inference import chatbot_response
import json

@csrf_exempt
def chat(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body.decode('utf-8'))
            message = data.get('message')
            if message:
                # Add your logic here to process the message
                response = 'This is a dummy response from the server.'
                return JsonResponse({'response': response})
            else:
                return JsonResponse({'error': 'Message parameter is missing.'}, status=400)
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=500)
    else:
        return JsonResponse({'error': 'Only POST requests are allowed for this endpoint.'}, status=405)




def chatbot_api_view(request):
    if request.method == 'POST':
        # Your logic to process the chatbot API request
        return JsonResponse({'response': 'This is a dummy response from the server.'})
    else:
        return JsonResponse({'error': 'Only POST requests are allowed for this endpoint.'}, status=405)
