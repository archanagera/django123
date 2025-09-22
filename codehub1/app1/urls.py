
from django.urls import path
from . import views
app_name='app1'#namespacing

urlpatterns = [
    #path('',views.index,name='index'),
    path('',views.IndexClassView.as_view(),name='index'),
    path('<int:item_id>/',views.detail,name='detail'),
    path('form',views.userform,name='userform'), 
    path('nameForm',views.nameForm,name='nameForm'),
    path('addItem',views.addItem,name='addItem'),
    path('addItemModel',views.addItemModel,name='addItemModel'),
    path('updateItem/<int:item_id>',views.updateItem,name='updateItem'),
]
