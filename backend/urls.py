from django.conf.urls import url, include
from rest_framework.urlpatterns import format_suffix_patterns
from . import views

urlpatterns = [

    url(r'^12/', views.CityList.as_view()),
    url(r'^11/', views.FavoriteListOnly.as_view()),
    url(r'^10/(?P<pk>[0-9]+)/$', views.FavoriteDelete.as_view()),
    url(r'^9/(?P<pk>[0-9]+)/$', views.FavoriteAdd.as_view()),
    url(r'^8/(?P<pk>[0-9]+)/$', views.CommentDetail.as_view()),
    url(r'^7/(?P<ins_name>.+)/$', views.InstitutionSearchList.as_view()),
    url(r'^6/', views.InstitutionListAll.as_view()),
  
    # url(r'^7/',
    # url(r'^6/',
    # url(r'^5/', vie
   
    # url(r'^main/$', views.main, name='main'),
    # url(r'^institutionList/$', views.institution, name='institutionList'),
    # url(r'^institution/(?P<pk>\d+)/$', views.institution_detail, name='institution_detail'),
    # url(r'^institution/$', views.home, name='institution'),
    # url(r'^register/$', views.register, name='register'),
    # url(r'^login/$', views.login, name = 'login'),
    # url(r'^logout/$', views.logout, name='logout'),


]
# urlpatterns = format_suffix_patterns(urlpatterns)
