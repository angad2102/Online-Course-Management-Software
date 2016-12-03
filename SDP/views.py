from django.shortcuts import render
from django.http import Http404
from django.shortcuts import render_to_response
from django.template import loader
from django.contrib.auth.models import User
from django.db import models
from .models import Course
from .models import Module
from .models import Category
from .models import Component
from django.shortcuts import get_object_or_404
from django.contrib.auth.models import User
# Create your views here.

from django.http import HttpResponse

def index(request):
	return HttpResponse("Hello, this is View: SDP.index")
#user =  Users.objects.get(pk=user_id)

def instructor(request):

	user = User.objects.get(pk=1)
	template = loader.get_template('instructor.html')
	courses = Course.objects.filter(instructor=user)
	for c in courses:
		if c.status == 'DR':
			c.status = "Draft"
		elif c.status == 'OP':
			c.status = "Open"
		elif c.status == 'CL': 
			c.status = "Closed" 
	context = {
		'courses': courses,
	}
	return HttpResponse(template.render(context, request))
	
def instructorcourse(request,course_id,module_id):

	course = Course.objects.get(pk=course_id)
	template = loader.get_template('instructor-course.html')
	if course.status == 'DR':
		course.status = "Draft"
	elif course.status == 'OP':
		course.status = "Open"
	elif course.status == 'CL': 
		course.status = "Closed"
	module = Module.objects.filter(course=course)
	module.order_by("sequence")

	module_pass = get_object_or_404(module,course=course_id,sequence=module_id)

	context = {
		'course': course,
		'modules':module,
		'components':Component.objects.filter(module=module_pass).order_by("sequence"),
		'cmodule':module_pass,	
	}
	return HttpResponse(template.render(context, request))

def instructorcoursenew(request):

	template = loader.get_template('instructor-course-new.html')

	cat = Category.objects.all()
	context = {
		'categories': cat,
	}
	return HttpResponse(template.render(context, request))
	