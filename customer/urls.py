from django.urls import path
from customer.views import CustomerSignup
from customer.views import CustomerLogin

urlpatterns = [
    path("",CustomerSignup.as_view()),
    path("login",CustomerLogin.as_view(), name="log-in"),
]