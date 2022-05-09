from django.test import TestCase
from crud.models import Developer, Project

class DeveloperModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        Developer.objects.create(first_name='Big', last_name='Bob', language='Python')

    def test_first_name_label(self):
        developer = Developer.objects.get(id=1)
        field_label = developer._meta.get_field('first_name').verbose_name
        self.assertEqual(field_label, 'first name')

    def test_last_name_label(self):
        developer = Developer.objects.get(id=1)
        field_label = developer._meta.get_field('last_name').verbose_name
        self.assertEqual(field_label, 'last_name')

    def test_first_name_max_length(self):
        developer = Developer.objects.get(id=1)
        max_length = developer._meta.get_field('first_name').max_length
        self.assertEqual(max_length, 256)

    def test_last_name_max_length(self):
        developer = Developer.objects.get(id=1)
        max_length = developer._meta.get_field('last_name').max_length
        self.assertEqual(max_length, 256)

    