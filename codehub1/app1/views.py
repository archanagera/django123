#from#django.http import HttpResponse
from django.shortcuts import redirect, render
from django.template import loader

from app1.forms import ItemForm, ItemModelForm, NameForm
from .models import Item
from django.contrib.auth.decorators import login_required
from django.views.generic.list import ListView
# Create your views here.

class IndexClassView(ListView):
    model=Item
    template_name='app1/index.html'
    context_object_name='item_list'
    #queryset=Item.objects.filter(price=150)


@login_required
def index(request):
    item_list=Item.objects.all()
    print(item_list)
    context={'item_list':item_list}
    return render(request,'app1/index.html',context)
    #return HttpResponse("This is my first view function")

@login_required
def detail(request,item_id):
    it=Item.objects.get(pk=item_id)
    print(it)
    context={'it':it}

    return render(request,'app1/detail.html',context)


def fn1(request):
    data={'app':"food",
          'restaurant':"CCD"
          }
    return render(request,'app1/index2.html',data)

# def fn1(request):
#     return HttpResponse("second view")

def userform(request):
    data={}
    print("before submit")
    print("method is",request.method)
    if request.method == "POST":
        print("after submit")
        n1=request.POST.get('num1')
        n2=request.POST.get('num2')
        n3=int(n1) +int(n2)
        print("no1 is",n1)
        print("no2 is",n2)
        print("res is",n3)
        data={'n1':n1,
              'n2':n2,
              'n3':n3}

    return render(request,'app1/userform.html',data)

def nameForm(request):

    if request.method=="POST":
        form=NameForm(request.POST)

        name=request.POST.get('your_name')
        n1=request.POST.get('n1')
        n2=request.POST.get('n2')
        print(f"data from form is {n1} {n2} and {name}")

    else:
        form=NameForm()

    data={'form':form}

    return render(request,'app1/nameform.html',data)

def addItem(request):
    if(request.method=="POST"):
        form=ItemForm(request.POST)

        nm=request.POST.get('name')
        pr=request.POST.get('price')
        ds=request.POST.get('desc')
        im=request.POST.get('image')
        
        print(f"NAme: {nm} Price: {pr} Desc: {ds} Image:{im}")

        obj=Item(name=nm,price=pr,desc=ds,image=im)

        obj.save()

        return redirect('app1:index')
    
    else:
        form=ItemForm()
    data={'form':form}

    return render(request,'app1/Itemform.html',data)
    
       

def updateItem(request,item_id):
    item=Item.objects.get(id=item_id)
    print(item)
    form=ItemModelForm(request.POST or None,instance=item)
    if request.method=="POST":
        
        if form.is_valid:
            form.save()
            return redirect('app1:index')     

    return render(request,'app1/ItemForm.html',{'form':form})

def addItemModel(request):
    #form=ItemModelForm(request.POST or None)

    if request.method=="POST":
        form=ItemModelForm(request.POST)
        if(form.is_valid):
            form.save()
            return redirect('app1:index')
    else:
        form=ItemModelForm()
    
    data={'form':form}
    return render(request,'app1/ItemFormModel.html',data)
        