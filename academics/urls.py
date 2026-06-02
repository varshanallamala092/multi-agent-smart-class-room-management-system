from django.urls import path
from . views import academic_list

urlpatterns = [
    path('', academic_list),
]