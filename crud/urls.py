from django.contrib.auth import views as auth_views
from django.contrib.auth.views import LoginView
from django.urls import path
from .views import ProjectListView, ProjectCreateView, ProjectUpdateView, ProjectDeleteView, DeveloperListView, DeveloperCreateView, DeveloperUpdateView, DeveloperDeleteView

urlpatterns = [
    path('', ProjectListView.as_view(), name='project_list'),
    path('project-create/', ProjectCreateView.as_view(), name='project_create'),
    path('project-update/<int:pk>', ProjectUpdateView.as_view(),name='project_update'),
    path('project-delete/<int:pk>', ProjectDeleteView.as_view(), name='project_delete'),
    
    path('developer/', DeveloperListView.as_view(), name='developer_list'),
    path('developer-create/', DeveloperCreateView.as_view(), name='developer_create'),
    path('developer-update/<int:pk>', DeveloperUpdateView.as_view(),name='developer_update'),
    path('developer-delete/<int:pk>', DeveloperDeleteView.as_view(), name='developer_delete'),
]