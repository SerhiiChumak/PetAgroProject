from django.urls import path
from . import views

urlpatterns = [
    # Головна сторінка
    path('', views.home_view, name='home'),

    # Списки об'єктів
    path('cultures/', views.CultureListView.as_view(), name='culture_list'),
    path('diseases/', views.DiseaseListView.as_asview(), name='disease_list'),
    path('drugs/', views.DrugListView.as_view(), name='drug_list'),

    path('cultures/<int:pk>/', views.CultureDetailView.as_view(), name='culture_detail'),
    path('diseases/<int:pk>/', views.DiseaseDetailView.as_view(), name='disease_detail'),
    path('drugs/<int:pk>/', views.DrugDetailView.as_view(), name='drug_detail'),
]
