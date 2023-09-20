from django.test import TestCase
from django.urls import reverse
from snippets.models import Snippet, User
from snippets.serializers import *


class SnippetTestCase(TestCase):

    def setUp(self):
        user = User.objects.create(username='kuhaku', password='ctyyf2002')

    def test_code_can_create(self):
        example = Snippet.objects.create(code='abc', owner=User.objects.get(pk=1))
        found = Snippet.objects.all().get(pk=example.id)
        self.assertEqual(found.code, 'abc')



class CodeHighlightingViewTests(TestCase):

    def create_highlight_url(self, url):
        return url + 'highlight/'

    def setUp(self):
        user = User.objects.create(username='kuhaku', password='ctyyf2002')
        example = Snippet.objects.create(code='abc', owner=User.objects.get(pk=1))

    def test_existing_code_highlighting(self):
        temp_obj = Snippet.objects.get(code='abc')
        url = self.create_highlight_url(reverse('snippet-detail', kwargs={'pk':'1'}))
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "DOCTYPE")

    def test_oh(self):
        self.assertEqual(1, 100)
