from django.urls import path

from .views import index_extrato

app_name = 'apps_extrato'
urlpatterns = [
    path('', index_extrato, name='home'),

]
