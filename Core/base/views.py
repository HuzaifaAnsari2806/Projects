from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from .models import User
from .forms import UserForm 
from django.http import HttpResponse,Http404


# Create your views here.
def home(request):
    obj=User.objects.get(id=1)
    name=' name = ' + obj.name +'<br>'
    email='email = ' + obj.email 
    
    html_str=name  +  email
    
    return HttpResponse(html_str)

def new(request):
    user_list=User.objects.all()
    context={
        'user_list':user_list
    }
    
    return render(request,'first.html',context)

def route(request,slug=None):
    User_obj=None
    if slug is not None:
        try:
            User_obj=User.objects.get(slug=slug)
        except:
            raise Http404
    context={
        "objects":User_obj
    }
    return render(request,'routers.html',context)

def user_search_view(request):
    query=request.GET.get('q')
    # qs=User.objects.filter(lookups)
    qs=User.objects.search(query=query)
    context={
        "objects_list":qs
    }
    return render(request,'search.html',context)


@login_required
def user_create_view(request):
    form=UserForm(request.POST or None)
    context={
        "form":form
    }
    if form.is_valid():
        obj=form.save()
        context['form']=UserForm()
        # context['object']=obj
        # context['created']=True
    return render(request,'create.html',context=context)

def login_user(request):
    if request.method=="POST":
        username=request.POST.get('uname')
        password=request.POST.get('upass')
        user=authenticate(request,username=username,password=password)
        if user is None:
            context={"error":"Invalid credentials"}
            return render(request,'login.html',context)
        login(request,user)
        return redirect('/base')
    return render(request,'login.html',{})

def auth_login_user(request):
    if request.method=="POST":
        form=AuthenticationForm(request,data=request.POST)
        if form.is_valid():
            user=form.get_user()
            login(request,user)
            return redirect('/base')
    else:
        form=AuthenticationForm()
    context={
        "form":form
    }
    return render(request,'authlogin.html',context)

def logout_user(request):
    if request.method=="POST":
        logout(request)
        return redirect('/login')      
    return render(request,'logout.html',{})

def register_user(request):
    form = UserCreationForm(request.POST or None)
    
    if form.is_valid():
        obj=form.save()
        return redirect("/login")
    context={
        "form":form
    }
    return render(request,'register.html',context )

