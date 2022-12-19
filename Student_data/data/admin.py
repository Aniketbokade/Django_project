from django.contrib import admin
from data.models import Student
from data.models import Admission
from data.models import marks
from data.models import Feedback

# Register your models here.
admin.site.register(Student)
admin.site.register(marks)
admin.site.register(Admission)
admin.site.register(Feedback)