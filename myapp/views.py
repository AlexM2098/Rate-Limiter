from django.shortcuts import render
from django.http import JsonResponse
from subprocess import run, PIPE
from django.http import HttpResponse

def rate_limiter_demo(request):
    return JsonResponse({"message": "Test endpoint accessed."})

def run_tests_view(request):
    results = ""  # Default value for results

    if request.method == "POST":
        # Run the test and capture the output
        result = run(['python', 'manage.py', 'test', 'myapp.test_rate_limiter.RateLimiterTest'], capture_output=True, text=True)
        results = result.stdout + result.stderr

    return render(request, 'myapp/test_runner.html', {'results': results})


def test_endpoint(request):
    return HttpResponse("This is the test endpoint.")
