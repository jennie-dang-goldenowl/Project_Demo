from django.test import TransactionTestCase
from django.urls import reverse
from crud.models import Project, Developer

class TestModels(TransactionTestCase):
    def setUp(self):
        self.pro=Project.objects.create(
            name="test",
            description="test",
            start_date="2022-04-05",
            end_date="2022-05-07",
            cost=100,
        )
        self.dev= Developer.objects.create(
            first_name= "test0905",
            last_name= "yeh",
            language="python",
            project='test'
        )

    def test_developer_create(self):
        self.assertEqual(Developer.objects.filter(first_name="test0905").count(),1)

    def test_project_create(self):
        self.assertEqual(Project.objects.all().count(),1)

        