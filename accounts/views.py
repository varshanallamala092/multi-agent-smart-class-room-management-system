from django.shortcuts import render

def account_list(request):
    return render(request, 'accounts_List.html')