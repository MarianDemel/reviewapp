from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('place/<int:place_id>/', views.place_detail, name='place_detail'),
    path('place/<int:place_id>/add-review/', views.add_review, name='add_review'),
]
