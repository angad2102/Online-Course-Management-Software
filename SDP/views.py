from django.shortcuts import render
from django.http import Http404
from django.shortcuts import render_to_response
from django.template import loader
from django.contrib.auth.models import User,Permission
from django.db import models
from .models import Course
from .models import Module
from .models import Category
from .models import Component
from .models import CourseParticipantMap
from django.shortcuts import get_object_or_404
from django.contrib.auth.models import User
from django.db.models import Max
from django.urls import reverse
from django.views import generic
from django.contrib.auth.models import User, Group
from django import forms  
from django.shortcuts import render, redirect
from django.contrib import auth 
from django.contrib.auth import authenticate, get_user_model, login,logout 
from .forms import UserLoginForm, UserRegisterForm
from django.contrib.auth import authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.contenttypes.models import ContentType


# Create your views here.

from django.http import HttpResponse,HttpResponseRedirect

from django.contrib.auth.decorators import permission_required





def login_view(request):
	template = loader.get_template('login.html')
	context = {
	}
	return HttpResponse(template.render(context, request))

def attempt_login(request):
	uname = request.POST.get('username')
	pwd = request.POST.get('pwd')
	user = authenticate(username=uname, password=pwd)
	if user is not None:
		login(request, user)
		URL = "/SDP/mycourse/0/module/0/"
		if user.has_perm('SDP.admin'):
			URL = "/SDP/administrator/"
		elif user.has_perm('SDP.instructor'):
			URL = "/SDP/instructor/"
	else:
		URL = "/SDP/login_incorrect"
	    # No backend authenticated the credentials

	return HttpResponseRedirect(URL)

def login_incorrect(request):
	template = loader.get_template('login_error.html')
	context = {
	}
	return HttpResponse(template.render(context, request))

@login_required(login_url='/SDP/login')
def all_participants(request):
	user = User.objects.filter(groups__name='Participant')
	return render(request, "hr.html", {"user" :user})
	
def logout_view(request):
	logout(request)
	return redirect('/SDP/login')

def index(request):
	return redirect('/SDP/login')
#user =  Users.objects.get(pk=user_id)

@login_required(login_url='/SDP/login')
@permission_required('SDP.instructor')
def instructor(request):

	user = request.user
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
	
@login_required(login_url='/SDP/login')
@permission_required('SDP.instructor')
def instructorcourse(request,course_id,module_id):

	course = Course.objects.get(pk=course_id)
	template = loader.get_template('instructor-course.html')
	if course.status == 'DR':
		course.status = "Draft"
	elif course.status == 'OP':
		course.status = "Open"
	elif course.status == 'CL': 
		course.status = "Closed"
	module = Module.objects.filter(course=course).order_by("sequence")
	
	print (module)
	
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

@login_required(login_url='/SDP/login')
@permission_required('SDP.instructor')
def instructorcoursenew(request):

	template = loader.get_template('instructor-course-new.html')

	cat = Category.objects.all()
	context = {
		'categories': cat,
	}
	return HttpResponse(template.render(context, request))

@login_required(login_url='/SDP/login')
@permission_required('SDP.instructor')
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

@login_required(login_url='/SDP/login')
@permission_required('SDP.instructor')
def addnewCourse(request):
	cname = request.POST.get('coursename')
	des = request.POST.get('description')
	cat = request.POST.get('cat')
	mname = request.POST.get('modulename')

	if((cname=="")and(mname=="")and(des=="")and(cat=="")):
			return HttpResponseRedirect('/SDP/instructor')

	course = Course(name=cname,course_detail=des,status='DR',category=Category.objects.get(pk=int(cat)),instructor=request.user)
	course.save()

	module = Module(name=mname,sequence=1,course=course)
	module.save()

	return HttpResponseRedirect('/SDP/instructor')

@login_required(login_url='/SDP/login')
@permission_required('SDP.instructor')
def addnewComponent(request,module_id):
	cname = request.POST.get('n-name')
	typ = request.POST.get('type')
	cont = request.POST.get('content')
	if typ == "VD":
		print("angad")
		cont = cont.replace("watch?v=", "v/")
	if((cname=="")and(typ=="")and(cont=="")):
			return HttpResponseRedirect('/SDP/instructor/ins-course/'+str(md.course.id)+'/1')

	md = Module.objects.get(pk=module_id)
	s = Component.objects.filter(module=md).aggregate(Max('sequence'))['sequence__max']
	if(not s):
		s=0
	component = Component(name=cname,typ=typ,module=md,content=cont,sequence=(s+1)) 
	component.save()

	return HttpResponseRedirect('/SDP/instructor/ins-course/'+str(md.course.id)+'/'+str(md.sequence))

