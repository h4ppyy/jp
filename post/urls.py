from django.urls import path
from . import views


urlpatterns = [
    path('', views.list, name='list'),
    path('post/<int:id>', views.post, name='post'),
    path('regist', views.regist, name='regist'),
    path('report', views.report, name='report'),
    path('delete', views.delete, name='delete'),
]
