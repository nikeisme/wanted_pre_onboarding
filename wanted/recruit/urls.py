from django.urls import path

from . import views

app_name = 'recruit'

urlpatterns = [
    # 채용공고 목록
    path('', views.index, name='index'),

    # 채용공고 상세페이지
    path('<int:notification_id>/', views.detail, name='detail'),

    # 채용공고 등록
    path('notification/create/', views.notification_create, name='notification_create'),

    # 채용공고 지원
    path('user/apply/<int:notification_id>/', views.user_apply, name='user_apply'),

    # 채용공고 수정
    path('notification/modify/<int:notification_id>/', views.notification_modify, name='notification_modify'),

    # 채용공고 삭제
    path('notification/delete/<int:notification_id>/', views.notification_delete, name='notification_delete'),

    # 회사가 올린 다른 채용 공고
    path('another/<str:slug/', views.another_page),
]