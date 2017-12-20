from django.conf.urls import url, include
from rest_framework.urlpatterns import format_suffix_patterns
from . import views

urlpatterns = [
    url(r'^institutionUnits/$', views.InstitutionUnitList.as_view()),
    url(r'^main/$', views.main, name='main'),
    url(r'^about/$', views.about, name='about'),

]
# urlpatterns = format_suffix_patterns(urlpatterns)
