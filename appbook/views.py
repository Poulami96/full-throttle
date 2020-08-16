from django.shortcuts import render

# Create your views here.
from django.shortcuts import render

# Create your views here.

from django.shortcuts import render
from django.urls import reverse_lazy,reverse

from django.views.generic.list import ListView 

from .models import User

class UserListView(ListView):
    
    def get_queryset(self,*args,**kwargs):
        qs = User.objects.all()
        data = {
            "ok":"true",
            "members":qs
        }
        print(data)
        return data