from django.views.generic import CreateView, ListView, UpdateView, DeleteView
from django.shortcuts import render
from django.core.paginator import Paginator
from .models import Project, Developer
from .forms import ProjectForm, DeveloperForm
from django.urls import reverse_lazy
#from bootstrap_datepicker_plus.widgets import DateTimePickerInput

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
    template_name = 'crud/project_form.html'
    form_class = ProjectForm
    success_url = reverse_lazy('project_list')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(ProjectUpdateView, self).form_valid(form)

class DeveloperUpdateView(UpdateView):
    model = Developer
    template_name_suffix = '_form'
    form_class = DeveloperForm
    success_url = reverse_lazy('developer_list')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(DeveloperUpdateView, self).form_valid(form)
class ProjectDeleteView(DeleteView):
    model = Project
    template_name = "crud/project_delete.html"
    success_url = reverse_lazy('project_list')

    def get_context_data(self, **kwargs):
        context = super(ProjectDeleteView, self).get_context_data(**kwargs)
        return context
class DeveloperDeleteView(DeleteView):
    model = Developer
    template_name = "crud/developer_delete.html"
    success_url = reverse_lazy('developer_list')

    def get_context_data(self, **kwargs):
        context = super(DeveloperDeleteView, self).get_context_data(**kwargs)
        return context
class ProjectListView(ListView):
    model = Project
    field_list = [
        'Project Name', 'Description', 'Start Date', 'End Date', 'Developer'
    ]
    context_object_name = 'project_list'
    paginate_by = 10
    queryset = Project.objects.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['field_list'] = self.field_list
        return context
    
    def listing(request):
        project_list = Project.objects.all()
        paginator = Paginator(project_list, 25) # Show 25 contacts per page.
        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)
        return render(request, 'project_list.html', {'page_obj': page_obj})

class DeveloperListView(ListView):
    model = Developer
    field_list = [
        'First Name', 'Last Name', 'Project'
    ]
    context_object_name = 'developer_list'
    paginate_by = 10
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['field_list']   =   self.field_list
        return context
