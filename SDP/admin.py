from django.contrib import admin

# Register your models here.
from .models import Course
from .models import Category
from .models import Module
from .models import Component
from .models import CourseParticipantMap

admin.site.register(Course)
admin.site.register(Category)
admin.site.register(Module)
admin.site.register(Component)
admin.site.register(CourseParticipantMap)