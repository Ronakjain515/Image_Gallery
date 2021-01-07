from django.urls import path
from . import views
urlpatterns = [
    path('', views.index, name="index"),
    path('<str:ImagePost>', views.viewDetailsPost, name="viewDetailsPost"),
]
