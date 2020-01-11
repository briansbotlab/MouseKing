from .models import Mouse
from . import views
from . import validaters
from . import notify

def load_login_success_status(request,uid):
    request.session['uid'] = uid
    request.session['login_status'] = True
    request.session['notification_num'] = notify.get_notification_num(uid)

def login_error_handler(request):
        request.session['login_status'] = False
        return views.render_to_login(request)

def login_handler(request):
    if validaters.validate_uuid4(request.POST['uid']):
        try:
            m = Mouse.objects.get(uid=request.POST['uid'])
            uid = request.POST['uid']
            load_login_success_status(request,uid)

            return views.redirect_to_index()

        except Mouse.DoesNotExist:
            return login_error_handler(request)

    else:
        return login_error_handler(request)
