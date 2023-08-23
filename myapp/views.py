from django.shortcuts import render
from django.http import JsonResponse

def test_rate_limit(request):
    return JsonResponse({"message": "Request successful!"})
