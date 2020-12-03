from django.test import SimpleTestCase

class ViewTests(SimpleTestCase):

    def test_index_view(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        
        response = self.client.get('hulk')
        self.assertEqual(response.status_code, 200)