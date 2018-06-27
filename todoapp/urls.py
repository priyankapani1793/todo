from django.contrib import admin
from django.urls import path
from todoapp import views

urlpatterns = [
   # path(r'admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('<int:task_id>/', views.detail, name='detail'),
]