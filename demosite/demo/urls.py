from django.urls import path
from . import views

app_name = "demo"
urlpatterns = [
    path('', views.welcome, name='welcome'),
    path('attention_check', views.attention, name='attention_check'),
    path('exit',views.exit, name='exit'),
    path("Example_1", views.demo_table1, name='Example_1'),
    path("Example_1_1", views.demo_table1_1, name='Example_1_1'),
    path("Example_1_2", views.demo_table1_2, name='Example_1_2'),
    path("Survey", views.survey, name='Survey'),
    path("Example_2", views.demo_table2, name='Example_2'),
    path("Example_3", views.demo_table3, name='Example_3'),
]
