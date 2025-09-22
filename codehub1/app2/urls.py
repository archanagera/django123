
from django.urls import path
from . import views


urlpatterns = [
    path('',views.fn1,name='index'),
    path('detail/',views.fn1,name='detail'),
    #path('index/',views.fn1),
]