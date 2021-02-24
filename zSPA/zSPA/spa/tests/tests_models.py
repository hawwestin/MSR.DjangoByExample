import os

from django.test import TestCase

from ..models import Images


class TestModels(TestCase):

    def setUp(self) -> None:
        from django.core.files.uploadedfile import SimpleUploadedFile
        image_path = 'zspa/cdn_test/media/spa/git.jpg'
        newPhoto = SimpleUploadedFile(name='test_image.jpg', content=open(image_path, 'rb').read(),
                                      content_type='image/jpeg')
        self.test_image = Images.objects.create(name='test', description='test', image=newPhoto, cssClass='small')

    def tearDown(self) -> None:
        if self.test_image is not None:
            os.remove(self.test_image.image.path)
        pass

    def test_image_str_representation(self):
        self.assertIs(str(self.test_image), 'test')

    def test_image_repr_representation(self):
        self.assertIs(repr(self.test_image), 'test')

