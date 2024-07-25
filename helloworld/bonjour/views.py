from django.shortcuts import render

def salutation(request):
    return render(request,'bonjour.html')
