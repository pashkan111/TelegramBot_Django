from .models import *
def get_time_of_first_advert():
    a = Advertisement.objects.first()
    tim = a.created
    