@login_required(login_url='/SDP/login')
@permission_required('SDP.instructor')
def editcoursename(request,course_id):
	cname = request.POST.get('newCourseName')
	course = Course.objects.get(pk=course_id)
	course.name=cname
	course.save()
	return HttpResponseRedirect('/SDP/instructor/ins-course/'+str(course_id)+'/1')

@login_required(login_url='/SDP/login')
@permission_required('SDP.instructor')
def editcoursedesc(request,course_id):
	cname = request.POST.get('newCourseDesc')
	course = Course.objects.get(pk=course_id)
	course.course_detail = cname
	course.save()
	return HttpResponseRedirect('/SDP/instructor/ins-course/'+str(course_id)+'/1')

@login_required(login_url='/SDP/login')
@permission_required('SDP.instructor')
def editcoursecat(request,course_id):
	cname = request.POST.get('cat')
	course = Course.objects.get(pk=course_id)
	course.category = Category.objects.get(pk=int(cname))
	course.save()
	return HttpResponseRedirect('/SDP/instructor/ins-course/'+str(course_id)+'/1')

@login_required(login_url='/SDP/login')
@permission_required('SDP.instructor')
def editmodule(request,module_id):
	cname = request.POST.get('editModuleName')
	module = Module.objects.get(pk=module_id)
	module.name= cname
	module.save()
	return HttpResponseRedirect('/SDP/instructor/ins-course/'+str(module.course.id)+'/'+str(module.sequence))

@login_required(login_url='/SDP/login')
@permission_required('SDP.instructor')
def editcomponent(request,component_id):
	cname = request.POST.get('n')
	ccontent = request.POST.get('editcontent')
	component = Component.objects.get(pk=component_id)
	component.name=cname
	component.content = ccontent
	component.save()
	return HttpResponseRedirect('/SDP/instructor/ins-course/'+str(component.module.course.id)+'/'+str(component.module.sequence))
	
@login_required(login_url='/SDP/login')
def mycourse(request, course_id, module_id):
	template = loader.get_template('mycourse.html')
	user = request.user

	cpm = CourseParticipantMap.objects.filter(participant=user)
	if not cpm:
		return HttpResponse(template.render({}, request))
	cpm = CourseParticipantMap.objects.filter(participant=user).filter(progress__gt=-1)
	if not cpm:
		return HttpResponse(template.render({}, request))
	cpm = CourseParticipantMap.objects.filter(participant=user).get(progress__gt=-1)
	if course_id == "0":
		course_id = cpm.course.id
	mid = cpm.progress
	mm = Module.objects.filter(course = course_id).get(pk=mid)
	if module_id == "0":	
		module_id = Module.objects.filter(course=cpm.course).get(sequence=1).id
	try:
		c = Course.objects.get(pk=course_id)
	except c.DoesNotExist:
		raise Http404("Course does not exist")
	ms = Module.objects.filter(course=course_id).filter(sequence__lte=mm.sequence).order_by('sequence')
	try:
		m = Module.objects.filter(course=course_id).get(pk=module_id)
	except m.DoesNotExist:
		raise Http404("Module does not exist")
	co = Component.objects.filter(module=module_id).order_by('sequence')
	context = {
		'mycourse': c,
		'moduleset': ms,
		'module': m,
		'componentset': co,
	}
	return HttpResponse(template.render(context, request))

@login_required(login_url='/SDP/login')
def history(request, course_id, module_id):
	template = loader.get_template('history.html')
	user = request.user

	cpm = CourseParticipantMap.objects.filter(participant=user).filter(progress=-1).all()
	clist = []
	if not cpm:
		return HttpResponse(template.render({}, request))
	for ma in cpm:
		clist.append(ma.course.id)
	h = Course.objects.all().filter(pk__in=clist)
	if course_id == "0":
		return HttpResponse(template.render({'history': h,}, request))

	try:
		c = Course.objects.get(pk=course_id)
	except c.DoesNotExist:
		raise Http404("Course does not exist")
	ms = Module.objects.filter(course=course_id).order_by('sequence')
	try:
		m = Module.objects.filter(course=course_id).get(pk=module_id)
	except m.DoesNotExist:
		raise Http404("Module does not exist")
	co = Component.objects.filter(module=module_id).order_by('sequence')
	context = {
		'history': h,
		'course': c,
		'moduleset': ms,
		'module': m,
		'componentset': co,
	}
	return HttpResponse(template.render(context, request))

