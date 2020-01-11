from django.shortcuts import render

from django.http import HttpResponse
from .models import Mouse
from django.shortcuts import redirect
from django.http import JsonResponse
from django.core import serializers
import numpy as np
from . import login
from . import logout
from . import register
from . import notify
from . import chart

def ajax_search_mouse(request):
    if request.method == 'GET':
        keyword = request.GET.get('keyword', None)
        if keyword != None:
            mouse_list = Mouse.objects.filter(uid__icontains=keyword).order_by('-currency')
            qs_json = serializers.serialize('json', mouse_list)
            return HttpResponse(qs_json, content_type='application/json')



def show_chart(request):
    x = np.arange(0.0, 2.0, 0.01)
    y = np.sin(2*np.pi*x)
    buffer_value,content_type = chart.create_chart(
    request,
    x=x,
    y=y,
    x_label="Time",
    y_label="Currency",
    chart_title="Mouse Currency")

    return HttpResponse(buffer_value, content_type=content_type)

def redirect_to_index():
    return redirect('/')

def render_to_login(request):
    return render(request, 'login.html')

def render_to_register(request):
    return render(request, 'register.html')

def index(request):
    mouse_list = Mouse.objects.all().order_by('-currency')
    if ('login_status'  in request.session) and (request.session['login_status']):
        notification_list = notify.get_notifications(request.session['uid'])
        return render(request, 'index.html', {
            'mouse_list': mouse_list,
            'notification_list': notification_list,
        })
    else:
        return render(request, 'index.html', {
            'mouse_list': mouse_list,
        })


def login_view(request):
    if request.method == "POST":
        return login.login_handler(request)
    else:
        pass
    return render_to_login(request)

def logout_view(request):
    return logout.logout_handler(request)

def register_view(request):
    if request.method == "POST":
        return register.register_handler(request)
    else:
        pass
    return render_to_register(request)


def n_del_all(request):
    uid = request.session['uid']
    notify.del_all_notification()
    return redirect_to_index()
