from django.shortcuts import render

def dashboard_base(request):
    return render(request, "dashboard/base.html")