@login_required(login_url='/SDP/login')
def enroll(request, course_id):
	template = loader.get_template('enroll.html')
	e = Course.objects.all().filter(status='OP')

	if course_id == "0":
		return HttpResponse(template.render({'enroll': e,}, request))

	try:
		c = Course.objects.get(pk=course_id)
	except c.DoesNotExist:
		raise Http404("Course does not exist")
	context = {
		'enroll': e,
		'course': c,
	}
	return HttpResponse(template.render(context, request))

@login_required(login_url='/SDP/login')
def drop(request, course_id):
	#get user, need to modify this line
	user = request.user

	try:
		cpm = CourseParticipantMap.objects.filter(participant=user).get(course=Course.objects.get(pk=course_id))
	except cpm.DoesNotExist:
		return HttpResponse('You can not drop this course')
	if int(cpm.progress) > 0:
		cpm.delete()
	return HttpResponse('success')

@login_required(login_url='/SDP/login')
def add(request, course_id):
	#get user, need to modify this line
	user = request.user
	c = Course.objects.get(pk=course_id)
	cpm = CourseParticipantMap.objects.filter(progress__gt = -1).filter(participant=user)
	if not cpm:
		cpma = CourseParticipantMap.objects.filter(progress = -1).filter(course=c)
		if cpma:
			return HttpResponse('You have already completed this course')
		c = Course.objects.get(pk=course_id)
		m = Module.objects.filter(sequence=1).get(course=c)
		add = CourseParticipantMap(participant=user, course=c, progress=m.id)
		add.save()
		return HttpResponse('success')
	else:
		return HttpResponse('You can only enroll one course')

@login_required(login_url='/SDP/login')
def retake(request, course_id):
	#get user, need to modify this line
	user = request.user

	
	c = Course.objects.get(pk=course_id)
	cpm = CourseParticipantMap.objects.filter(course=c).get(participant=user)
	if c.status == 'CL':
		return HttpResponse('Sorry, this course is closed') 
	m = Module.objects.filter(sequence=1).get(course=c)
	cpm.progress=m.id
	cpm.save()
	return HttpResponse('success')

@login_required(login_url='/SDP/login')
def finish(request, course_id, module_id):
	user = request.user
	c = Course.objects.get(pk=course_id)
	cpm = CourseParticipantMap.objects.filter(course=c).get(participant=user)
	m = Module.objects.filter(course=c).get(pk=module_id)
	p = m.sequence+1
	mp = Module.objects.filter(course=c).filter(sequence=p)
	if not mp:
		cpm.progress = -1
		cpm.save()
		return HttpResponse('Finish')
	mp = Module.objects.filter(course=c).get(sequence=p)
	cpm.progress = mp.id
	cpm.save()
	return HttpResponse('success')

@login_required(login_url='/SDP/login')
@permission_required('SDP.instructor')
def deleteCourse(request,course_id):
	course = Course.objects.get(pk=course_id)
	course.delete()
	return HttpResponseRedirect('/SDP/instructor')

@login_required(login_url='/SDP/login')
@permission_required('SDP.instructor')
def publishCourse(request,course_id):
	course = Course.objects.get(pk=course_id)
	course.status = "OP"
	course.save()
	return HttpResponseRedirect('/SDP/instructor/ins-course/'+str(course_id)+'/1')

@login_required(login_url='/SDP/login')
@permission_required('SDP.instructor')
def deleteComponent(request,c_id):
	comp = Component.objects.get(pk=c_id)
	m = comp.module.sequence
	c = comp.module.course.id
	comp.delete()
	return HttpResponseRedirect('/SDP/instructor/ins-course/'+str(c)+'/'+str(m))

@login_required(login_url='/SDP/login')
@permission_required('SDP.instructor')
def deleteModule(request,m_id):
	
	mod = Module.objects.get(pk=m_id)
	c = mod.course.id
	modu = Module.objects.filter(course=mod.course)

	if mod.sequence == 1 and len(modu)>=2:
		m = Module.objects.get(pk=m_id)
		modules = sorted(map(int,Module.objects.filter(course=Module.objects.get(pk=m_id).course).order_by("sequence").values_list('sequence', flat=True)))
		mo = Module.objects.get(course=m.course,sequence=modules[1])
		se = mo.sequence
		mo.sequence = m.sequence
		mod.sequence = se 
		mo.save()

	if len(modu)>=2:
		mod.delete()
	return HttpResponseRedirect('/SDP/instructor/ins-course/'+str(c)+'/1')

