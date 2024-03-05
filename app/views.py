from django.shortcuts import render
from rest_framework.decorators import APIView
from app.models import *
from app.serializers import *
from rest_framework.response import Response

# Create your views here.

class StudentData(APIView):
    def get(self,request,id):
        SDO = Student.objects.all()
        JDO = StudentModalSerializer(SDO,many=True)
        # SDO = Student.objects.get(id=id)
        # JDO = StudentModalSerializer(SDO)
        return Response(JDO.data)
    
    def post(self,request,id):
        JSD = request.data
        PDO = StudentModalSerializer(data=JSD)
        if PDO.is_valid():
            PDO.save()
            return Response({'inserted':'inserted data successfully done'})
        else:
            return Response({'error':'Data is invalid'})
        
    def put(self,request,id):
        SD = Student.objects.get(id=id)
        JSDO = StudentModalSerializer(SD,data=request.data)
        if JSDO.is_valid():
            JSDO.save()
            return Response({'update':'Data updated successfully'})
        else:
            return Response({'error':'Data is invalid'})
        
    def patch(self,request,id):
        SD = Student.objects.get(id=id)
        JSDO = StudentModalSerializer(SD,data=request.data,partial=True)
        if JSDO.is_valid():
            JSDO.save()
            return Response({'update':'Data updated successfully'})
        else:
            return Response({'error':'Data is invalid'})
    
    def delete(self,request,id):
        Student.objects.get(id=id).delete()
        return Response({'Deleted':'data deleted successfully'})
