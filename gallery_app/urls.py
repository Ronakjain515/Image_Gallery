from django.urls import path
from . import views
urlpatterns = [
    path('', views.index, name="index"),
    path('Post/<str:ImagePostParameter>', views.viewDetailsPost, name="viewDetailsPost"),
    path('SaveAngle', views.saveImageAngle, name="SaveImageAngle"),
    path('searchTag', views.searchTag, name="searchTag"),
    path('isTagComplete', views.isTagComplete, name="isTagComplete"),
    path('AddImagePost', views.addImagePost, name="addImagePost"),
    path('AddImagePost_Submit', views.addImagePost_Submit, name="AddImagePost_Submit"),
]
