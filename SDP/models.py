from django.db import models
from django.contrib.auth.models import User

# Create your models here.

# class Author(models.Model):
# 	name = models.CharField(max_length=200)



# class Article(models.Model):
# 	author = models.ForeignKey(Author, on_delete=models.CASCADE)
# 	title = models.CharField(max_length=200)
# 	content = models.TextField()
# 	tags = models.ManyToManyField(Tag)

class Category(models.Model):
	name = models.CharField(max_length=200)
	def __str__(self):
		return self.name

class Course(models.Model):
	name = models.CharField(max_length=200)
	course_detail = models.TextField()
	OPEN = 'OP'
	DRAFT = 'DR'
	CLOSED = 'CL'
	STATUS_CHOICES = (
		(OPEN, 'Open'),
		(DRAFT, 'Draft'),
		(CLOSED, 'Closed'),
	)
	status = models.CharField(
		max_length=2,
		choices = STATUS_CHOICES,
		default = DRAFT,
	)
	category = models.ForeignKey(Category) 
	instructor =  models.ForeignKey(User)
	def __str__(self):
		return self.name 

class Module(models.Model):
	name = models.CharField(max_length=200)
	sequence = models.IntegerField()
	course = models.ForeignKey(Course, on_delete=models.CASCADE)   

class Component(models.Model):
	name = models.CharField(max_length=200)
	TEXT = 'TX'
	IMAGE = 'IM'
	VIDEO = 'VD'
	FILE = 'FL'
	TYPE_CHOICES = (
		(TEXT, 'Text'),
		(IMAGE, 'Image'),
		(VIDEO, 'Video'),
	)
	typ = models.CharField(
		max_length=2,
		choices = TYPE_CHOICES,
		default = TEXT,
	)
	content = models.TextField()
	sequence = models.IntegerField()
	module = models.ForeignKey(Module, on_delete=models.CASCADE)

class CourseParticipantMap(models.Model):
	participant =  models.ForeignKey(User) 
	course =  models.ForeignKey(Course)
	progress = models.CharField(max_length=200)

