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
] 