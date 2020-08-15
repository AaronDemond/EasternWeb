from django.contrib import admin
from django.urls import path

from .views import getCandleData
from .views import __get_last_price as get_last_price 
from .views import index as home_page
from .views import insights
from .views import invest as invest_page
from .views import trades  as trades_page

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home_page, name='index'),
    #path('invest', invest_page, name='invest') need to update context
    path('trades', trades_page, name='trades'),
    path('insights', insights, name='insights'),
    path('i', insights, name='insights'),
    path('get-last-price', get_last_price, name='get_last_price'),
    path('get-candle-data', getCandleData)
]
