import os, sys
import django
from aiogram import executor
from config import *


proj = os.path.dirname(os.path.abspath('manage.py'))
sys.path.append(proj)
os.environ['DJANGO_SETTINGS_MODULE'] = 'test1.settings'
django.setup()

if __name__ == '__main__':
    from handlers import dp
    executor.start_polling(dp)


