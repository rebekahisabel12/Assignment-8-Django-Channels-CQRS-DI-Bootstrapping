from django.contrib.auth.models import User
from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework import routers
from rest_framework.test import APIRequestFactory, APITestCase


from .models import AnalyticalMethod
from .models import Instrument
from .views import AnalyticalMethodViewSet, InstrumentViewSet


class InstrumentTests(APITestCase):
    def setUp(self):
        self.factory = APIRequestFactory()
        self.user = User.objects.create_user(
            username='testuser', password='password')
        self.client.force_login(self.user)
        self.create_url = reverse('an_organ:instrument-list')
        self.instrument_data = {
            'instrument_id': '654',
            'manufacturer': 'Firenza',
            'sample_type': 'Liquid',
        }

    def test_create_instrument(self):
        response = self.client.post(
            self.create_url, self.instrument_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Instrument.objects.count(), 1)
        self.assertEqual(Instrument.objects.get(
            instrument_id='654').manufacturer, 'Firenza')


# class AnalyticalMethodAPITestCase(APITestCase):
#     def setUp(self):
#         self.factory = APIRequestFactory()
#         self.view = AnalyticalMethodViewSet.as_view(
#             {'post': 'create', 'get': 'retrieve'})
#         self.instrument_data = {
#             'manufacturer': 'Manufacturer X',
#             'sample_type': 'Solid',
#             'price_per_sample': '100.00'
#         }
#         self.instrument = Instrument.objects.create(**self.instrument_data)

#         self.analytical_method_data = {
#             'name': 'Test Method',
#             'description': 'Test Method Description',
#             'instrument': reverse('instrument-detail', kwargs={'pk': self.instrument.pk}),
#         }

#     def test_create_analytical_method(self):
#         url = '/api/analytical-methods/'
#         request = self.factory.post(
#             url, self.analytical_method_data, format='json')
#         response = self.view(request)
#         self.assertEqual(response.status_code, status.HTTP_201_CREATED)
#         self.assertEqual(AnalyticalMethod.objects.count(), 1)
#         self.assertEqual(
#             AnalyticalMethod.objects.last().name, 'Test Method')

        # response = self.client.post(self.list_url, data, format="json")
        # print("Response status code:", response.status_code)
        # print("Response content:", response.content.decode('utf-8'))

        # self.assertTrue(status.is_success(response.status_code))
        # self.assertEqual(Analytical_Method.objects.count(), 2)
        # created_method = Analytical_Method.objects.get(
        #     method_name="internal temp")
        # self.assertEqual(created_method.method_name, "internal temp")

    # def test_analytical_method_detail(self):
    #     url = reverse('analytical-method-detail',
    #                   kwargs={'pk': self.analytical_method.pk})
    #     response = self.client.get(url)
    #     self.assertEqual(response.status_code, status.HTTP_200_OK)
    #     self.assertEqual(response.data['method_name'],
    #                      self.analytical_method_data['method_name'])

    # def test_analytical_method_create(self):
    #     url = reverse('analytical-method-list')
    #     new_analytical_method_data = {
    #         "method_name": "New Method",
    #         "method_description": "Description of New Method",
    #         "sample_matrix": "New Matrix",
    #         "cost_per_sample": 100.00,
    #     }
    #     response = self.client.post(
    #         url, new_analytical_method_data, format='json')
    #     self.assertEqual(response.status_code, status.HTTP_201_CREATED)
    #     # Assuming two AnalyticalMethod objects are created now
    #     self.assertEqual(Analytical_Method.objects.count(), 2)
