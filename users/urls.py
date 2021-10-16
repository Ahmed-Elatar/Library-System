from django.urls import path
from users.views import login,register,log_reg,borrow,loginadmin,addbook

urlpatterns = [
    path('', log_reg),
    path('register/', register),
    path('login/', login),
    path('admin/', loginadmin),
    path('addbook', addbook),
    path("login/borrow/<id>", borrow),


]
