from django.urls import path
from . import views

urlpatterns = [
    path('create_service_request/', views.create_service_request_view, name='create_service_request'),
    path('update_service_request/<int:request_id>/', views.update_service_request_view, name='update_service_request'),
    path('delete_service_request/<int:request_id>/', views.delete_service_request_view, name='delete_service_request'),
]
