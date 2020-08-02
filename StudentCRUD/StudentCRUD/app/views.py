from django.db.models import Q
from django.shortcuts import render,HttpResponse

from .models import *
# Create your views here.

def index(request):
    students = Student.objects;
    return render(request,"index.html",{"students":students})

def deleteStudentById(request):
    if request.POST:
        id = int(request.POST.get("id"))
        Student.objects.filter(id=id).delete();
        return HttpResponse("ok")
    return HttpResponse("default")

def updateStudent(request):
    if request.POST:
        id = int(request.POST.get("id"))
        gender = request.POST.get("gender")
        name = request.POST.get("name")
        age = int(request.POST.get("age"))
        address = request.POST.get("address")
        student = Student.objects.get(id=id);
        if gender.strip():
            student.gender = gender
        if address.strip():
            student.address = address
        if age:
            student.age = age
        if name.strip():
            student.name = name;
        Student.objects.filter(id=id).update(gender=gender,name=name,age=age,address=address);
        return HttpResponse("ok")
    return HttpResponse("default")

def createStudent(request):
    if request.POST:
        gender = request.POST.get("gender")
        name = request.POST.get("name")
        age = int(request.POST.get("age"))
        address = request.POST.get("address")
        student = Student(gender=gender,name=name,age=age,address=address);
        student.save();
        return HttpResponse("ok")
    return HttpResponse("default")

def search(reqeust,keyword):
    students = Student.objects(Q(name__exists=keyword)|Q(address__exists =keyword)|Q(gender__exists=keyword))
    return render(reqeust,"index.html",{"students":students})