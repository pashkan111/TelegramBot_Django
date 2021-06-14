from django.shortcuts import redirect, render
from .models import Advertisement, User
from django.db.models.functions import Lower
from .utils import sort_adv_list, check_time_5min, check_time_60min


def home(request):
    adv_list = sort_adv_list()
    first_created_element = adv_list.last()
    if check_time_60min(first_created_element) == False:
        sort_adv_list().delete()
    else:
        last_sales_price_element = adv_list.filter(sales_price__gt=0).first()
        if last_sales_price_element:
            if check_time_5min(last_sales_price_element) == False:
               adv_list = sort_adv_list()
            else:
                adv_list = Advertisement.objects.raw('(SELECT * FROM mainapp_advertisement WHERE sales_price>0 ORDER BY id DESC) UNION ALL (SELECT * FROM mainapp_advertisement WHERE sales_price is null ORDER BY id DESC)')
    return render(request, 'home.html', {'adv': adv_list})


def filter(request, condition):
    if condition:
        if condition == 'price':
            adv = Advertisement.objects.filter(sales_price__gt=0)
            return render(request, 'home.html', {'adv': adv})
    return home(request)