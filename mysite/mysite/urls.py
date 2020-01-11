"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import include, url
from django.contrib import admin
from trips.views import hello_world
from trap.views import index, login_view, logout_view, register_view, n_del_all, ajax_search_mouse, show_chart

urlpatterns = [
    url(r'^$', index),
    url(r'^show_chart/$', show_chart),
    url(r'^index/search/$', ajax_search_mouse),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^hello/$', hello_world),
    url(r'^login/$', login_view),
    url(r'^logout/$', logout_view),
    url(r'^register/$', register_view),
    url(r'^notification/delete/all/$', n_del_all),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
