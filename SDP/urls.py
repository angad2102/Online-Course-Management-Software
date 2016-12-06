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
	url(r'^mycourse/(?P<course_id>[0-9]+)/module/(?P<module_id>[0-9]+)/$', views.mycourse, name='mycourse'),
	url(r'^history/(?P<course_id>[0-9]+)/module/(?P<module_id>[0-9]+)/$', views.history, name='history'),
	url(r'^enroll/(?P<course_id>[0-9]+)/$', views.enroll, name='enroll'),
	url(r'^drop/(?P<course_id>[0-9]+)/$', views.drop, name='drop'),
	url(r'^add/(?P<course_id>[0-9]+)/$', views.add, name='add'),
	url(r'^retake/(?P<course_id>[0-9]+)/$', views.retake, name='retake'),
	url(r'^finish/(?P<course_id>[0-9]+)/(?P<module_id>[0-9]+)/$', views.finish, name='finish'),
	url(r'^login', views.login_view, name="login" ),  
    url(r'^logout/$', views.logout_view, name="logout" ),  
    url(r'^hr/$', views.all_participants),
    url(r'^attemptlogin',views.attempt_login),  
    url(r'^login_incorrect',views.login_incorrect),
    url(r'^inst-course/delete/(?P<course_id>\d+)$', views.deleteCourse),
    url(r'^inst-course/publish/(?P<course_id>\d+)$', views.publishCourse),
    url(r'^inst-course/deletecomponent/(?P<c_id>\d+)$', views.deleteComponent),
    url(r'^inst-course/deletemodule/(?P<m_id>\d+)$', views.deleteModule),
    url(r'^instructor/ins-course/movemoddown/(?P<id>\d+)$', views.mdown),
    url(r'^instructor/ins-course/movemodup/(?P<id>\d+)$', views.mup),
    url(r'^instructor/ins-course/movecompup/(?P<id>\d+)$', views.cup),
    url(r'^instructor/ins-course/movecompdown/(?P<id>\d+)$', views.cdown),
    url(r'^administrator/$', views.administrator_view),
    url(r'^assigninstructor/(?P<username>\d+)/$', views.add_instructor_view),
    url(r'^register', views.register),
    url(r'^attemptregister',views.attmeptregister),
] 