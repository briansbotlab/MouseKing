from .models import Mouse,Relationship,Notification,Transaction
from . import validaters
from django.db.models import  Count

def transaction_error_handler(request):
    #error happend
    pass

def transfer_currency(from,to,amount):
    from_m = Mouse.objects.get(uid=from)
    to_m = Mouse.objects.get(uid=to)
    if from_m.currency > amount:
        from_m.currency = from_m.currency - amount
        to_m.currency = to_m.currency + amount
        from_m.save()
        to_m.save()
    else:
        #do not have enough currency
        pass

def create_transaction(from,to,amount):
    t = Transaction(
        from_mouse = from,
        to_mouse = to,
        amount = amount)
    t.save()


def new_sub_profit(super,sub):
    amount = 10
    create_transaction(from = sub,to = super,amount = amount)
    transfer_currency(from = sub,to = super,amount = amount)
