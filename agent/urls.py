from django.urls import path
from django.contrib.auth import views as auth_views
from agent import views



urlpatterns = [

    path('agent-registration/', views.AgentRegistration, name='agentregistration'),

]