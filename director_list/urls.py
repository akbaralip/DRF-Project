from tkinter.font import names

from django.urls import path
from . views import DirecotorList
urlpatterns = [
    path('', DirecotorList.as_view(), name='director-list'),
]