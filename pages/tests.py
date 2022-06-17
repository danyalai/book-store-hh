from django.test import TestCase
from django.urls import reverse


# Create your tests here.
class HomePageTests(TestCase):
    def test_home_page_url_by_name(self):  # is path name in urls = home
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)

    def test_home_page_content(self):  # did print ' Home page' in home.html
        response = self.client.get(reverse('home'))
        self.assertContains(response, ' Home page')

    def test_home_page_url(self):  # did home page address is ('/')
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)

    def test_home_page_template_used(self):  # did you use template with 'home.html'
        response = self.client.get(reverse('home'))
        self.assertTemplateUsed(response, 'home.html')
