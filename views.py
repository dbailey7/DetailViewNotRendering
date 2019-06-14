from django.shortcuts import render;
from cmpbltrapp.forms import mp_archetype_model_form, mp_element_model_form;
from django.views.generic import TemplateView, ListView, DetailView;  # For the cbv's
from . import models;

# Create your views here ...

# Here is a Template cbv ...
class IndexView(TemplateView):
    template_name = 'cmpbltrapp/index.html';
    # **kwargs info: https://stackoverflow.com/questions/36901/what-does-double-star-and-star-do-for-parameters
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs);
        context['injectMeId'] = "Here's some text for injection!";
        return context;

# Here are mp_archetype's and mp_elements's List and Detail cbv's ...
class mp_archetypeListView(ListView):
    # context_object_name mp_archetype_list gets generated automagically,
    # but if you want to specity your own context name, then ...
    context_object_name = 'mp_archs';
    model = models.mp_archetype;
    # mp_archeype_list gets generated automagically!

class mp_archetypeDetailView(DetailView):
    context_object_name = 'mp_archetype_detail';
    model = models.mp_archetype;
    template_name = 'cmpbltrapp/mp_archetype_detail.html';

class mp_elementListView(ListView):
    # context_object_name mp_element_list gets generated automagically,
    # but if you want to specity your own, then ...
    context_object_name = 'mp_elems';
    model = models.mp_element;

class mp_elementDetailView(DetailView):
    context_object_name = 'mp_element_detail';
    model = models.mp_element;
    template_name = 'cmpbltrapp/mp_element_detail.html';

def index(request):
    return render(request, 'cmpbltrapp/index.html');

def mp_archetype_form_view(request):
    form = mp_archetype_model_form();

    # Check to see if we get a POST back ...
    if request.method == 'POST':
        # In which case we pass in the request.
        form = mp_archetype_model_form(request.POST);

        # Check to see if form is valid.
        if form.is_valid():
            form.save(commit=True);
            return index(request);
        else:
            print('Error: mp_archetype_model_form is invalid!');
    return render(request, 'cmpbltrapp/mp_archetype_form.html', {'form': form});

def mp_element_form_view(request):
    form = mp_element_model_form();

    # Check to see if we get a POST back ...
    if request.method == 'POST':
        # In which case we pass in the request.
        form = mp_element_model_form(request.POST);

        # Check to see if form is valid.
        if form.is_valid():
            form.save(commit=True);
            return index(request);
        else:
            print('Error: mp_element_model_form is invalid!');
    return render(request, 'cmpbltrapp/mp_element_form.html', {'form': form});
