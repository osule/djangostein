from django.test import TestCase, Client
from django.urls import reverse

from auth.models import MyUser as User


# Create your tests here.
class AuthTestCase(TestCase):
    def setUp(self):
        self.client = Client()
        self.credentials = {'username': 'user', 'password': 'password'}
        self.user = User.objects.create_user(**self.credentials)

    def test_administration_authorization(self):

        from urllib.parse import urlencode

        url = reverse("authing:login")
        # encoded_get_params = urlencode({'next': reverse("home:index")})
        # separator = '&' if '?' in bare_url else '?'
        # url = '{}{}{}'.format(bare_url, separator, encoded_get_params)
        params = dict(**self.credentials, next=reverse("home:index"))
        response = self.client.post(
            url,
            params,
            follow=True
        )

        # self.assertEqual(response.status_code, 302)
        self.assertRedirects(
            response,
            reverse("home:index"),
            status_code=302,
            target_status_code=200
        )