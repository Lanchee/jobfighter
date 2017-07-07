from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^home/', views.home, name='home_name'),
    url(r'^index/', views.index, name='index_name'),
    url(r'^list/[a-zA-Z]+/$', views.list, name='list_name'),
]