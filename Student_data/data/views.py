from django.shortcuts import render, HttpResponse
from datetime import datetime
from django.contrib import messages
from data.models import Admission
from data.models import Student
from data.models import marks
from data.models import Feedback
from django.shortcuts import render

def all_events(request):
    Admission_list= Admission.objects.all()
    return render(request,'event.html', 
    {'Admission_list': Admission_list})

def all_events2(request):
    Context = {}
    name = request.POST.get('name')
    Context['name'] = name
    Admission_list= Admission.objects.all()
    for x in Admission_list:
        if x.Student_name == name:
            Context['Reg_no']=x.Reg_no
            Context['Branch']=x.Branch
            Context['Class']=x.Class
            Context['Semester']=x.Semester
    Student_list= Student.objects.all()
    for x in Student_list:
        if x.Student_name == name:
            Context['Address']=x.Address
            Context['District']=x.District
            Context['State']=x.State
            Context['Photo']=x.Photo
            Context['Pincode']=x.Pincode
    Marks_list = marks.objects.all()
    # for x in Marks_list:
    #     if x.Student_name == name:
    #         Context['Subject']=x.Subject
    #         Context['marks']=x.marks
    #         Context['Semester']=x.Semester
    #         Context['Year']=x.Year
            
    return render(request,'event2.html', Context)


def index(request):
    return render(request, 'index.html')

def Student(request):
    if request.method == "POST":
        name = request.POST.get('name')
        reg_no = request.POST.get('reg_no')
        Address = request.POST.get('Address')
        Taluka = request.POST.get('Taluka')
        District = request.POST.get('District')
        State = request.POST.get('State')
        Photo = request.POST.get('Photo')
        Pincode = request.POST.get('Pincode')
        Student = Student(name=name, reg_no=reg_no, Address=Address, Taluka=Taluka, District=District, State=State, Photo=Photo, Pincode=Pincode ,date = datetime.today())
        Student.save()
        messages.success(request, 'Your message has been sent!')
    return render(request, 'Student.html')