from django.urls import path
from . import views

application = 'regserve'

#to start, hit play on "Run and Debug on left hand tabs"

urlpatterns = [
    #Can be accessed at: 
    #http://localhost:8000/regserve/data/students/
    #http://localhost:8000/regserve/students/
    #http://localhost:8000/regserve/createstudent/

    path('', views.index, name="index"),
    path('/data/students/', views.StudentListView.as_view(), name="api_students"), 
    path('/students/', views.StudentListForm.as_view(), name="students"),
    path('/createstudent/', views.StudentCreateForm.as_view(), name="create_student"), 
]