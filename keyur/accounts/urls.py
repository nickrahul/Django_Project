from django.urls import path
from . import views


urlpatterns = [
    path('',views.user_login, name='user_login'),
    path('home/', views.home, name='home'),
    path('accounts/login/', views.user_login, name='account_login'),
    path('logout/',views.user_logout,name='user_logout'),
    path('all_jobs/',views.all_jobs,name='all_jobs'),
    path('add_user/',views.add_userr,name='add_user'),
    path('createjob/',views.createjob, name='createjob'),
    path('customers/',views.customers, name='customers')

]
