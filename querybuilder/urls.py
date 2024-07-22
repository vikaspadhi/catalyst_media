from django.urls import path , include
from .views import UsersList , UploadData , QueryBuilder ,  CSVDataFilterAPIView

urlpatterns = [
    path('',QueryBuilder.as_view(),name='query'),
    path('users/',UsersList.as_view(),name='userList'),
    path('upload/',UploadData.as_view(),name='uploadData'),
    path('filter/',CSVDataFilterAPIView.as_view(),name='filter'),
]
