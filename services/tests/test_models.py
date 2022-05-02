from django.test import TestCase
from services.models import Area, Provider
from django.contrib.gis.geos import Polygon


class ProviderModelTest(TestCase):
    def setUp(self):
        self.provider = Provider.objects.create(email='provider@gmail.com',
                                                name='provider', language='japanese')

    def test_str(self):
        self.assertEqual(str(self.provider), "provider")

    def test_email(self):
        meta_data = self.provider._meta.get_field('email')
        self.assertEqual(meta_data.verbose_name, 'email')
        self.assertEqual(meta_data.unique, True)
        self.assertEqual(meta_data.null, False)
        self.assertEqual(meta_data.blank, False)
        self.assertEqual(self.provider.email, "provider@gmail.com")

    def test_name(self):
        meta_data = self.provider._meta.get_field('name')
        self.assertEqual(meta_data.verbose_name, 'name')
        self.assertEqual(meta_data.max_length, 100)
        self.assertEqual(meta_data.null, True)
        self.assertEqual(meta_data.blank, True)
        self.assertEqual(self.provider.name, "provider")

    def test_language(self):
        meta_data = self.provider._meta.get_field('language')
        self.assertEqual(meta_data.verbose_name, 'language')
        self.assertEqual(meta_data.max_length, 20)
        self.assertEqual(meta_data.null, True)
        self.assertEqual(meta_data.blank, True)
        self.assertEqual(self.provider.language, "japanese")

    def test_currency(self):
        meta_data = self.provider._meta.get_field('currency')
        self.assertEqual(meta_data.verbose_name, 'currency')
        self.assertEqual(meta_data.max_length, 5)
        self.assertEqual(meta_data.null, True)
        self.assertEqual(meta_data.blank, True)
        self.assertEqual(self.provider.currency, None)

    def test_created_at(self):
        meta_data = self.provider._meta.get_field('created_at')
        self.assertEqual(meta_data.verbose_name, 'created_at')
        self.assertEqual(meta_data.auto_now_add, True)
        self.assertEqual(meta_data.auto_now, True)

    def test_created_at(self):
        meta_data = self.provider._meta.get_field('updated_at')
        self.assertEqual(meta_data.verbose_name, 'updated_at')
        self.assertEqual(meta_data.auto_now_add, False)
        self.assertEqual(meta_data.auto_now, True)


class AreaModelTest(TestCase):
    def setUp(self):
        self.provider = Provider.objects.create(email='provider@gmail.com',
                                                name='provider', language='japanese')
        self.area = Area.objects.create(provider=self.provider, name="area-1", price=24.35,
                                        region='POLYGON((0 0, 0 50, 50 50, 50 0, 0 0))')

    def test_str(self):
        self.assertEqual(str(self.area), "area-1")

    def test_provider(self):
        self.assertEqual(self.area.provider.pk, self.provider.pk)

    def test_name(self):
        meta_data = self.area._meta.get_field('name')
        self.assertEqual(meta_data.verbose_name, 'name')
        self.assertEqual(meta_data.null, False)
        self.assertEqual(meta_data.blank, False)
        self.assertEqual(self.area.name, "area-1")

    def test_price(self):
        meta_data = self.area._meta.get_field('price')
        self.assertEqual(meta_data.verbose_name, 'price')
        self.assertEqual(meta_data.null, False)
        self.assertEqual(meta_data.blank, False)
        self.assertEqual(meta_data.max_digits, 12)
        self.assertEqual(meta_data.decimal_places, 2)
        self.assertEqual(self.area.price, 24.35)

    def test_region(self):
        meta_data = self.area._meta.get_field('region')
        self.assertEqual(meta_data.verbose_name, 'region')
        self.assertEqual(meta_data.null, True)
        self.assertEqual(meta_data.blank, True)
        self.assertTrue(isinstance(self.area.region, Polygon))

    def test_created_at(self):
        meta_data = self.area._meta.get_field('created_at')
        self.assertEqual(meta_data.verbose_name, 'created_at')
        self.assertEqual(meta_data.auto_now_add, True)
        self.assertEqual(meta_data.auto_now, False)

    def test_updated_at(self):
        meta_data = self.area._meta.get_field('updated_at')
        self.assertEqual(meta_data.verbose_name, 'updated_at')
        self.assertEqual(meta_data.auto_now_add, False)
        self.assertEqual(meta_data.auto_now, True)
