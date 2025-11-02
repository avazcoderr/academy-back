import pytest
from faker import Faker
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient
from apps.courses.models import Course

fake = Faker()

@pytest.fixture
def api_client():
    """APIClient fixture for making API requests"""
    return APIClient()


@pytest.mark.django_db
class TestCourseAPI:
    """Test suite for Course API endpoints"""
    
    def test_create_course(self, api_client):
        """Test creating a new course via API"""
        url = reverse('course-list-create') 


        # user = CustomUser.objects.create_user(username='testuser', password='testpass')
        # api_client.force_authenticate(user=user)

        course = Course(
            title=" ".join(fake.words(nb=3)),
            description=fake.text(),
            duration=fake.random_int(min=1, max=7000),
            is_active=fake.boolean(),
            is_premium=fake.boolean()
        )

        print(type(fake.sentence))
        data = {
            "title": course.title,
            "description": course.description,
            "duration": course.duration,
            "is_active": course.is_active,
            "is_premium": course.is_premium
        }
        # response = post(url, data, format='json')
        response = api_client.post(url, data, format='json')
        print(response.status_code)
        print(response.data)

        result = response.data['result']


        assert response.status_code == status.HTTP_201_CREATED
        assert result['title'] == course.title
        assert result['duration'] == course.duration
        assert result['is_active'] == course.is_active
        assert Course.objects.filter(title=data['title']).exists()

