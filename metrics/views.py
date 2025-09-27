from django.shortcuts import render

def metrics_base(request):
    return render(request, "metrics/base.html")
