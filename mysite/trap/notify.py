from .models import Mouse,Relationship,Notification,Transaction
from . import validaters
from django.db.models import  Count

def notification_error_handler(request):
    #error happend
    pass

def create_notification(super,sub,message):
    n = Notification(
        receiver = super,
        creator = sub,
        context = message)
    n.save()

def new_sub_notification(super,sub):
    message = "hi %s, I am your new subordinate, my UID is %s." % (str(super.uid), str(sub.uid))
    create_notification(super,sub,message)

def new_sub_transaction_notification(super,sub,amount):
    message = "hi %s, your new subordinate, UID %s, give you %s currency." % (str(super.uid), str(sub.uid), str(amount))
    create_notification(super,sub,message)

def get_notifications(uid):
    notifications = Notification.objects.filter(receiver=uid)
    return notifications

def get_notification_num(uid):
    num = Notification.objects.filter(receiver=uid).count()
    return num

def del_all_notification(uid):
    Notification.objects.filter(receiver=uid).delete()
