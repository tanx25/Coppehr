from django.urls import path
from . import views

app_name = 'coppehr'

urlpatterns = [
    path('', views.home, name='home'),
    path('login/', views.user_login, name='login'),
    path('logout/', views.user_logout, name='logout'),
    path('calendar/', views.calendar, name='calendar'),
    path('about/', views.about, name='about'),
    path('event/<int:event_id>/', views.event_detail, name='event-detail'),
    path('resource/<int:resource_id>/', views.resource_detail, name='resource-detail'),
    path('htips/<int:healthtips_id>/', views.healthtips_detail, name='htips-detail'),
    path('health-events/', views.health_events, name='health-events'),
    path('friendship-events/', views.friendship_events, name='friendship-events'),
    path('support-events/', views.support_events, name='support-events'),
    path('health-resources/', views.health_resources, name='health-resources'),
    path('friendship-resources/', views.friendship_resources, name='friendship-resources'),
    path('support-resources/', views.support_resources, name='support-resources'),
]
