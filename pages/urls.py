from django.urls import path
from . import views

urlpatterns = [
    path('',views.Index,name='index'),
    path('HomePage',views.HomePage,name='HomePage'),
    path('Login',views.Login,name='Login'),
    path('Logout',views.LogoutPage,name='Logout'),
    path('Student',views.StudentPage,name='Student'),
    path('AddStudent',views.AddStudent,name='AddStudent'),
    path('EditStudent/<str:Id>/',views.EditStudent,name='EditStudent'),
    path('updateStudent/<str:Id>/',views.UpdateStudent,name='updateStudent'),
    path('Active',views.ActivePage,name='active'),
    path('Course',views.Course,name='Course'),
    path('AddCourse',views.AddCourse,name='AddCourse'),
    path('EditCourse/<int:Id>/',views.EditCourse,name='EditCourse'),
    path('updateCourse/<str:Id>/',views.UpdateCourse,name='updateCourse'),
    path('RegisterCourse/<str:Id>/',views.RegPage,name='RegisterCourse'),
    path('RegCourse/<str:Id>/',views.RegCourse,name='RegCourse'),
    path('deleteStudent/<str:Id>/',views.deleteStudent,name='deleteStudent'),
    path('deleteCourse/<str:Id>/',views.deleteCourse,name='deleteCourse'),

]
