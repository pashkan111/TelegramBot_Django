from django.shortcuts import render
from .models import Advertisement, User
import datetime
from django.utils.timezone import utc


now = datetime.datetime.utcnow().replace(tzinfo=utc)

def home(request):
    adv = Advertisement.objects.all().order_by('-created')
    last_adv = Advertisement.objects.last()
    created = last_adv.created   
    delta = now - created
    if delta.total_seconds() > 3600:
        Advertisement.objects.all().delete()
    return render(request, 'home.html', {'adv': adv})


# def put_adv_at_the_top(request):
#     last_adv = Advertisement.objects.last()
#     if last_adv.sales_price:
#         delta = now - last_adv.created
#         if delta