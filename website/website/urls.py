from django.contrib import admin
from django.urls import path
from .views import index as home_page
from .views import about as about_page
from .views import shop as shop_page
from .views import contact as contact_page
from .views import account as account_page
from .views import invest as invest_page
from .views import invest2

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home_page, name='index'),
    path('about', about_page, name='about'),
    path('shop', shop_page, name='shop'),
    path('invest', invest_page, name='invest'),
    path('invest2', invest2, name='invest2'),
    path('contact', contact_page, name='contact'),
    path('account', account_page, name='account'),
    path('email_signup', home_page, name='index')

]
