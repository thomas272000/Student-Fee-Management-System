from django.contrib import admin
from .models import Student, FeeCategory, StudentFees

# Register your models here.


admin.site.register(Student)
admin.site.register(FeeCategory)
admin.site.register(StudentFees)