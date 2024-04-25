# myapp/urls.py
from django.urls import path
from .views import EmployeeStatsView, EmployeeDetailsView
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView

urlpatterns = [
    path('employees', EmployeeStatsView.as_view(), name='employee-stats'),
    path('employees/<int:user>', EmployeeDetailsView.as_view(), name='employee-details'),
    path('api-spec.yaml', SpectacularAPIView.as_view(), name='schema'),
    path('docs', SpectacularSwaggerView.as_view(url_name='schema'), name='Employee API Documentation'),
]
