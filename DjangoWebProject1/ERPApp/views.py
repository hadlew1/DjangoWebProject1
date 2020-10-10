from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime

def index(request):
        now = datetime.now()

        return render(request,"ERPApp/index.html", {
            'title' : "Test Program",
            'message' : "Hello Django!",
            'content' : " on " + now.strftime("%A, %d %B, %Y at %X")
        })
def about(request):
    return render(request, "ERPApp/about.html",{'title': "About Django App", 'content' : "Example Django app page"})


# Create your views here.
