from django.urls import path
from myguest import views

urlpatterns = [
    path('', views.ListFunc), # guest의 요청명이 들어왔을 때 해당 코드가 실행되므로 path를 ''로 받는다.
    path('insert/',views.InsertFunc),
    path('insertok/',views.InsertFuncOk),
]