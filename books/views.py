from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
from books.models import books








def bookspage(request):
    book=books.objects.all()








    context={"data":book}

    print(context)
    # return HttpResponse(context)
    return render(request,'books/books.html',context)


