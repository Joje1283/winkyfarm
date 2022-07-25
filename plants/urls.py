from django.urls import path
from .views import PlantDetailView

app_name = "plants"

urlpatterns = [
    path("<int:pk>/", PlantDetailView.as_view(), name="plant_detail")
]