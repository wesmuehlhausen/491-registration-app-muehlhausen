from django.urls import path
from . import views

application = 'regserve'

#to start, hit play on "Run and Debug on left hand tabs"

urlpatterns = [
    #to add student data with link 1

    path('', views.index, name="index"),
    path('/data/students/', views.StudentListView.as_view(), name="api_students"), # 1) http://localhost:8000/regserve/data/students/
    path('/students/', views.StudentListForm.as_view(), name="students"),# 2) http://localhost:8000/regserve/students/
    path('/createstudent/', views.StudentCreateForm.as_view(), name="create_student"), # 3) http://localhost:8000/regserve/createstudent/
]