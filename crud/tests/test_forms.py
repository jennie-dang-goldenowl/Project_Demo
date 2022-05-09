from django.test import TestCase
from crud.forms import DeveloperForm, ProjectForm

class TestForms(TestCase):
    setUp_developer={
            'first_name': 'testfirstname',
            'last_name': 'testlastname',
            'language': 'python',
            'project': 'test'
        }
    setUp_project={
            'name': 'test',
            'description': 'test',
            'start_date': '2022-02-02',
            'end_date': '2011-02-02',
            'cost': 100
        }
    def test_developer_valid_data(self):
        form = DeveloperForm(data=self.setUp_developer)
        self.assertTrue(form.is_valid)

    def test_developer_form_no_data(self):
        form = DeveloperForm(data={})
        self.assertFalse(form.is_valid())
        self.assertEquals(len(form.errors), 4)

    def test_project_valid_data(self):
        form = ProjectForm(data=self.setUp_project)
        self.assertTrue(form.is_valid)

    def test_project_form_no_data(self):
        form = ProjectForm(data={})
        self.assertFalse(form.is_valid())
        self.assertEquals(len(form.errors), 6)
