
from services.views import ProviderView, ProviderDetailView
from django.urls import path

urlpatterns = [
    path('providers', ProviderView.as_view(), name="provider_view"),
    path('providers/<int:pk>', ProviderDetailView.as_view(),
         name="provider_detail_view"),
]
