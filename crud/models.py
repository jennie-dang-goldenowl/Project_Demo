from django.db import models
from django.urls import reverse
from django.utils.translation import gettext_lazy as _
from djmoney.models.fields import MoneyField

# Create your models here.
#Model Projects
class Project(models.Model):
    project_id = models.BigAutoField(_('project_id'),primary_key=True)
    name = models.CharField(_('name'),max_length=256)
    description = models.CharField(_('description'),max_length=256)
    start_date = models.DateField(_('start_date'))
    end_date = models.DateField(_('end_date'),)
    cost = MoneyField(max_digits=14, decimal_places=2, default_currency='USD')
    developers = models.OneToOneField('Developer', null=True, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

info_lang = (
    ('Python', 'Python'),
    ('C++', 'C++'),
    ('Java', 'Java'),
    ('Ruby', 'Ruby'),
    ('Javascript', 'Javascript'),
    ('Others', 'Others')
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
    def __str__(self):
        return self.first_name +' '+ self.last_name