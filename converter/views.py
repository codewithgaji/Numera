from django.shortcuts import render
from django.http import JsonResponse
from .word_converter import word_to_digits

def converter(request):
    word = request.GET.get('word', '').lower()                                                                                                                                          
    if not word:
        return JsonResponse({'error': "No word number provided"}, status=400)

    result = word_to_digits(word)
    if result is None:
        return JsonResponse({'error': 'Invalid word number provided'}, status=400)
    
    return JsonResponse({'digit': result})

def home(request):
    return render(request, "index.html")
