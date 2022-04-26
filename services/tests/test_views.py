from django.test import TestCase
from django.urls import reverse
from services.models import Area, Provider


class ProviderTest(TestCase):
    @classmethod
    def setUpTestData(cls) -> None:
        for provider_id in range(5):
            Provider.objects.create(
                email="provider{}@gmail.com".format(provider_id),
                name="provider{}".format(provider_id),
                currency="USD"
            )
        return super().setUpTestData()

    def test_list(self):
        response = self.client.get(reverse('provider'))
        self.assertEqual(response.status_code, 200)

    def test_create(self):
        response = self.client.post(reverse('provider'), {
                                    'email': 'new@gmail.com'})
        self.assertEqual(response.status_code, 201)

    def test_retrieve(self):
        response = self.client.get(
            reverse('provider_detail', kwargs={'pk': 3}))
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'provider0@gmail.com', response.content)

    def test_patch(self):
        response = self.client.patch(
            reverse('provider_detail', kwargs={'pk': 3}), {'name': 'new_name'}, content_type='application/json')
        self.assertEqual(response.status_code, 200)

        response = self.client.get(
            reverse('provider_detail', kwargs={'pk': 3}))
        self.assertIn(b'new_name', response.content)

    def test_delete(self):
        response = self.client.delete(
            reverse('provider_detail', kwargs={'pk': 3}))
        self.assertEqual(response.status_code, 204)

        response = self.client.get(
            reverse('provider_detail', kwargs={'pk': 3}))
        self.assertEqual(response.status_code, 404)

    def test_put(self):
        response = self.client.put(
            reverse('provider_detail', kwargs={'pk': 3}), {'email': 'new@gmail.com'}, content_type='application/json')
        self.assertEqual(response.status_code, 200)

        response = self.client.get(
            reverse('provider_detail', kwargs={'pk': 3}))
        self.assertIn(b'new@gmail.com', response.content)


class AreaTest(TestCase):
    @classmethod
    def setUpTestData(cls) -> None:
        provider = Provider.objects.create(
            email="provider1@gmail.com",
            name="provider1",
            currency="USD"
        )
        Area.objects.create(
            provider=provider, name="area-1", price=100.5,
            region='POLYGON((0 0, 0 50, 50 50, 50 0, 0 0))'
        )

    def test_create(self):
        response = self.client.post(reverse('area'), {
            'provider_id': 2,
            'name': 'area-2', 'price': 80.00, 'region': 'POLYGON((0 20, 20 20, 20 30, 0 20))'})
        self.assertEqual(response.status_code, 201)

    def test_list(self):
        response = self.client.get(reverse('area'))
        self.assertEqual(response.status_code, 200)

    def test_search_by_point(self):
        response = self.client.get(
            reverse('area'), {'provider_id': 2, 'point': 'POINT(18 18)'})
        self.assertNotEqual(response.content, b'[]')
        self.assertEqual(response.status_code, 200)

    def test_retrieve(self):
        response = self.client.get(
            reverse('area_detail', kwargs={'pk': 2}))
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'area-1', response.content)

    def test_patch(self):
        response = self.client.patch(
            reverse('area_detail', kwargs={'pk': 2}),
            {'region': 'POLYGON((12 12, 12 50, 50 50, 50 12, 12 12))'}, content_type='application/json')
        self.assertEqual(response.status_code, 200)

        response = self.client.get(
            reverse('area_detail', kwargs={'pk': 2}))
        self.assertIn(b'[12.0,12.0],[12.0,50.0]', response.content)

    def test_put(self):
        response = self.client.put(
            reverse('area_detail', kwargs={'pk': 2}),
            {'name': 'area-22', 'provider_id': 2, 'price': 80.5,
                'region': 'POLYGON((18 18, 18 72, 72 72, 72 18, 18 18))'},
            content_type='application/json')
        self.assertEqual(response.status_code, 200)

        response = self.client.get(
            reverse('area_detail', kwargs={'pk': 2}))
        self.assertIn(
            b'[18.0,18.0],[18.0,72.0],[72.0,72.0],[72.0,18.0],[18.0,18.0]', response.content)

    def test_delete(self):
        response = self.client.delete(
            reverse('area_detail', kwargs={'pk': 2}))
        self.assertEqual(response.status_code, 204)

        response = self.client.get(
            reverse('area_detail', kwargs={'pk': 2}))
        self.assertEqual(response.status_code, 404)
