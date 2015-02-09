import unittest

from django.test import TestCase, Client
from django.conf import settings
from django.contrib.auth.models import User

from tokenauth.authbackends import TokenAuthBackend

import requests
import responses


class ApiTestCase(TestCase):
    def setUp(self):

        pass

    def test_one_plus(self):

        pass