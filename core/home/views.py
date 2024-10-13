from django.shortcuts import render
from django.shortcuts import redirect
from django.http import HttpResponse
import datetime
# Create your views here.

isActive = True

programs = [
    'WAP to find the palindrome',
    'WAP to find the factorial',
    'WAP to find the prime numbers',
]

Student = {
    "student_name": "Zain Ashraf",
    "roll no": 225441,
    "email": "zain@zain.com",
}


date = datetime.datetime.now()
data = {
    "isActive": isActive,
    "students": Student,
    "programs": programs,
    "date": date
}


def home(request):
    # return HttpResponse('<h1 style="color:red">hey I am django server..</h1>')
    if request.method == 'POST':
        check = request.POST['check']
        
    return render(request, 'home/index.html')

def submit(request):
    pass
    # return redirect('/')


def dateFunc(request):
    return HttpResponse(f"this is time now: {date}")


def about(request):
    return render(request, "home/about.html")


def contact(request):
    return render(request, "home/contact.html")


def random(request):
    return render(request, 'home/random.html', data)
