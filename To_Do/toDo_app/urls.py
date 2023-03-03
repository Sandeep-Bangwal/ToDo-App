from django.urls import path
from . import views

urlpatterns = [
   path('home', views.home, name='home'),
   path('', views.hendle_signUp, name='hendle_signUp'),
   path('login', views.hendle_login, name='hendle_login'),
   path('logout', views.handel_Logout, name='handel_Logout'),
   path('addTasks', views.addTasks, name='addTasks'),
   path('delete/<int:id>', views.delete, name='delete'),
   path('Finished/<int:id>', views.Finished, name='Finished'),
  
]
