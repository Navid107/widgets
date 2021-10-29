from django.urls import path
from . import views


urlpatterns = [
  path('', views.home, name='home'),
  path('create/', views.WidgetCreate.as_view(), name='widgets_create'),
  path('<int:widget_id>/', views.widget_delete, name='widgets_delete'),
]