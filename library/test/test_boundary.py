from rest_framework.test import APITestCase
from library.test.TestUtils import TestUtils
from django.urls import reverse
from django.test import TestCase
from rest_framework.test import APITestCase
from library.models import ServiceRequest
from library.services import ServiceRequestService

class ServiceRequestBoundaryTest(TestCase):


    def test_service_request_model_save_and_retrieve(self):
        """Test if a service request is saved and retrieved correctly"""
        test_obj = TestUtils()
        try:
            # Create a service request
            service_request = ServiceRequestService.create_service_request('Sam Brown', 'maintenance')
            
            # Retrieve the service request from the database
            retrieved_service_request = ServiceRequest.objects.get(id=service_request.id)
            
            # Check if the retrieved service request has the same ID as the created one
            if service_request.id == retrieved_service_request.id:
                test_obj.yakshaAssert("TestServiceRequestSaveAndRetrieve", True, "exceptional")
                print("TestServiceRequestSaveAndRetrieve = Passed")
            else:
                test_obj.yakshaAssert("TestServiceRequestSaveAndRetrieve", False, "exceptional")
                print("TestServiceRequestSaveAndRetrieve = Failed")
        except Exception as e:
            test_obj.yakshaAssert("TestServiceRequestSaveAndRetrieve", False, "exceptional")
            print(f"TestServiceRequestSaveAndRetrieve = Failed")
            
            
    