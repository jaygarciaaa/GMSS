from django.shortcuts import render

def memberships_base(request):
    return render(request, "dashboard/base.html")
