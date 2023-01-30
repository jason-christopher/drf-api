from django.urls import path
from .views import HomeList, HomeDetail


urlpatterns = [
    path('', HomeList.as_view(), name='home_list'),
    path('<int:pk>/', HomeDetail.as_view(), name='home_detail'),
]
