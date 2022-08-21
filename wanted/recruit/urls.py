from django.urls import path

from . import views

app_name = 'recruit'

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:notification_id>/', views.detail, name='detail'),
    path('notification/create/', views.notification_create, name='notification_create'),
    path('user/apply/<int:notification_id>/', views.user_apply, name='user_apply'),
    path('notification/modify/<int:notification_id>/', views.notification_modify, name='notification_modify'),
    path('notification/delete/<int:notification_id>/', views.notification_delete, name='notification_delete'),
]