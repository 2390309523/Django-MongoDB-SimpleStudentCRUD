from django.urls import path
from . import views

urlpatterns = [
    path('',views.index,name="index"),
    path('deleteStudent/',views.deleteStudentById,name="deleteStudent"),
    path('updateStudent/',views.updateStudent,name="updateStudent"),
    path('createStudent/',views.createStudent,name="createStudent"),
    path('search/',views.index,name="search"),
    path('search/<str:keyword>/',views.search),
]