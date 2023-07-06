from django.shortcuts import render, HttpResponse,redirect
from myapp.models import RegisterUser
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login

# Create your views here.
def register(request):
    if (request.method=="POST"):
        name= request.POST.get("username")
        email= request.POST.get("email")
        password= request.POST.get("password")
        confirmPassword=request.POST.get("confirm-password")
        if password==confirmPassword:
            User.objects.create_user(username=name,email=email,password=password)
            
            messages.success(request,'User is successfully registered')
        else:
           messages.error(request,'Both password should be same')
    return render(request,"register.html")

def loginUser(request):
    
    if (request.method=="POST"):
        password=request.POST.get("password")
        username=request.POST.get("email")
        
        print(password,username)

        user= authenticate(username=username, password=password)
        if user is not None:
            login(request,user)
            return redirect("./home")
        else:
            messages.error(request,"Invalid username or password")


    # allData=RegisterUser.objects.all().values()

    # for data in allData:
    #     print(data['email'])
    #     print(data['password'])
    return render(request,"login.html")
def homePage(request):
    return render(request,"home.html")