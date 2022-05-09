from django.test import TestCase
from django.urls import reverse, resolve
from crud.views import *

class TestURLs(TestCase):
    def test_project_list_url_resolved(self):
        url = reverse('project_list')
        self.assertEqual(resolve(url).func.view_class, ProjectListView)

    def test_project_create_url_resolved(self):
        url = reverse('project_create')
        self.assertEqual(resolve(url).func.view_class, ProjectCreateView)

    def test_developer_create_url_resolved(self):
        url = reverse('developer_create')
        self.assertEqual(resolve(url).func.view_class, DeveloperCreateView)

    def test_project_update_url_resolved(self):
        url = reverse('project_update', args=(20,))
        self.assertEqual(resolve(url).func.view_class, ProjectUpdateView)

    def test_developer_update_url_resolved(self):
        url = reverse('developer_update', args=(20,))
        self.assertEqual(resolve(url).func.view_class, DeveloperUpdateView)

    def test_project_search_url_resolved(self):
        url = reverse('project_search_list_view')
        self.assertEqual(resolve(url).func.view_class, ProjectSearchListView)

    def test_project_search_date_url_is_resolved(self):
        url = reverse('project_filter_list_view')
        self.assertEqual(resolve(url).func.view_class, ProjectFilterListView)
