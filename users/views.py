from django.shortcuts import render

def users_base(request):
    return render(request, "users/base.html")
