#step 1 creat an app by putting python manage.py startapp [inset name] into the terminal
#step 2 add the app to the settings.py file in the INSTALLED_APPS section
#step 3 add the path in the  urls.py file in the main project folder urls.py 
# file(in this case its moviesstore/urls.py)
#step 4 create a urls.py file in the app folder (in this case its accounts/urls.py)
#step 5 define the function in the views.py file in the app folder (in this case
#  its accounts/views.py)
#step 6 create the html files in the templates folder in the app folder (in this 
# case its accounts/templates/accounts/)
#step 7 create the html file for this app we have to extend the base.html file
# in the home app folder
#step 8 add the link to the new page in the base.html file in the home app folder
#step 9 test your changes by running on the local server byt typing python manage.py runserver in the terminal
#step 10 depending on use you may need to add a new files for forms.py so the admin page can reconize the new user
#when adding new pages in the app you repeat steps 4,5,6,8,9 then you make a new html file for each new page in the
#  templates folder in the app folder depending on functionality you will link to  the new page in the base.html file in the home app folder
from django.urls import path
from . import views

urlpatterns = [
    #inittial
    path('signup', views.signup, name='accounts.signup'),
    #branches from intitial to other pages in this app
    path('login/', views.login, name='accounts.login'),
    path('logout/', views.logout, name='accounts.logout'),
    path('orders/', views.orders, name='accounts.orders'),


]