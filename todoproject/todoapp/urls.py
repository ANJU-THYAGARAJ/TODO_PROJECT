from . import views
from django.urls import path
urlpatterns = [
    path('',views.index,name='index'),
    path('delete/<int:taskid>/',views.delete,name="delete"),
    path('update/<int:id>/',views.update,name="update"),
    path('classbvhome/',views.TaskListView.as_view(),name='classbvhome'),
    path('cvdetail/<int:pk>/',views.TaskDetailView.as_view(),name='cvdetail'),
    path('cbvupdate/,int:pk>/',views.TaskUpdateView.as_view(),name='cbvupdate'),
    path('cbvdelete/<int:pk>/',views.TaskDeleteView.as_view(),name='cbvdelete'),
]
