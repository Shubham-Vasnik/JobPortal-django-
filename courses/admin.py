from django.contrib import admin

# Register your models here.
from courses.models import Course


admin.site.register(Course)