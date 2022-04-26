from django.test import TestCase
from django.urls import reverse
from services.models import Provider


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
        response = self.client.get(reverse('provider_view'))
        self.assertEqual(response.status_code, 200)

    def test_create(self):
        response = self.client.post(reverse('provider_view'), {
                                    'email': 'new@gmail.com'})
        self.assertEqual(response.status_code, 201)

    def test_retrieve(self):
        response = self.client.get(
            reverse('provider_detail_view', kwargs={'pk': 3}))
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'provider1@gmail.com', response.content)

    def test_patch(self):
        response = self.client.patch(
            reverse('provider_detail_view', kwargs={'pk': 2}), {'name': 'new_name'}, content_type='application/json')
        self.assertEqual(response.status_code, 200)

        response = self.client.get(
            reverse('provider_detail_view', kwargs={'pk': 2}))
        self.assertIn(b'new_name', response.content)

    def test_delete(self):
        response = self.client.delete(
            reverse('provider_detail_view', kwargs={'pk': 3}))
        self.assertEqual(response.status_code, 204)

        response = self.client.get(
            reverse('provider_detail_view', kwargs={'pk': 3}))
        self.assertEqual(response.status_code, 404)

    def test_put(self):
        response = self.client.put(
            reverse('provider_detail_view', kwargs={'pk': 4}), {'email': 'new@gmail.com'}, content_type='application/json')
        self.assertEqual(response.status_code, 200)

        response = self.client.get(
            reverse('provider_detail_view', kwargs={'pk': 4}))
        self.assertIn(b'new@gmail.com', response.content)
