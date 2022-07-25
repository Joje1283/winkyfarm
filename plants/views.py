from .models import Plant
from django.views.generic import DetailView


class PlantDetailView(DetailView):
    model = Plant

    def get_context_data(self, **kwargs):
        context = super(PlantDetailView, self).get_context_data(**kwargs)
        return context
