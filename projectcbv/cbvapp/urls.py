from django.urls import path,include
from . import views

app_name = "cbvapp"


urlpatterns = [
    path('', views.SchoolListView.as_view(), name='list'),
]
