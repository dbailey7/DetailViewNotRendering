from django.conf.urls import url;
from cmpbltrapp import views;

app_name = 'cmpbltrapp';  # Need this so we can ref, say, cmpbltrapp:list, etc in the templates

urlpatterns = [
    url(r'^$', views.index, name='index'), # Need name for same reason in templates
    url(r'^archetype_list/', views.mp_archetypeListView.as_view(), name='alist'), # Need name for same reason in templates
    url(r'^(?P<pk>\d+)/$', views.mp_archetypeDetailView.as_view(model='mp_archetype', template_name='cmpbltrapp/mp_archetype_detail.html'), name='mp_archetype-detail'),
    url(r'^mp_archetype_form/', views.mp_archetype_form_view, name='aform'), # Need name for same reason in templates
    url(r'^element_list/', views.mp_elementListView.as_view(), name='elist'), # Need name for same reason in templates
    url(r'^(?P<pk>\d+)/$', views.mp_elementDetailView.as_view(), name='edetail'), # Need name for same reason in templates
    url(r'^mp_element_form/', views.mp_element_form_view, name='eform'), # Need name for same reason in templates
];
