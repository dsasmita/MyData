from django.urls import path

from . import views

app_name = 'dataset'
urlpatterns = [
    path('', views.HomeView.as_view(), name='index'),
    path('dataset-<int:pk>', views.DetailView.as_view(), name='detail'),
    path('dataset-download-<int:pk>', views.DetailViewDownload.as_view(), name='download'),
]