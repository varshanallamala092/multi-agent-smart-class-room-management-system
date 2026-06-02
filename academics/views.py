from django.shortcuts import render

def academic_list(request):
    return render(request, 'academic_list.html')