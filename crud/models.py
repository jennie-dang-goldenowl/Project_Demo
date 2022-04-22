from django.db import models
from django.urls import reverse

# Create your models here.
#Model Projects
class Project(models.Model):
    project_id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=256)
    description = models.CharField(max_length=256)
    start_date = models.DateField()
    end_date = models.DateField()
    cost = models.FloatField()
    developers = models.OneToOneField('Developer', null=True, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

info_lang = (
    ('Python', 'Python'),
    ('C++', 'C++'),
    ('Java', 'Java'),
    ('Ruby', 'Ruby'),
    ('Javascript', 'Javascript'),
)

#Model Developer_
class Developer(models.Model):
    developer_id = models.BigAutoField(primary_key=True)
    first_name = models.CharField(max_length=256)
    last_name = models.CharField(max_length=256)
    projects = models.OneToOneField(Project, null=True, blank=True, on_delete=models.CASCADE)
    language = models.TextField(
            max_length=50,
            choices= info_lang,
            default= '1'
    )

    def get_absolute_url(self):
        return reverse('project_list')

    def __str__(self):
        return self.first_name +' '+ self.last_name