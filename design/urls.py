from django.urls import path
from . import views

app_name = 'design'

urlpatterns = [

    path('', views.home, name='home'),
    path('item/<int:itemid>/', views.detail, name='detail'),
    path('add/', views.add_item, name='add_item'),
    path('update/<int:id>/', views.update, name='update'),
    path('delete/<int:id>/', views.delete, name='delete'),
]
