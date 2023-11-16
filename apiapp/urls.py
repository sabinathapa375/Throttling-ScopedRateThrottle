from django.urls import path, include
from apiapp import views

urlpatterns = [
    path('studentapi/', views.StudentList.as_view(), name='studentapi'),
    path('createstudent/', views.StudentCreate.as_view(), name='createstudent'),
    path('retrievestudent/<int:pk>/', views.StudentRetrive.as_view(), name='retrievestudent'),
    path('updatestudent/<int:pk>/', views.StudentUpdate.as_view(), name='updatestudent'),
    path('deletestudent/<int:pk>/', views.StudentDelete.as_view(), name='deletestudent'),
]
