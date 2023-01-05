from django.shortcuts import render

# Create your views here.
def hostelapp(request):
    return render(request,'index.html')