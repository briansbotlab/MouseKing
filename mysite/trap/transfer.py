from .models import Mouse,Relationship,Notification,Transaction
from . import validaters
from django.db.models import  Count

def transaction_error_handler(request):
    #error happend
    pass

def transfer_currency(from_m,to_m,amount):
    from_m_o = Mouse.objects.get(uid=str(from_m.uid))
    to_m_o = Mouse.objects.get(uid=str(to_m.uid))
    if from_m_o.currency > amount:
        from_m_o.currency = from_m_o.currency - amount
        to_m_o.currency = to_m_o.currency + amount
        from_m_o.save()
        to_m_o.save()
    else:
        #do not have enough currency
        pass

def create_transaction(from_m,to_m,amount):
    t = Transaction(
        from_mouse = from_m,
        to_mouse = to_m,
        amount = amount)
    t.save()


def transfer_handler(from_m,to_m,amount):
    create_transaction(from_m = from_m,to_m = to_m,amount = amount)
    transfer_currency(from_m = from_m,to_m = to_m,amount = amount)
