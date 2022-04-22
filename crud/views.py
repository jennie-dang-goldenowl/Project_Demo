from django.shortcuts import render, redirect
from django.views.generic import CreateView, ListView, UpdateView, DeleteView
from .models import Project, Developer
from .forms import ProjectForm, DeveloperForm
from django.urls import reverse_lazy
from django.contrib.auth import authenticate, login

class ProjectCreateView(CreateView):
    model = Project
    form_class = ProjectForm
    success_url = reverse_lazy('project_list')
    template_name = 'crud/project_form.html'

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(ProjectCreateView, self).form_valid(form)

class DeveloperCreateView(CreateView):
    model = Developer
    form_class = DeveloperForm
    success_url = reverse_lazy('developer_list')
    template_name = 'crud/developer_form.html'

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(DeveloperCreateView, self).form_valid(form)

class ProjectUpdateView(UpdateView):
    model = Project
    template_name_suffix = '_form'
    form_class = ProjectForm
    success_url = reverse_lazy('project:project_list')

    def form_valid(self, form):
            form.instance.user = self.request.user
            return super(ProjectCreateView, self).form_valid(form)

class DeveloperUpdateView(UpdateView):
    model = Developer
    template_name_suffix = '_form'
    form_class = DeveloperForm
    success_url = reverse_lazy('developers:developer_list')

    def get_context_data(self, **kwargs):
        context = super(DeveloperUpdateView, self).get_context_data(**kwargs)
        return context

class ProjectDeleteView(DeleteView):
    model = Project
    template_name_suffix = '_delete'
    success_url = reverse_lazy('projects:project_list')

    def get_context_data(self, **kwargs):
        context = super(ProjectDeleteView, self).get_context_data(**kwargs)
        return context

class DeveloperDeleteView(DeleteView):
    model = Developer
    template_name_suffix = '_delete'
    success_url = reverse_lazy('developers:developer_list')

    def get_context_data(self, **kwargs):
        context = super(DeveloperDeleteView, self).get_context_data(**kwargs)
        return context

class ProjectListView(ListView):
    model = Project
    field_list = [
        'Project Name', 'Description', 'Start Date', 'End Date', 'Developer'
    ]
    # paginate_by = 20
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['field_list']   =   self.field_list
        return context

class DeveloperListView(ListView):
    model = Developer
    field_list = [
        'First Name', 'Last Name', 'Project'
    ]
    paginate_by = 20
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['field_list']   =   self.field_list
        return context
