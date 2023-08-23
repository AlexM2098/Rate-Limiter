from django.urls import path
from myapp import views

urlpatterns = [
    path('test/', views.test_endpoint, name='test_endpoint'),
    path('rate-limiter-demo/', views.rate_limiter_demo, name='rate_limiter_demo'),
    path('run-tests/', views.run_tests_view, name='run_tests'),
]
