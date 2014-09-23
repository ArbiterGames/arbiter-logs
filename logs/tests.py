import unittest
import requests
from django.core.urlresolvers import reverse
from django.conf import settings
from logs.utils import Logger

logger = Logger()


class Tests(unittest.TestCase):

    def test_can_get_200_from_reporting(self):
        r = requests.post('%s%s' % (settings.URL_ORIGIN, reverse('report')))
        self.assertEqual(r.status_code, 200)
