from django.conf.urls import url, include
from rest_framework.urlpatterns import format_suffix_patterns
from . import views


urlpatterns = [

    url(r'^12/', views.CityListView.as_view()),
    url(r'^11/', views.FavoriteListOnlyView.as_view()),
    url(r'^10/(?P<pk>[0-9]+)/$', views.FavoriteDeleteView.as_view()),
    url(r'^9/(?P<pk>[0-9]+)/$', views.FavoriteAddView.as_view()),
    url(r'^8/(?P<pk>[0-9]+)/$', views.CommentDetailView.as_view()),
    # url(r'^8_5/(?P<pk>[0-9]+)/$/$', views.CommentListAll.as_view()),
    url(r'^7/(?P<ins_name>.+)/$', views.InstitutionSearchListView.as_view()),
    url(r'^6/', views.InstitutionListAllView.as_view()),
    url(r'^register/$', views.RegisterView.as_view(), name='rest_register'),
    url(r'^verify-email/$', views.VerifyEmailView.as_view(), name='rest_verify_email'),url(r'^account-confirm-email/(?P<key>[-:\w]+)/$', TemplateView.as_view(),
        name='account_confirm_email'),
    # url(r'^6/',
    # url(r'^5/', vie


    #以下為login
    # URLs that do not require a session or valid token
    url(r'^password/reset/$', views.PasswordResetView.as_view(),
        name='rest_password_reset'),
    url(r'^password/reset/confirm/$', views.PasswordResetConfirmView.as_view(),
        name='rest_password_reset_confirm'),
    url(r'^login/$', views.LoginView.as_view(), name='rest_login'),
    # URLs that require a user to be logged in with a valid session / token.
    url(r'^logout/$', views.LogoutView.as_view(), name='rest_logout'),
    url(r'^user/$', views.UserDetailsView.as_view(), name='rest_user_details'),
    url(r'^password/change/$', views.PasswordChangeView.as_view(),
        name='rest_password_change'),


]
