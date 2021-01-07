from django.shortcuts import render
from .models import ImagePost
from django.core.paginator import Paginator

# Create your views here.


def index(request):
    imagePost = ImagePost.objects.all().order_by("id")
    paginator = Paginator(imagePost, 8)
    page_no = request.GET.get("page")
    page_image = paginator.get_page(page_no)
    return render(request, "index.html", context= {"imagePost": page_image})


def viewDetailsPost(request, ImagePost):
    print(ImagePost)
    return render(request, "DetailPage.html")
