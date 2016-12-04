from django.conf.urls import url
from . import views
from django.conf.urls.static import static
from django.contrib import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from SE import settings

urlpatterns = [
	url(r'^$', views.index, name='index'),
	url(r'^instructor/$', views.instructor),
	url(r'^instructor/ins-course/(?P<course_id>\d+)/(?P<module_id>\d+)$', views.instructorcourse),
	url(r'^instructor/addcourse$', views.instructorcoursenew),
	url(r'^instructor/ins-course/addnewmodule/(?P<course_id>\d+)$',views.addnewModule),
	url(r'^instructor/ins-course/addcourse$',views.addnewCourse),
	url(r'^instructor/ins-course/(?P<module_id>\d+)/addcomponent$',views.addnewComponent),
	url(r'^instructor/ins-course/(?P<course_id>\d+)/editname$',views.editcoursename),
	url(r'^instructor/ins-course/(?P<course_id>\d+)/editdescription$',views.editcoursedesc),
	url(r'^instructor/ins-course/(?P<course_id>\d+)/editcat$',views.editcoursecat),
	url(r'^instructor/ins-course/(?P<module_id>\d+)/editmodule$',views.editmodule),
	url(r'^instructor/ins-course/(?P<component_id>\d+)/editcomponent$',views.editcomponent),
] 