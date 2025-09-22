from django.shortcuts import render

# Create your views here.
def fn1(request):
    context={'name':"uday"}
    return render(request,'app2/fn1.html',context)