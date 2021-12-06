from django.contrib.auth import authenticate
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.contrib.auth import login as auth_login
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth import logout as auth_logout
from .forms import RegistrationForm



# Create your views here.
def Login(request):
    return render(request,'users/login.html',context={})

def Authenticate(request):
    username_str=request.POST.get('username') #to get the username from frontend
    encrypt_password=request.POST.get('password')

    print(username_str, encrypt_password)
    login_url='login'
    redirect_url='/home'
    if username_str and encrypt_password:
        username=username_str
        password=encrypt_password
        try:
            user=authenticate(username=username,password=password)#authenticate is a class to login, which will authenticate user by checking it into the backend
        except Exception as e:
            messages.error(request,'Wrong username/password')
            for message in messages:
                print(message)
            return HttpResponseRedirect(login_url)
        if user is not None:
            auth_login(request,user)
            request.session['username']=username
            return HttpResponseRedirect(redirect_url)
        else:
            messages.error(request,'Wrong username/password')
            return HttpResponseRedirect(login_url)
    else:
        messages.error(request,'Please enter username/password')
        return HttpResponseRedirect(login_url)

def LogOut(request):
    template_name='users/login.html'
    response=HttpResponseRedirect('/login')
    if request.user.is_authenticated:
        try:
            auth_logout(request)
            response.set_cookie('username',value='',max_age=1)
            return response
        except Exception as e:
            print(e)
            pass
        return render(request,template_name)


def SignUp(request):
    form=RegistrationForm()
    if request.method == "POST":
        signup_form=RegistrationForm(request.POST,request.FILES)
        if signup_form.is_valid():
            signup_form.save()
            messages.add_message(request,messages.SUCCESS,'user added successfully')
            return HttpResponseRedirect('/login')
        else:
            return HttpResponseRedirect('/signup')

    context={"form":form}
    print(context)
    return render(request,'users/signup.html',context)