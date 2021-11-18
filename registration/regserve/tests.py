from django.test import TestCase, Client

class SimpleTest(TestCase):
    def setUp(self):
        self.test_client = Client()

    def test_response(self):
        response = self.test_client.get('/regserve')
        print(f'Simple response test: {response}')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.content, b'Hello world from django backend')

#Run in command line: py manage.py test

# Create your tests here.
