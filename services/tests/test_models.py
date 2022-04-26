from django.test import TestCase
from services.models import Area, Provider
from django.contrib.gis.geos import Polygon


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


class ProviderModelTest(TestCase):
    @classmethod
    def setUpTestData(cls) -> None:
        Provider.objects.create(email='blabla@gmail.com',
                                name='blabla', language='japanese')
        Area.objects.create(provider_id=1, name="area-1", price=24.35,
                            region='POLYGON((0 0, 0 50, 50 50, 50 0, 0 0))')
        return super().setUpTestData()

    def test_provider(self):
        area = Area.objects.get(pk=1)
        self.assertEqual(area.provider.pk, 1)

    def test_name(self):
        area = Area.objects.get(pk=1)
        field_label = area._meta.get_field('name').verbose_name
        self.assertEqual(field_label, 'name')
        max_length = area._meta.get_field('name').max_length
        self.assertEqual(max_length, 100)
        self.assertEqual(area.name, "area-1")

    def test_price(self):
        area = Area.objects.get(pk=1)
        field_label = area._meta.get_field('price').verbose_name
        self.assertEqual(field_label, 'price')
        max_digits = area._meta.get_field('price').max_digits
        self.assertEqual(max_digits, 12)
        decimal_places = area._meta.get_field('price').decimal_places
        self.assertEqual(decimal_places, 2)

    def test_region(self):
        area = Area.objects.get(pk=1)
        field_label = area._meta.get_field('region').verbose_name
        self.assertEqual(field_label, 'region')
        self.assertTrue(isinstance(area.region, Polygon))
