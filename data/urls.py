from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from . import views

urlpatterns = [
    url(r'^$', views.IndexView.as_view(template_name="data/index.html"), name='index'),
    #url(r'^data/sign_in/$', views.sign_in, name='sign_in'),
    #url(r'^data/sign_in/', views.UserView.as_view(),name="sign_in"),
    url(r'^data/sign_in/', views.sign_in, name='sign_in'),
    url(r'^data/login/', views.redirect,name="login"),
    #url(r'^data/create/$', views.UserView.as_view(), name='create'),
    url(r'^data/$', views.UserList.as_view(), name="user_view"),
    url(r'^data/(?P<pk>[0-9]+)/$', views.UserDetail.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)