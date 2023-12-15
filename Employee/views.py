from django.shortcuts import render
from rest_framework.decorators import api_view,permission_classes
from .serializer import UserSerializer
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .models import Employee
from .serializer import EmployeeSerializer
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
# Create your views here.

@api_view(http_method_names=['POST'])
def view_register(request):
    data={}
    if request.method=='POST':
        user_ser=UserSerializer(data=request.data)
        if user_ser.is_valid():
            u= user_ser.save()
            data['register']='User Register SuccessFully!!'
            data['username']=u.username
            t=Token.objects.get(user=u)
            data['token']=t.key
        else:
            data['error']=user_ser.errors
        return Response(data=data)

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def view_secure(request):
    return Response(data="This is my Secure page can access only when Token is provided")        

class EmployeeDetail(APIView):
    def get(self,request):
        obj = Employee.objects.all()
        serializer = EmployeeSerializer(obj, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def post(self, request):
        serializer = EmployeeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.data, status=status.HTTP_400_BAD_REQUEST)
    

class EmployeeInfo(APIView):
    def get(self, request, id):
        try:
            obj = Employee.objects.get(id=id)

        except Employee.DoesNotExist:
            msg = {"msg" : "not found"}
            return Response(msg, status=status.HTTP_404_NOT_FOUND)
        
        serializer = EmployeeSerializer(obj)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def put(self, request, id):
        try:
            obj = Employee.objects.get(id=id)

        except Employee.DoesNotExist:
            msg = {"msg" : "not found error"}
            return Response(msg, status=status.HTTP_404_NOT_FOUND)
        
        serializer = EmployeeSerializer(obj, data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_205_RESET_CONTENT)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def patch(self, request, id):
        try:
            obj = Employee.objects.get(id=id)

        except Employee.DoesNotExist:
            msg = {"msg" : "not found error"}
            return Response(msg, status=status.HTTP_404_NOT_FOUND)
        
        serializer = EmployeeSerializer(obj, data=request.data, partial=True)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_205_RESET_CONTENT)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, id):
        try:
            obj = Employee.objects.get(id=id)

        except Employee.DoesNotExist:
            msg = {"msg" : "not found"}
            return Response(msg, status=status.HTTP_404_NOT_FOUND)  

        obj.delete()
        return Response({"msg" : "deleted"}, status=status.HTTP_204_NO_CONTENT)  