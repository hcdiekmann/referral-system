from django.views.generic import CreateView, UpdateView, DetailView, DeleteView, ListView
from django.urls import reverse_lazy
from .models import Person
from .forms import PersonForm


class PersonListView(ListView):
    model = Person
    template_name = 'person_list.html'


class PersonDetailView(DetailView):
    model = Person
    template_name = 'person_detail.html'


class PersonCreateView(CreateView):
    model = Person
    form_class = PersonForm
    template_name = 'person_form.html'
    success_url = reverse_lazy('person_list')
    
    def form_valid(self, form):
        form.instance.created_by = self.request.user
        return super().form_valid(form)
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['action'] = 'Create'
        return context


class PersonUpdateView(UpdateView):
    model = Person
    fields = ['first_name', 'last_name', 'phone_number', 'date_of_birth']
    template_name = 'person_form.html'  # same form for create and update
    
    def get_success_url(self):
        return reverse_lazy('person_detail', kwargs={'pk': self.object.pk})


class PersonDeleteView(DeleteView):
    model = Person
    success_url = reverse_lazy('person_list')
    template_name = 'person_confirm_delete.html'