from django.contrib import admin

# Register your models here.
from .models import Course,CourseResource,Lesson,Video

admin.site.register(Course)
admin.site.register(CourseResource)
admin.site.register(Lesson)
admin.site.register(Video)