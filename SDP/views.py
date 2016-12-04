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
from django.db.models import Max
# Create your views here.

from django.http import HttpResponse,HttpResponseRedirect

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

	
	cat = Category.objects.all()
	module_pass = get_object_or_404(module,course=course_id,sequence=module_id)
	comp = Component.objects.filter(module=module_pass).order_by("sequence")
	for c in comp:
		if c.typ == "VD":
			c.typ = "Video"
		elif c.typ == "IM":
			c.typ = "Image"
		elif c.typ == "TX":
			c.typ = "Text"
		elif c.typ == "FL":
			c.typ = "File"
	context = {
		'course': course,
		'modules':module,
		'components':comp,
		'cmodule':module_pass,	
		'categories': cat,

	}
	return HttpResponse(template.render(context, request))

def instructorcoursenew(request):

	template = loader.get_template('instructor-course-new.html')

	cat = Category.objects.all()
	context = {
		'categories': cat,
	}
	return HttpResponse(template.render(context, request))

def addnewModule(request,course_id):

		post_text = request.POST.get('add-module-name')
		if(post_text==""):
			return HttpResponseRedirect('/SDP/instructor/ins-course/'+str(course_id)+'/1')
		post_id = course_id
		response_data = {}
		args = Module.objects.filter(course=Course.objects.get(pk=post_id))
		# Calculates the maximum out of the already-retrieved objects
		s = Module.objects.filter(course=Course.objects.get(pk=post_id)).aggregate(Max('sequence'))['sequence__max']
		sec = s+1
		module = Module(name=post_text, course=Course.objects.get(pk=post_id), sequence=sec)
		module.save()

		return HttpResponseRedirect('/SDP/instructor/ins-course/'+str(course_id)+'/'+str(module.sequence))

def addnewCourse(request):
	cname = request.POST.get('coursename')
	des = request.POST.get('description')
	cat = request.POST.get('cat')
	mname = request.POST.get('modulename')

	if((cname=="")and(mname=="")and(des=="")and(cat=="")):
			return HttpResponseRedirect('/SDP/instructor')

	course = Course(name=cname,course_detail=des,status='DR',category=Category.objects.get(pk=int(cat)),instructor=User.objects.get(pk=1))
	course.save()

	module = Module(name=mname,sequence=1,course=course)
	module.save()

	return HttpResponseRedirect('/SDP/instructor')

def addnewComponent(request,module_id):
	cname = request.POST.get('n-name')
	typ = request.POST.get('type')
	cont = request.POST.get('content')

	if((cname=="")and(typ=="")and(cont=="")):
			return HttpResponseRedirect('/SDP/instructor/ins-course/'+str(md.course.id)+'/1')

	md = Module.objects.get(pk=module_id)
	s = Component.objects.filter(module=md).aggregate(Max('sequence'))['sequence__max']
	if(not s):
		s=0
	component = Component(name=cname,typ=typ,module=md,content=cont,sequence=(s+1)) 
	component.save()

	return HttpResponseRedirect('/SDP/instructor/ins-course/'+str(md.course.id)+'/'+str(md.sequence))

def editcoursename(request,course_id):
	cname = request.POST.get('newCourseName')
	course = Course.objects.get(pk=course_id)
	course.name=cname
	course.save()
	return HttpResponseRedirect('/SDP/instructor/ins-course/'+str(course_id)+'/1')

def editcoursedesc(request,course_id):
	cname = request.POST.get('newCourseDesc')
	course = Course.objects.get(pk=course_id)
	course.course_detail = cname
	course.name=cname
	course.save()
	return HttpResponseRedirect('/SDP/instructor/ins-course/'+str(course_id)+'/1')

def editcoursecat(request,course_id):
	cname = request.POST.get('cat')
	course = Course.objects.get(pk=course_id)
	course.category = Category.objects.get(pk=int(cname))
	course.save()
	return HttpResponseRedirect('/SDP/instructor/ins-course/'+str(course_id)+'/1')

def editmodule(request,module_id):
	cname = request.POST.get('editModuleName')
	module = Module.objects.get(pk=module_id)
	module.name= cname
	module.save()
	return HttpResponseRedirect('/SDP/instructor/ins-course/'+str(module.course.id)+'/'+str(module.sequence))


def editcomponent(request,component_id):
	cname = request.POST.get('n')
	ccontent = request.POST.get('editcontent')
	component = Component.objects.get(pk=component_id)
	component.name=cname
	component.content = ccontent
	component.save()
	return HttpResponseRedirect('/SDP/instructor/ins-course/'+str(component.module.course.id)+'/'+str(component.module.sequence))
	
