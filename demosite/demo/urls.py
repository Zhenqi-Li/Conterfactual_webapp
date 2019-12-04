from django.urls import path
from . import views

app_name = "demo"
urlpatterns = [
    path('', views.Dataset, name='Dataset'),
    path("Example_1", views.demo_table1, name='Example_1'),
    path("Example_2", views.demo_table2, name='Example_2'),
    path("Example_3", views.demo_table3, name='Example_3'),
]
