from django.urls import reverse
from django.views.generic import TemplateView, ListView, DetailView, CreateView

from .models import Band, County

class HomepageView(TemplateView):
    template_name = "public_index.html"

class CountyListView(ListView):
    model = County
    context_object_name='counties'
    #template_name='county_list.html'
    # paginate_by = 10

class BandListView(ListView):
    model = Band
    context_object_name='bands'

class BandDetailView(DetailView):
    model = Band

class BandCreateView(CreateView):
    model = Band
    fields = ["name", "homecounty", "profile"]

    # def get_absolute_url(self):
    #     """Return absolute URL to the Cheese Detail page."""
    #     return reverse('band_detail', kwargs={"slug": self.slug})
    def get_success_url(self):
        return reverse("band_detail", kwargs={"slug": self.object.slug})
