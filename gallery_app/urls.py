from django.urls import path
from . import views
urlpatterns = [
    path('', views.index, name="index"),
    path('Post/<str:ImagePostParameter>', views.viewDetailsPost, name="viewDetailsPost"),
    path('SaveAngle', views.saveImageAngle, name="SaveImageAngle"),
]
