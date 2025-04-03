from rest_framework.test import APITestCase
from rest_framework import status
from jobs.models import JobPost
from django.urls import reverse


class JobPostTests(APITestCase):

    def setUp(self):
        # registered as 'jobpost-list' by DefaultRouter
        self.url = reverse('jobpost-list')
        self.valid_data = {
            "title": "Backend Developer",
            "company": "Google",
            "location": "Hyderabad",
            "salary": 2500000,
            "description": "Strong Django and REST skills"
        }

    def test_create_job_success(self):
        response = self.client.post(self.url, self.valid_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(JobPost.objects.count(), 1)

    def test_create_job_missing_fields(self):
        response = self.client.post(self.url, {}, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertIn("title", response.data)
        self.assertIn("company", response.data)

    def test_job_list_retrieval(self):
        JobPost.objects.create(**self.valid_data)
        response = self.client.get(self.url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
