from rest_framework import status

from django.contrib.auth.models import User

from .base import BaseViewTest


class AuthLoginUserTest(BaseViewTest):
    """
    Tests for the login/ endpoint
    """

    def test_login_user_with_valid_credentials(self):
        # test login with valid credentials
        response = self.login_a_user("test_user", "testing")
        print(response)
        # assert token key exists
        self.assertIn("token", response.data)
        # assert status code is 200 OK
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        # test login with invalid credentials
        response = self.login_a_user("anonymous", "pass")
        # assert status code is 401 UNAUTHORIZED
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_login_user_with_empty_credentials(self):
        # test login with valid credentials
        response = self.login_a_user("", "testing")
        print(response)
        
        # assert status code is 401 UNAUTHORIZED
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_register_a_user(self):
        response = self.register_a_user("new_user", "new_pass", "new_user@mail.com")
        # assert status code is 201 CREATED
        self.assertEqual(response.data["username"], "new_user")
        self.assertEqual(response.data["email"], "new_user@mail.com")
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        # test with invalid data
        response = self.register_a_user()
        # assert status code
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_register_a_userwith_empty_creds(self):
        response = self.register_a_user("", "new_pass", "new_user@mail.com")
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_register_a_userwith_emptycreds(self):
        response = self.register_a_user("name", "", "new_user@mail.com")
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)