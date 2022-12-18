from ..models import *
from ..views import *
from ..serializers import *
from rest_framework.test import APIClient,APITransactionTestCase,APITestCase
from django.db import connections
from rest_framework import status


class testApi(APITestCase):
    def setUp(self) -> None:
        url='http://127.0.0.1:8000/api/'
        return super().setUp()
    def test_token_working(self):
        response=self.client.get(url)
        self.assertEqual(response.status_code,status.HTTP_401_UNAUTHORIZED)
        
    def test_register_working(self):
        payload={"email":"mohamed@mohamed.mohamed","password":"Mohamed*1234","password2":"Mohamed*1234"}
        response=self.client.post(f'{url}register/',data=payload)
        self.assertEqual(response.status_code,status.HTTP_201_CREATED)
    
    