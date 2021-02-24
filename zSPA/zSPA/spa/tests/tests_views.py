from django.test import TestCase
from django.urls import reverse
from ..models import Images


class TestViews(TestCase):
    """
    Test for views in this app
    """

    def test_index_GET(self):
        response = self.client.get(reverse('spa:index'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Alaska")
        self.assertQuerysetEqual(response.context['images'], [])

    def test_no_images(self):
        response = self.client.get(reverse('spa:index'))
        self.assertContains(response, "Brak obrazów dostępnych w galerii.")

    def test_some_images(self):
        # Arrange
        from django.core.files.uploadedfile import SimpleUploadedFile
        image_path = 'zspa/cdn_test/media/spa/git.jpg'
        newPhoto = SimpleUploadedFile(name='test_image.jpg', content=open(image_path, 'rb').read(),
                                            content_type='image/jpeg')
        test_image = Images.objects.create(name='test', description='test', image=newPhoto, cssClass='small')
        # Act
        response = self.client.get(reverse('spa:index'))
        # Assert
        self.assertContains(response,
                            "li alt=\"test\" class=\"small\" style=\"background-image: url(/media/{})".format(test_image.image.name))

    def test_google_form_link(self):
        response = self.client.get(reverse('spa:index'))
        self.assertContains(response, "docs.google.com/forms")

    def test_google_map_link(self):
        response = self.client.get(reverse('spa:index'))
        self.assertContains(response, "www.google.com/maps/")


