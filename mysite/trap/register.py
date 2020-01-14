from .models import Mouse,Relationship
from . import views
from . import validaters
from . import notify
from . import transfer

def register_error_handler(request):
        request.session['login_status'] = False
        return views.render_to_register(request)

def register_handler(request):
    if validaters.validate_uuid4(request.POST['uid']):
        try:
            init_currency = 100
            fee = 50
            sup_m = Mouse.objects.get(uid=request.POST['uid'])

            sub_m = Mouse(currency=init_currency)
            sub_m.save()

            request.session['uid'] = str(sub_m.uid)
            request.session['login_status'] = True

            r = Relationship(superior = sup_m,subordinate =sub_m)
            r.save()

            notify.register_init_handler(
            super = sup_m,
            sub = sub_m,
            init_currency = init_currency,
            fee = fee)

            transfer.transfer_handler(
            from_m = sub_m,
            to_m = sup_m,
            amount = fee)

            return views.redirect_to_index()

        except Mouse.DoesNotExist:
            return register_error_handler(request)

    else:
        return register_error_handler(request)
