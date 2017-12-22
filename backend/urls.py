from django.conf.urls import url, include
from rest_framework.urlpatterns import format_suffix_patterns
from . import views

urlpatterns = [
    # url(r'^institutionUnits/$', views.InstitutionUnitList.as_view()),
    url(r'^main/$', views.main, name='main'),
    url(r'^institutionList/$', views.institution, name='institutionList'),
    url(r'^institution/(?P<pk>\d+)/$', views.institution_detail, name='institution_detail'),
    url(r'^institution/$', views.home, name='institution'),
    url(r'^register/$', views.register, name='register'),
    url(r'^login/$', views.login, name = 'login'),
    url(r'^logout/$', views.logout, name='logout'),


]
# urlpatterns = format_suffix_patterns(urlpatterns)
