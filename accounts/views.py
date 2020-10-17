from django.shortcuts import render,redirect
from django.contrib.auth.models import auth,User
from django.contrib import messages
# Create your views here.


def login(requests):
    if requests.method=="POST":
        username=requests.POST['username']
        password=requests.POST['password']
        user=auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(requests,user)
            return redirect("/")
        else:
            messages.info(requests,"Invalid credentials")
            return redirect('login')

    else:
        return render(requests,'login.html')


def logout(requests):
    auth.logout(requests)
    return redirect('/')



def register(requests):
    if requests.method=='POST':

        first_name=requests.POST['fname']
        last_name=requests.POST['lname']
        password1=requests.POST['password1']
        email=requests.POST['email']
        username=requests.POST['username']
        password2=requests.POST['password2']

        # Verification part

        if password1!=password2:
            messages.info(requests,"Password error")
            return redirect('register')
        elif User.objects.filter(username=username).exists():
            messages.info(requests,"Username already exists")
            return redirect('register')
        elif User.objects.filter(email=email).exists():
            messages.info(requests,"Email already exists")
            return redirect('register')

        user=User.objects.create_user(username=username,password=password1,first_name=first_name,last_name=last_name,email=email)
        user.save();

    return render(requests,'register.html')


    
