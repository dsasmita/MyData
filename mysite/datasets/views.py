from django.views import generic

from .models import Dataset


class HomeView(generic.ListView):
    template_name = 'datasets/home.html'
    context_object_name = 'datasets_list'
    paginate_by = 12

    def get_queryset(self):
        sch = Dataset.objects
        keyword = self.request.GET.get('keyword') or ''
        if keyword != '':
            sch = sch.filter(title__icontains=keyword)
        sorting = self.request.GET.get('sort') or ''
        if sorting == 'popular':
            sch = sch.order_by('-seen_count')
        elif sorting == 'update':
            sch = sch.order_by('-updated_at')
        else:
            sch = sch.order_by('-published_at')
        return sch

    def get_context_data(self, **kwargs):
        keyword = self.request.GET.get('keyword') or ''
        sort = self.request.GET.get('sort') or ''

        context = super(HomeView, self).get_context_data(**kwargs)

        context['title'] = 'MyData - Dataset Collection'
        context['sort'] = sort
        context['keyword'] = keyword

        return context


class DetailView(generic.DetailView):
    model = Dataset
    template_name = 'datasets/detail.html'

    def get_context_data(self, **kwargs):
        context = super(DetailView, self).get_context_data(**kwargs)
        self.object.update_counter_seen()

        context['popular'] = Dataset.objects.order_by('-seen_count')[:5]
        context['title'] = 'Dataset - ' + self.object.title

        return context

class DetailViewDownload(generic.DetailView):
    model = Dataset
    template_name = 'datasets/download.html'

    def get_context_data(self, **kwargs):
        context = super(DetailViewDownload, self).get_context_data(**kwargs)
        self.object.update_counter_download()

        context['title'] = 'Download - ' + self.object.title

        return context