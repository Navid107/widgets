from django.shortcuts import redirect, render
from .models import Widget
from django.views.generic import ListView
from django.views.generic.edit import CreateView, DeleteView
from .forms import WidgetForm

# Create your views here.



class WidgetCreate(CreateView):
    model = Widget
    fields = ['Description', 'Quantity']
    success_url = '/'

class WidgetDelete(DeleteView):
  model = Widget
  success_url = '/'

def home(request):
  return render(request, 'home.html')


def widgets_index(request):
    widgets = Widget.objects.all()
    widgets_form = WidgetForm()
    return redirect(request, 'home.html', { 'widgets': widgets, 'widgets_form': widgets_form })