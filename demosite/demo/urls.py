from django.urls import re_path, path
from . import views
import re
app_name = "demo"
urlpatterns = [
    path('', views.welcome, name='welcome'),
    path('attention_check', views.attention, name='attention_check'),
    path('exit',views.exit, name='exit'),
    re_path(r'^Example_1/(?P<testnum>\w+)/$', views.demo_table1, name='Example_1'),
    path("Survey", views.survey, name='Survey'),
    re_path(r'^Example_2/(?P<testnum>\w+)/$', views.demo_table2, name='Example_2'),
    re_path(r'^Example_3/(?P<testnum>\w+)/$', views.demo_table3, name='Example_3'),
]
