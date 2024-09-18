from django.urls import path,include
from . import views

app_name = "cbvapp"


urlpatterns = [
    path('', views.SchoolListView.as_view(), name='list'),
    path('<pk>/', views.SchoolDetailView.as_view(),name='detail'),
]
