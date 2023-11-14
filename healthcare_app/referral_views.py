
from django.views.generic import CreateView, UpdateView, DetailView, DeleteView, ListView
from django.urls import reverse_lazy
from .models import Referral
from .forms import ReferralForm


class ReferralListView(ListView):
    model = Referral
    template_name = 'referral_list.html'


class ReferralDetailView(DetailView):
    model = Referral
    template_name = 'referral_detail.html'


class ReferralCreateView(CreateView):
    model = Referral
    form_class = ReferralForm
    template_name = 'referral_form.html'

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['action'] = 'Create'
        return context

    def get_success_url(self):
        return reverse_lazy('referral_detail', kwargs={'pk': self.object.pk})


class ReferralUpdateView(UpdateView):
    model = Referral
    form_class = ReferralForm
    template_name = 'referral_form.html'

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy('referral_detail', kwargs={'pk': self.object.pk})
 
    
class ReferralDeleteView(DeleteView):
    model = Referral
    template_name = 'referral_confirm_delete.html'
    success_url = reverse_lazy('referral_list')

    def delete(self, request, *args, **kwargs):
        return super().delete(request, *args, **kwargs)