from django.urls import path

from justtodo import views

app_name='justtodo'

urlpatterns=[
  path('',views.index,name='index'),
  path('add',views.addTodo,name='add'),
  path('complete/<todo_id>/',views.completetodo,name='complete'),
  path('delete',views.deletecomplete,name='delete'),
  path('deleteall',views.deleteall,name='deleteall')
]