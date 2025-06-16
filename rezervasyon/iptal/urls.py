from django.urls import path
from . import views

app_name = 'iptal'

urlpatterns = [
    path('', views.iptal_basvuru_formu, name='form'),
    path('tesekkur_simple/<int:basvuru_id>/', views.tesekkur, name='tesekkur'),
    
]
