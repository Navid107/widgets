from django.urls import path
from . import views


urlpatterns = [
  path('', views.home, name='home'),
  path('create/', views.WidgetCreate.as_view(), name='widgets_create'),
  path('<int:pk>/delete/', views.WidgetDelete.as_view(), name='widgets_delete'),
]