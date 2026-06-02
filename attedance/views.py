from django.shortcuts import render

def attendance_list(request):
    return render(request, 'attendance_List.html')