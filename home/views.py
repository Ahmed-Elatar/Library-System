from django.http import HttpResponse
from django.shortcuts import render
from books.models import books
from users.models import users,opinion
# Create your views here.



def home(request):
    book = books.objects.all()
    Users=users.objects.all()
    context = {"data": book}



    if request.method=='GET':
        return render(request,'home/home.html',context)
    elif request.method=='POST':
        opin = opinion()
        opin.name=request.POST['name']
        opin.faculty = request.POST['faculty']
        opin.subject = request.POST['subject']
        opin.save()
        return render(request,'home/home.html',context)