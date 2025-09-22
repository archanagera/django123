from django import forms

from app1.models import Item

class NameForm(forms.Form):
    your_name = forms.CharField(label="Your name", max_length=100)
    n1=forms.IntegerField(label="num1")
    n2=forms.IntegerField(label="num2")

class ItemForm(forms.Form):
    name=forms.CharField(label="Name",max_length=100)
    price=forms.IntegerField(label="price")
    desc=forms.CharField(label="Description",max_length=200)
    image=forms.CharField(label="Image")

class ItemModelForm(forms.ModelForm):
    class Meta:
        model=Item
        #fields=["name","price","desc"]
        #exclude=["price"]
        fields='__all__'
        # widgets = {
        #     "name": forms.Textarea(attrs={"cols": 80, "rows": 20}),
        # }