@login_required(login_url='/SDP/login')
@permission_required('SDP.instructor')
def mup(request,id):
	m = Module.objects.get(pk=id)
	modules = sorted(map(int,Module.objects.filter(course=Module.objects.get(pk=id).course).values_list('sequence', flat=True)))
	f=0
	pos=len(modules)
	flag =1
	while flag and pos>0 and not f:
		pos = pos -1
		if modules[pos] < m.sequence and modules[pos] != m.sequence:
			flag=0
			f=1
		

	if f == 1:
		print("Angad")
		print(pos)
		mo = Module.objects.get(sequence=modules[pos],course=m.course)
		seq = m.sequence
		print (m.sequence)
		print (mo.sequence)
		m.sequence = mo.sequence
		mo.sequence = seq 
		m.save()
		mo.save()

	return HttpResponseRedirect('/SDP/instructor/ins-course/'+str(m.course.id)+'/'+str(m.sequence))

@login_required(login_url='/SDP/login')
@permission_required('SDP.instructor')
def mdown(request,id):
	m = Module.objects.get(pk=id)
	modules = sorted(map(int,Module.objects.filter(course=Module.objects.get(pk=id).course).values_list('sequence', flat=True)))
	f=0
	pos=-1
	flag =1
	while flag and pos<len(modules)-1 and not f:
		pos = pos +1
		if modules[pos] > m.sequence and modules[pos] != m.sequence:
			print(modules[pos])
			print(m.sequence)
			flag=0
			f=1
		

	if f == 1:
		print("Angad")
		print(pos)
		mo = Module.objects.get(sequence=modules[pos],course=m.course)
		seq = m.sequence
		print (m.sequence)
		print (mo.sequence)
		m.sequence = mo.sequence
		mo.sequence = seq 
		m.save()
		mo.save()

	return HttpResponseRedirect('/SDP/instructor/ins-course/'+str(m.course.id)+'/'+str(m.sequence))

@login_required(login_url='/SDP/login')
@permission_required('SDP.instructor')
def cup(request,id):
	c = Component.objects.get(pk=id)
	components = sorted(map(int,Component.objects.filter(module=Component.objects.get(pk=id).module).values_list('sequence', flat=True)))
	f=0
	pos=len(components)
	flag =1
	while flag and pos>0 and not f:
		pos = pos -1
		if components[pos] < c.sequence and components[pos] != c.sequence:
			flag=0
			f=1
		

	if f == 1:
		print("Angad")
		print(pos)
		co = Component.objects.get(sequence=components[pos],module=c.module)
		seq = c.sequence
		c.sequence = co.sequence
		co.sequence = seq 
		c.save()
		co.save()

	return HttpResponseRedirect('/SDP/instructor/ins-course/'+str(c.module.course.id)+'/'+str(c.module.sequence))

@login_required(login_url='/SDP/login')
@permission_required('SDP.instructor')
def cdown(request,id):
	c = Component.objects.get(pk=id)
	components = sorted(map(int,Component.objects.filter(module=Component.objects.get(pk=id).module).values_list('sequence', flat=True)))
	f=0
	pos=-1
	flag =1
	while flag and pos<len(components)-1 and not f:
		pos = pos +1
		if components[pos] > c.sequence and components[pos] != c.sequence:
			flag=0
			f=1
	if f == 1:
		co = Component.objects.get(sequence=components[pos],module=c.module)
		seq = c.sequence
		c.sequence = co.sequence
		co.sequence = seq 
		c.save()
		co.save()

	return HttpResponseRedirect('/SDP/instructor/ins-course/'+str(c.module.course.id)+'/'+str(c.module.sequence))

@login_required(login_url='/SDP/login')
@permission_required('SDP.admin')
def administrator_view(request):
	users = User.objects.all()
	for u in users: 
		if u.has_perm("SDP.instructor"):
			u.ins =1
	return render(request, "admin.html", {"users":users})

@login_required(login_url='/SDP/login')
@permission_required('SDP.admin')
def add_instructor_view(request, username):
	permission = Permission.objects.get(codename='instructor')
	#permission = Permission.objects.get(codename='instructor') 
	user = User.objects.get(pk=username)
	user.user_permissions.add(permission) 
	return redirect('/SDP/administrator')

def attmeptregister(request):
	u = request.POST.get('username')
	pwd = request.POST.get('pwd')

	user = User.objects.create_user(username=u,
                                 password=pwd)
	user.save()
	login(request,user)
	return redirect('/SDP/mycourse/0/module/0')

def register(request):
	template = loader.get_template('register.html')
	context = {
	}
	return HttpResponse(template.render(context, request))
# def all_participants(request):
# 	user = User.objects.filter(groups__name='Participant')
# 	return render(request, "hr.html", {"user" :user})
