from django.shortcuts import render
from django.views.generic import (View,
                                  TemplateView,
                                  ListView,
                                  DetailView,
                                  CreateView,
                                  UpdateView,
                                  DeleteView)



from . import models


class IndexView(TemplateView):
    template_name = 'index.html'


class SchoolListView(ListView):
    context_object_name = "schools"
    model = models.School


class SchoolDetailView(DetailView):
    context_object_name = "school_detail"
    model = models.School
    template_name = 'cbvapp/school_detail.html'

class SchoolCreateView(CreateView):
    model = models.School
    fields = ["name","principal","location"]
    

class SchoolUpdateView(UpdateView):
    fields = ['name','principal','location']
    model = models.School

class CarCreateView(CreateView):
    model = models.Car
    fields = ["brand","license_plate","manufacturing_year"]
    



