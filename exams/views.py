from django.shortcuts import render

def exam_list(request):
    return render(request, 'exams_List.html')