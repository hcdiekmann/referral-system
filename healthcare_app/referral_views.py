
from django.views.generic import CreateView, UpdateView, DetailView, DeleteView, ListView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from .models import Person, Referral
from .forms import ReferralForm


class ReferralListView(LoginRequiredMixin, ListView):
    model = Referral
    template_name = 'referral_list.html'
    paginate_by = 10


class ReferralDetailView(LoginRequiredMixin, DetailView):
    model = Referral
    template_name = 'referral_detail.html'


class ReferralCreateView(LoginRequiredMixin, CreateView):
    model = Referral
    form_class = ReferralForm
    template_name = 'referral_form.html'

    def form_valid(self, form):
        person_id = self.kwargs.get('person_id')
        form.instance.person = Person.objects.get(pk=person_id)
        form.instance.user = self.request.user
        return super().form_valid(form)
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['action'] = 'Create'
        return context

    def get_success_url(self):
        return reverse_lazy('referral_detail', kwargs={'pk': self.object.pk})


class ReferralUpdateView(LoginRequiredMixin, UpdateView):
    model = Referral
    form_class = ReferralForm
    template_name = 'referral_form.html'

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy('referral_detail', kwargs={'pk': self.object.pk})
 
    
class ReferralDeleteView(LoginRequiredMixin, DeleteView):
    model = Referral
    template_name = 'referral_confirm_delete.html'
    success_url = reverse_lazy('referral_list')