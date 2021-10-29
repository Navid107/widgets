from django.shortcuts import redirect, render
from .models import Widget
from django.views.generic.edit import CreateView, DeleteView
from .forms import WidgetForm

# Create your views here.



class WidgetCreate(CreateView):
    model = Widget
    fields = '__all__'
    success_url = '/'

def widget_delete(request, widget_id):
    Widget.objects.get(id=widget_id).delete()
    return redirect('home')


def home(request):
    widgets = Widget.objects.all()
    widgets_form = WidgetForm()
    print(widgets)
    return render (request, 'home.html',
     { 'widgets': widgets, 'widgets_form': widgets_form })

def add_widget(request):
  form = WidgetForm(request.POST)
  print(form,'valid form')
  if form.is_valid():
    new_add = form.save(commit=False)
    new_add.save()
    print(new_add,'just made this')
  return redirect('home')