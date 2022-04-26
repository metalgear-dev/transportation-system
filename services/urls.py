
from services.views import AreaView, AreaDetailView, ProviderView, ProviderDetailView
from django.urls import path

urlpatterns = [
    path('providers', ProviderView.as_view(), name="provider"),
    path('providers/<int:pk>', ProviderDetailView.as_view(),
         name="provider_detail"),
    path('areas', AreaView.as_view(), name="area"),
    path('areas/<int:pk>', AreaDetailView.as_view(), name="area_detail"),
]
