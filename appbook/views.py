from django.shortcuts import render

# Create your views here.
from django.shortcuts import render

# Create your views here.


from django.shortcuts import render,get_object_or_404
from django.db.models import Q
from django.urls import reverse_lazy,reverse


from django.views.generic.list import ListView 

from .models import User

class UserListView(ListView):
    
    def get_queryset(self,*args,**kwargs):
        qs = User.objects.all()
        # print(self.request.GET) #/tweet/?q=Somesearch
        # query =self.request.GET.get("q",None)
        # if query is not None:
        #     qs = qs.filter(
        #         Q(content__icontains=query) #|
        #         # Q(user__username__icontains=query)
        #         )
        return qs