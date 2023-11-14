from django.urls import path
from django.conf.urls.static import static
from core_project.settings import DEBUG, MEDIA_URL, MEDIA_ROOT
from .views import HomeView
from .person_views import PersonListView, PersonDetailView, PersonCreateView, PersonUpdateView, PersonDeleteView
from .referral_views import ReferralListView, ReferralDetailView, ReferralCreateView, ReferralUpdateView, ReferralDeleteView

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('people/', PersonListView.as_view(), name='person_list'),
    path('people/<int:pk>/', PersonDetailView.as_view(), name='person_detail'),
    path('people/new/', PersonCreateView.as_view(), name='person_new'),
    path('people/<int:pk>/edit/', PersonUpdateView.as_view(), name='person_edit'),
    path('people/<int:pk>/delete/', PersonDeleteView.as_view(), name='person_delete'),
    path('referral/', ReferralListView.as_view(), name='referral_list'),
    path('referral/<int:pk>/', ReferralDetailView.as_view(), name='referral_detail'),
    path('referral/new/', ReferralCreateView.as_view(), name='referral_new'),
    path('referral/<int:pk>/edit/', ReferralUpdateView.as_view(), name='referral_edit'),
    path('referral/<int:pk>/delete/', ReferralDeleteView.as_view(), name='referral_delete'),
    
        
]

# Add media url and root for development
if DEBUG:
    urlpatterns += static(MEDIA_URL, document_root=MEDIA_ROOT)