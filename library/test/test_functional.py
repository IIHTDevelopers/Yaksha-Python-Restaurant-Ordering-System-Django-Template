from django.test import TestCase
from django.urls import reverse
from library.test.TestUtils import TestUtils
from rest_framework.test import APITestCase
from django.test import TestCase
from library.models import ServiceRequest
from library.services import ServiceRequestService

class ServiceRequestFunctionalTest(TestCase):
    def test_create_service_request(self):
        """Test if a service request is created successfully"""
        test_obj = TestUtils()
        try:
            service_request = ServiceRequestService.create_service_request('John Doe', 'consulting')
            if service_request:
                test_obj.yakshaAssert("TestCreateServiceRequest", True, "functional")
                print("TestCreateServiceRequest = Passed")
            else:
                test_obj.yakshaAssert("TestCreateServiceRequest", False, "functional")
                print("TestCreateServiceRequest = Failed")
        except:
            test_obj.yakshaAssert("TestCreateServiceRequest", False, "functional")
            print("TestCreateServiceRequest = Failed")
    def test_update_service_request(self):
        """Test if service request status is updated successfully"""
        test_obj = TestUtils()
        try:
            service_request = ServiceRequestService.create_service_request('Jane Smith', 'maintenance')
            updated_service_request = ServiceRequestService.update_service_request_status(service_request.id, 'completed')
            if updated_service_request.status == 'completed':
                test_obj.yakshaAssert("TestUpdateServiceRequest", True, "functional")
                print("TestUpdateServiceRequest = Passed")
            else:
                test_obj.yakshaAssert("TestUpdateServiceRequest", False, "functional")
                print("TestUpdateServiceRequest = Failed")
        except:
            test_obj.yakshaAssert("TestUpdateServiceRequest", False, "functional")
            print("TestUpdateServiceRequest = Failed")
            
    def test_delete_service_request(self):
        """Test if a service request is deleted successfully"""
        test_obj = TestUtils()
        try:
            service_request = ServiceRequestService.create_service_request('Jake Hill', 'support')
            deleted_service_request = ServiceRequestService.delete_service_request(service_request.id)
            if not ServiceRequest.objects.filter(id=deleted_service_request.id).exists():
                test_obj.yakshaAssert("TestDeleteServiceRequest", True, "functional")
                print("TestDeleteServiceRequest = Passed")
            else:
                test_obj.yakshaAssert("TestDeleteServiceRequest", False, "functional")
                print("TestDeleteServiceRequest = Failed")
        except:
            test_obj.yakshaAssert("TestDeleteServiceRequest", False, "functional")
            print("TestDeleteServiceRequest = Failed")