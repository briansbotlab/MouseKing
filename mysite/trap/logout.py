from uuid import UUID
from . import views

def del_login_session(request):
    del request.session['uid']
    del request.session['login_status']
    del request.session['notification_num']
    

def logout_handler(request):
    try:
        del_login_session(request)
    except KeyError:
        pass
    return views.redirect_to_index()
