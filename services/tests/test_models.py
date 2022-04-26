from django.test import TestCase
from services.models import Provider


class ProviderModelTest(TestCase):
    @classmethod
    def setUpTestData(cls) -> None:
        Provider.objects.create(email='blabla@gmail.com',
                                name='blabla', language='japanese')
        return super().setUpTestData()

    def test_email(self):
        provider = Provider.objects.get(pk=1)
        field_label = provider._meta.get_field('email').verbose_name
        self.assertEqual(field_label, 'email')
        self.assertEqual(provider.email, "blabla@gmail.com")

    def test_name(self):
        provider = Provider.objects.get(pk=1)
        field_label = provider._meta.get_field('name').verbose_name
        self.assertEqual(field_label, 'name')
        max_length = provider._meta.get_field('name').max_length
        self.assertEqual(max_length, 100)
        self.assertEqual(provider.name, "blabla")

    def test_language(self):
        provider = Provider.objects.get(pk=1)
        field_label = provider._meta.get_field('language').verbose_name
        self.assertEqual(field_label, 'language')
        max_length = provider._meta.get_field('language').max_length
        self.assertEqual(max_length, 20)
        self.assertEqual(provider.language, "japanese")

    def test_currency(self):
        provider = Provider.objects.get(pk=1)
        field_label = provider._meta.get_field('currency').verbose_name
        self.assertEqual(field_label, 'currency')
        max_length = provider._meta.get_field('currency').max_length
        self.assertEqual(max_length, 5)
        self.assertEqual(provider.currency, None)
