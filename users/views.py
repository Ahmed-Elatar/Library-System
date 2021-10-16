from django.shortcuts import render
from users.models import users
from books.models import books
from users.models import opinion
from django.http import HttpResponse

# Create your views here.




book = books.objects.all()
user=users.objects.all()
opo=opinion.objects.all()

flag=0
context = {"data": book, "case": flag}
context5={"books":book,"users":user,"opinions":opo}





# /////////////////////////////////////////  Login function ///////////////////////////////////////////

def login(request):
    global context

    if request.method == 'POST' :
        book = books.objects.all()



        flag=len(users.objects.all().filter(email=request.POST['email']))


        if flag>0:
            O=users.objects.filter(email=request.POST['email'])
            o=O[0]
            context = {"data": book, "user": o, "case": flag}
            if o.passcode == request.POST['passcode']:
                flag=1
            else:
                flag=0



        context2 = {"data": "Data"}

        if flag ==0:
            return render(request, 'users/login.html', context2)



        if flag ==1:

            return render(request, 'users/books.html', context)








    elif request.method =='GET':
        return render(request, 'users/login.html')








# ////////////////////////////////////// Register function ////////////////////////////////////


def register(request):
    context = {"data": "Data"}
    if request.method =="POST":
        n=users()
        n.name=request.POST['name']
        n.email = request.POST['email']
        n.nid=request.POST['nid']
        n.passcode = request.POST['passcode']
        if len( users.objects.all().filter(nid=request.POST['nid'])) == 0  and len( users.objects.all().filter(email=request.POST['email'])) == 0 and len( users.objects.all().filter(email=request.POST['name'])) == 0:
            n.save()

            return render(request, 'home/home.html')
        else:

            return render(request, 'users/register.html',context)

    elif request.method=="GET":
        return render(request,'users/register.html')



#////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////










def log_reg(request):

    Users =users.objects.all()







    context={"data":Users}
    # return HttpResponse(context)


    return render(request,'users/log-reg.html',context )



# ////////////////////////////////////////////////////////////////////


def borrow(request,id):
    data = books.objects.all().filter(id=id)
    n=data[0]
    n.status='borrowed'
    n.bookuser=context["user"].name
    n.status="borrowed"

    context3 = {"data": data}
    if request.method=='POST':
        n.save()
        context4=context
        return render(request, 'users/books.html', context4)
    elif request.method=='GET':
        return render(request,'users/borrow.html',context3)






# ///////////////////////////////////////////////////////////////////

def addbook(request):

    newbook=books()
    wrong={"wrong":"wrong"}
    if request.method=="POST":

         newbook.title=request.POST['title']
         newbook.description = request.POST['description']
         newbook.image = request.POST['image']
         newbook.cat = request.POST['cat']
         newbook.bookuser='none'
         newbook.status="Available"

         if len( books.objects.all().filter(title=request.POST['title'])) == 0:
             newbook.save()
             return render(request, 'users/adminview.html',context5)
         else:
            return render(request, 'users/addbook.html',wrong)



    elif request.method=='GET':
        return render(request, 'users/addbook.html')





# ///////////////////////////////////////////////////////////////
def loginadmin(request):
    wrong = {"req": "wrong"}

    if request.method=='POST':

        if request.POST['email']=='a7med.elatar55@gmail.com' and request.POST['passcode']=='123':


            return render(request, 'users/adminview.html',context5)
        else:

            return render(request, 'users/adminlogin.html',wrong)



    elif request.method=='GET':

        return render(request,'users/adminlogin.html')
