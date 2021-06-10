from django.shortcuts import redirect, render
from .models import Advertisement, User
import datetime
from django.utils.timezone import utc
from django.http import JsonResponse
from django.db.models.functions import Lower


now = datetime.datetime.utcnow().replace(tzinfo=utc)

def home(request):
    adv_list = Advertisement.objects.order_by('sales_price', '-created')
    try:
        last_adv = adv_list.first()
        created = last_adv.created
        delta = now - created
        if delta.total_seconds() > 3600:
            Advertisement.objects.all().delete()
        else:
            list_of_sales_price_adv = adv_list.filter(sales_price__gt=0).order_by('created')
            if list_of_sales_price_adv:
                last_element = list_of_sales_price_adv.last()
                created_last_element = last_element.created
                delta_last_element = now - created_last_element
                if delta_last_element.total_seconds() > 300:
                    adv_list=adv_list
                else:
                    adv_list=Advertisement.objects.order_by('sales_price','-created')
    except:
        ValueError('Список объявлений пуст')
    return render(request, 'home.html', {'adv': adv_list})



def filter1():
    adv_list=Advertisement.objects.order_by('-created')
    return adv_list

def filter2():
    adv_list=Advertisement.objects.order_by('-sales_price', '-created')
    return adv_list





def filter(request, id):
    if id:
        if id == 'price':
            adv = Advertisement.objects.filter(sales_price__gt=0)
            return render(request, 'home.html', {'adv': adv})
    return home(request)