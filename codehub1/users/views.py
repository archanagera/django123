from django.shortcuts import redirect, render
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from .forms import RegisterForm
# Create your views here.
def register(request):
    if(request.method=='POST'):
        #form=UserCreationForm(request.POST)
        form=RegisterForm(request.POST)
        print(request)
        if form.is_valid():
            username=form.cleaned_data.get('username')
            str=f"Welcome {username},Your Account is created successfully"
            print(str)
            form.save()
            messages.success(request,str)
            #return redirect('users:login')
            return redirect("app1:index")
    else:
        #form=UserCreationForm()
        form=RegisterForm()
    return render(request,'users/register.html',{'form':form})

 
def profile(request):
    return render(request,'users/profile.html')