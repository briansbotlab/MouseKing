from .models import Mouse,Relationship,Notification,Transaction
from . import validaters
from django.db.models import  Count

def notification_error_handler(request):
    #error happend
    pass

def create_notification(receiver,creator,context):
    n = Notification(
        receiver = receiver,
        creator = creator,
        context = context)
    n.save()

def new_sub_notification(super,sub):
    message = "hi %s, I am your new subordinate, my UID is %s." % (str(super.uid), str(sub.uid))
    create_notification(
    receiver = super,
    creator = sub,
    context = message)

def new_sub_transaction_notification(super,sub,amount):
    message = "hi %s, your new subordinate, UID %s, give you %s currency." % (str(super.uid), str(sub.uid), str(amount))
    create_notification(
    receiver = super,
    creator = sub,
    context = message)

def new_regiser_notification(super,sub,amount):
    message = "Welcome to join 'Mouse King',you had already gave your superior %s %s currency." %(str(super.uid), str(amount))
    create_notification(
    receiver = sub,
    creator = sub,
    context = message)

def new_regiser_init_currency_notification(sub,amount):
    message = "Welcome to join 'Mouse King',you got %s currency." %(str(amount))
    create_notification(
    receiver = sub,
    creator = sub,
    context = message)

def register_init_handler(super,sub,init_currency,fee):
    new_sub_notification(super,sub)
    new_regiser_init_currency_notification(sub,init_currency)
    new_regiser_notification(super,sub,fee)
    new_sub_transaction_notification(super,sub,fee)

def get_notifications(uid):
    notifications = Notification.objects.filter(receiver=uid)
    return notifications

def get_notification_num(uid):
    num = Notification.objects.filter(receiver=uid).count()
    return num

def del_all_notification(uid):
    Notification.objects.filter(receiver=uid).delete()
