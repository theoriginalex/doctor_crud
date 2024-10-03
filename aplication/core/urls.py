from django.urls import path
from aplication.core import views

app_name='core' # define un espacio de nombre para la aplicacion
urlpatterns = [
# ruta principal
path('', views.home,name='home'),
# ruts de doctores

path('doctor_list/', views.doctor_List,name="doctor_list"),
path('doctor_create/', views.doctor_create,name="doctor_create"),
]
