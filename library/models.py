from django.db import models

class ServiceRequest(models.Model):
    SERVICE_CHOICES = [
        ('consulting', 'Consulting'),
        ('maintenance', 'Maintenance'),
        ('support', 'Support')
    ]
    
    STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('in_progress', 'In Progress'),
        ('completed', 'Completed')
    ]
    
    client_name = models.CharField(max_length=100)
    service_type = models.CharField(max_length=20, choices=SERVICE_CHOICES)
    request_date = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending')
    
    def __str__(self):
        return f"Request by {self.client_name} for {self.service_type}"
