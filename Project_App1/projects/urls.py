from django.urls import path
from . import views

urlpatterns = [
    path('projects/',views.projects, name='all_projects'),
    path('projects/all/',views.allprojects, name='all_projects_details'),
    path('projects/<str:uid>/',views.projectbyid, name='proj_pid'),
    path('contactus/',views.contactus, name='Contactpage'),
    path('createproject/',views.project_create_form, name='create_project'),
    path('updateproject/<str:pk>/',views.project_update_form, name='update_project'),
    path('deleteproject/<str:pk>/',views.delete_project, name='delete_project'),
    path('',views.homepage, name='homepage'),

]
