from django.urls import path

from . import views

app_name = 'learning_logs'

urlpatterns = [
    # Домашняя страница
    path('', views.index, name='index'),
    # Страница с темами
    path('topics/', views.topics, name='topics'),
    # Страница с подробной информацией по отдельной теме
    path('topics/<int:topic_id>/', views.topic, name='topic'),
]