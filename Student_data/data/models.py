from django.db import models
from django.core.exceptions import ValidationError




# Create your models here.
class Student(models.Model):
         Student_name = models.CharField(max_length=122)
         Reg_no = models.CharField(max_length=122)
         Address= models.CharField(max_length=122)
         Taluka = models.CharField(max_length=122)
         District = models.CharField(max_length=122)
         State = models.CharField(max_length=122)
         Photo = models.ImageField(upload_to="myimage")
         Pincode = models.IntegerField(max_length=6)
         def __str__(self):
             return self.Reg_no

def validiate_phone_no(value):
    if '1'|'2'|'3'|'4'|'5'|'6'|'7'|'8'|'9'|'0' in value and len(value)==10:
        return value
    else:
        raise ValidationError("Plz enter the valid mobile no.")

def validiate_college_email(value):
    if "@sggs.ac.in" in value:
        return value
    else:
        raise ValidationError("This field accepts mail id provided by SGGSIE&T college only")

class Admission(models.Model):
    Reg_no = models.ForeignKey(Student, blank=True,null=True, on_delete=models.CASCADE)
    Student_name = models.CharField( max_length=120)
    Branch = models.CharField( max_length=50)
    Class = models.CharField( max_length= 50)
    Date_of_admission = models.IntegerField (max_length= 20)
    Semester = models.CharField (max_length= 20)
    phoneno=models.CharField(max_length=10, validators=[validiate_phone_no])
    college_email = models.EmailField(max_length=25, validators=[validiate_college_email],default="nt@sggs.ac.in")

    def __str__(self):
	    return self.Student_name
  

class marks(models.Model):
    Reg_no = models.ForeignKey(Student, blank=True,null=True, on_delete=models.CASCADE)
    Student_name = models.CharField( max_length=120)
    Subject = models.CharField(max_length=122) 
    marks = models.IntegerField(max_length=122)
    Semester = models.CharField(max_length=122)
    Year = models.IntegerField(max_length=122)
    def __str__(self):
             return self.Student_name + ' ' + self.marks

class Feedback(models.Model):
    Reg_no = models.ForeignKey(Student, blank=True,null=True, on_delete=models.CASCADE)
    Student_name = models.CharField( max_length=120)
    Date=models.DateField()
    marks = models.ForeignKey(marks, blank=True,null=True, on_delete=models.CASCADE)
    Subject=models.CharField(max_length=122)
    Feedback=models.TextField()
    def __str__(self):
             return self.Student_name
         