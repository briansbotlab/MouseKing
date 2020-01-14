from django.shortcuts import render

from django.http import HttpResponse
from .models import Mouse,Transaction
from django.shortcuts import redirect
from django.http import JsonResponse
from django.core import serializers
from django.db.models import Sum

import numpy as np
from . import login
from . import logout
from . import register
from . import notify
from . import chart

def redirect_to_index():
    return redirect('/')

def ajax_search_mouse(request):
    if request.method == 'GET':
        keyword = request.GET.get('keyword', None)
        if keyword != None:
            mouse_list = Mouse.objects.filter(uid__icontains=keyword).order_by('-currency')
            qs_json = serializers.serialize('json', mouse_list)
            return HttpResponse(qs_json, content_type='application/json')

def show_chart(request):
    x = Transaction.objects.values_list('create_at', flat=True)
    y = list(Transaction.objects.values_list('amount', flat=True))

    for i in range(len(y)):
        if i != 0:
            y[i] += y[i-1]

    buffer_value,content_type = chart.create_chart(
    request,
    x=x,
    y=y,
    x_label="Time",
    y_label="Currency",
    chart_title="The Cumulative Transaction Currency")

    return HttpResponse(buffer_value, content_type=content_type)

def render_to_login(request):
    return render(request, 'login.html')

def render_to_register(request):
    return render(request, 'register.html')

def index(request):
    mouse_list = Mouse.objects.all().order_by('-currency')
    if ('login_status'  in request.session) and (request.session['login_status']):
        request.session['notification_num'] = notify.get_notification_num(request.session['uid'])
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
    notify.del_all_notification(uid)
    return redirect_to_index()
