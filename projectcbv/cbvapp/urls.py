from django.urls import path
from . import views

app_name = "cbvapp"


urlpatterns = [
    path('', views.SchoolListView.as_view(), name='list'),
    path('<pk>/', views.SchoolDetailView.as_view(),name='detail'),
    path('create/', views.SchoolCreateView.as_view(),name='create'),
    path('update/<pk>/', views.SchoolUpdateView.as_view(), name='update'),
    path('create_car/', views.CarCreateView.as_view(), name='create_car'),
    
]
