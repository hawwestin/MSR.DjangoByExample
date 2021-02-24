from django.test import SimpleTestCase
from django.urls import reverse, resolve

# Create your tests here.
from ..views import index


class TestUrls(SimpleTestCase):
    """
    test cases to test URLS redirects
    """

    def test_load_index(self):
        """
        Test if url for index will return index view.
        :return:
        """
        url = reverse('spa:index')
        self.assertEquals(resolve(url).func, index)
