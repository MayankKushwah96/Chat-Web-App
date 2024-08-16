from django.urls import path
from chat import views 

urlpatterns = [
    path("entry/", views.EntryView, name="entry"),
    path("<str:room_name>/<str:username>/", views.RoomView, name="room"),
    path('', views.login_page, name="login_page"),
    path('register/', views.register_page, name="register_page"),
    path('logout/', views.logout_page, name="logout_page"),
    path('home/', views.home_page, name='home_page'), 
]
 
