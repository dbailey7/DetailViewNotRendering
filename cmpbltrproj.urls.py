"""cmpbltrproj URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include;
from django.contrib import admin;
from cmpbltrapp import views;

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', views.IndexView.as_view(), name='index'),
    # url(r'^(?P<pk>[-\w]+)/$', views.mp_archetypeDetailView.as_view(), name='adetail'),
    # url(r'^mp_archetype_form/', views.mp_archetype_form_view, name='mp_archetype_form'),
    # url(r'^mp_element_form/', views.mp_element_form_view, name='mp_element_form'),
    url(r'^cmpbltrapp/', include('cmpbltrapp.urls', namespace='cmpbltrapp')),  # create mapping of app to url

];
