from rest_framework.test import APITestCase
from django.db import IntegrityError
from library.test.TestUtils import TestUtils
from django.urls import reverse
from unittest.mock import patch
from django.urls import get_resolver
from django.test import TestCase
from library.models import ServiceRequest
from library.services import ServiceRequestService


class ServiceRequestExceptionalTest(TestCase):


    def test_service_request_not_found_for_update(self):
        """Test that an exception is raised when trying to update a non-existent service request"""
        test_obj = TestUtils()
        try:
            # Try to update a service request that does not exist
            service_request = ServiceRequestService.update_service_request_status(999, 'completed')
            test_obj.yakshaAssert("TestServiceRequestNotFoundForUpdate", False, "exceptional")
            print("TestServiceRequestNotFoundForUpdate = Failed")
        except ServiceRequest.DoesNotExist:
            test_obj.yakshaAssert("TestServiceRequestNotFoundForUpdate", True, "exceptional")
            print("TestServiceRequestNotFoundForUpdate = Passed")
        except Exception as e:
            test_obj.yakshaAssert("TestServiceRequestNotFoundForUpdate", False, "exceptional")
            print(f"TestServiceRequestNotFoundForUpdate = Failed")
            
    