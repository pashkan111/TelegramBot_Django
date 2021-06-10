from django.urls import path
from .views import home, filter

urlpatterns = [
    path('home/', home, name='home'),
    path('filter/<str:id>', filter, name='filter'),
]
