from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^home/', views.home, name='home_name'),
    url(r'^index/', views.index, name='index_name'),
    url(r'^list/(.+)/', views.list, name='list_name'),
    url(r'^skill/$', views.skill, name='skill_name'),
]