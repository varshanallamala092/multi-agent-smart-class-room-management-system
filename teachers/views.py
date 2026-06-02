from django.shortcuts import render

def teacher_list(request):
  return render(request, 'teacher_List.html')