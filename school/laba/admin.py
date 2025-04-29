from django.contrib import admin
from .models import StudentClass, Student


@admin.register(StudentClass)
class StudentClassAdmin(admin.ModelAdmin):
    pass

@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    pass