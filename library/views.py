from django.shortcuts import render
from django.http import JsonResponse
from .services import ServiceRequestService

def create_service_request_view(request):
    if request.method == 'POST':
        client_name = request.POST.get('client_name')
        service_type = request.POST.get('service_type')
        
        service_request = ServiceRequestService.create_service_request(client_name, service_type)
        
        return JsonResponse({'message': 'Service request created successfully', 'id': service_request.id})

def update_service_request_view(request, request_id):
    if request.method == 'POST':
        new_status = request.POST.get('status')
        service_request = ServiceRequestService.update_service_request_status(request_id, new_status)
        
        return JsonResponse({'message': 'Service request updated successfully', 'status': service_request.status})

def delete_service_request_view(request, request_id):
    if request.method == 'POST':
        service_request = ServiceRequestService.delete_service_request(request_id)
        
        return JsonResponse({'message': 'Service request deleted successfully'})
