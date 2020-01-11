from .models import Mouse,Relationship
from . import views
from . import validaters
from . import notify

def register_error_handler(request):
        request.session['login_status'] = False
        views.render_to_login(request)

def register_handler(request):
    if validaters.validate_uuid4(request.POST['uid']):
        try:
            sup_m = Mouse.objects.get(uid=request.POST['uid'])

            sub_m = Mouse(currency=100)
            sub_m.save()

            request.session['uid'] = str(sub_m.uid)
            request.session['login_status'] = True

            r = Relationship(superior = sup_m,subordinate =sub_m)
            r.save()
            notify.new_sub_notification(sup_m,sub_m)

            return views.redirect_to_index()

        except Mouse.DoesNotExist:
            register_error_handler(request)

    else:
        register_error_handler(request)
