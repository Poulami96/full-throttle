from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from rest_framework import generics 
from appbook.models import User
from .serializers import UserSerializer


class UserListAPIView(generics.ListAPIView):
    serializer_class = UserSerializer
    
    def get_queryset(self):
        return User.objects.all()
    def list(self, request):
        queryset = self.get_queryset()
        serializer = UserSerializer(queryset, many=True)
        print(serializer.data)
        data={"ok":"true",
              "members":serializer.data}
        return Response(data)
    