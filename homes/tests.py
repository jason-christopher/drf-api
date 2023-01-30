from django.contrib.auth import get_user_model
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from .models import Home


class HomeTests(APITestCase):
    # In Python, the @classmethod decorator is used to declare a method in the class as a class method that can be called using ClassName.MethodName()
    # click the blue circle, this overrides a particular method
    @classmethod
    def setUpTestData(cls):
        testuser1 = get_user_model().objects.create_user(
            username="testuser1", password="pass"
        )
        testuser1.save()

        test_home = Home.objects.create(
            owner=testuser1,
            street_address="1234 Test St.",
            city="Orlando",
            state="FL",
            zip=12345,
            square_feet=1000,
            description="Great house.",
        )
        test_home.save()

    def test_homes_model(self):
        home = Home.objects.get(id=1)
        actual_owner = str(home.owner)
        actual_street_address = str(home.street_address)
        actual_description = str(home.description)
        self.assertEqual(actual_owner, "testuser1")
        self.assertEqual(actual_street_address, "1234 Test St.")
        self.assertEqual(
            actual_description, "Great house."
        )

    def test_get_home_list(self):
        url = reverse("home_list")
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        homes = response.data
        self.assertEqual(len(homes), 1)
        self.assertEqual(homes[0]["street_address"], "1234 Test St.")

    def test_get_home_by_id(self):
        url = reverse("home_detail", args=(1,))
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        home = response.data
        self.assertEqual(home["street_address"], "1234 Test St.")

    def test_create_home(self):
        url = reverse("home_list")
        data = {"owner": 1, "street_address": "4567 Test St.", "city": "Orlando", "state": "FL", "zip": 12345,  "square_feet": 1200, "description": "Even better house"}
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        homes = Home.objects.all()
        self.assertEqual(len(homes), 2)
        self.assertEqual(Home.objects.get(id=2).street_address, "4567 Test St.")

    def test_update_home(self):
        url = reverse("home_detail", args=(1,))
        data = {
            "owner": 1,
            "street_address": "1234 Test St.",
            "description": "Great house.",
        }
        response = self.client.put(url, data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        home = Home.objects.get(id=1)
        self.assertEqual(home.street_address, data["street_address"])
        self.assertEqual(home.owner.id, data["owner"])
        self.assertEqual(home.description, data["description"])

    def test_delete_home(self):
        url = reverse("home_detail", args=(1,))
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        homes = Home.objects.all()
        self.assertEqual(len(homes), 0)
