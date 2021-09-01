from django.db.models.query import QuerySet
from django.shortcuts import render, redirect
from django.views.generic import ListView,DetailView,CreateView,DeleteView,UpdateView
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator


from .models import artikel
from .forms import artikelForm


#@login_required(login_url='login')
class artikelUpdateView(UpdateView):
    form_class = artikelForm
    model = artikel
    template_name = "artikel/artikel_update.html"

    @method_decorator(login_required(login_url='login'))
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)


#@login_required(login_url='login')
class artikelDeleteView(DeleteView):
    model = artikel
    template_name = "artikel/artikel_delete_confirmation.html"
    success_url = reverse_lazy('artikel:manage')

    @method_decorator(login_required(login_url='login'))
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)


#@login_required(login_url='login')
class artikelManageView(ListView):
    model = artikel
    template_name = "artikel/artikel_manage.html"
    context_object_name = 'artikel_list'

    @method_decorator(login_required(login_url='login'))
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)


#@login_required(login_url='login')
#@method_decorator(login_required(login_url='category'))
class artikelCreateView(CreateView):
    form_class = artikelForm
    template_name = 'artikel/artikel_create.html'

    @method_decorator(login_required(login_url='login'))
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)


class ArtikelPerkategori():
    model = artikel

    def get_latest_artikel_each_kategori(self):
        kategori_list = self.model.objects.values_list('kategori', flat=True).distinct()
        QuerySet = []

        for kategori in kategori_list:
            artikel = self.model.objects.filter(kategori=kategori).latest('published')
            QuerySet.append(artikel)

        return QuerySet


class artikelkategoriListView(ListView):
    model = artikel
    template_name = 'artikel/artikel_kategori_list.html'
    context_object_name = 'artikel_list'
    ordering = ['published']
    paginate_by = 3

    def get_queryset(self):
        self.queryset = self.model.objects.filter(kategori=self.kwargs['kategori'])
        return super().get_queryset()
    
    def get_context_data(self, **kwargs):
        kategori_list = self.model.objects.values_list('kategori', flat=True).distinct().exclude(kategori=self.kwargs['kategori'])
        self.kwargs.update({'kategori_list':kategori_list})
        kwargs = self.kwargs
        
        return super().get_context_data(**kwargs)

class artikelistView(ListView):
    model = artikel
    template_name = "artikel/artikel_list.html"
    context_object_name ='artikel_list'
    oredering = ['published']
    paginate_by = 3

    def get_context_data(self, **kwargs):
        kategori_list = self.model.objects.values_list('kategori', flat=True).distinct()
        self.kwargs.update({'kategori_list':kategori_list})
        kwargs = self.kwargs
        
        return super().get_context_data(**kwargs)
    


class artikelDetailView(DetailView):
    model = artikel
    template_name = "artikel/artikel_detail.html"
    context_object_name = 'artikel'

    def get_context_data(self, **kwargs):
        kategori_list = self.model.objects.values_list('kategori', flat=True).distinct()
        self.kwargs.update({'kategori_list':kategori_list})
        artikel_serupa = self.model.objects.filter(kategori=self.object.kategori).exclude(id = self.object.id)
        self.kwargs.update({'artikel_serupa':artikel_serupa})
        kwargs = self.kwargs
        return super().get_context_data(**kwargs)


    