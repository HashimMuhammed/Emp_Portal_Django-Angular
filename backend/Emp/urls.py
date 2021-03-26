
from django.conf.urls import url
from Emp import views
from django.conf.urls.static import static


urlpatterns = [
    url(r'^department/$', views.departmentApi),
    url(r'^department/([0-9]+)$', views.departmentApi),

    url(r'^employee/$', views.employeeApi),
    url(r'^employee/([0-9]+)$', views.employeeApi),

]
