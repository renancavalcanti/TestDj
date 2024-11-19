from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.login_view, name='login'),
    path('signup/', views.signup_view, name='signup'),  # Rota para o signup
    path('tasks/', views.fetch_tasks, name='tasks'),
    path('tasks/new/', views.create_task, name='create_task'),
    path('tasks/<str:task_id>/delete/', views.delete_task, name='delete_task'),
    path('tasks/<str:task_id>/done/', views.mark_task_done, name='mark_task_done'),
]
