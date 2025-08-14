from . import views
from django.urls import path

urlpatterns=[
    path('addTask/', views.addTask, name='addTask'),
    path('mark_as_done/<int:pk>/', views.mark_as_done, name="mark_as_done"),
    path('mark_as_undone/<int:pk>/', views.mark_as_undone, name="mark_as_undone"),
    path('update_task/<int:pk>/', views.update_task, name="update_task"),
    path('delete_task/<int:pk>/', views.delete_task, name="delete_task"),
    
]