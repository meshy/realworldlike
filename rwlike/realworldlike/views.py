from django.views.generic import CreateView

from realworldlike.models import PrintRun, Spot

# Create your views here.

class PrintRunCreateView(CreateView):
    model = PrintRun

class SpotCreateView(CreateView):
    model = Spot
