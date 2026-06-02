from django.urls import path
from . views import account_list

urlpatterns = [
    path('', account_list),
]