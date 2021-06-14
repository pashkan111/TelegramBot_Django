from .models import *
import datetime
from django.utils.timezone import utc


now = datetime.datetime.utcnow().replace(tzinfo=utc)

def check_time_60min(first_created_element):
    created = first_created_element.created
    delta = now - created
    if delta.total_seconds() < 3600:
        return True
    else:
        return False


def check_time_5min(elem):
    created = elem.created
    delta = now - created
    if delta.total_seconds() < 300:
        return True
    else:
        return False


def sort_adv_list():
    adv_list = Advertisement.objects.order_by('-created')
    return adv_list
    
