import json

from django.http import JsonResponse
from django.shortcuts import render
from .models import ImagePost, Tags, Images
from django.core.paginator import Paginator

# Create your views here.


def index(request):
    imagePost = list(ImagePost.objects.values("id", "name").order_by("id"))
    for i in range(0, len(imagePost)):
        temp = Images.objects.values("image").filter(imagePostId=imagePost[i]["id"]).first()
        try:
            imagePost[i]["mainImage"] = temp["image"]
        except:
            pass
    paginator = Paginator(imagePost, 8)
    page_no = request.GET.get("page")
    page_image = paginator.get_page(page_no)
    return render(request, "index.html", context={"imagePost": page_image})


def viewDetailsPost(request, ImagePostParameter):
    imagePostData = ImagePost.objects.values('id', 'name', 'date').filter(name=ImagePostParameter).first()
    imagePostData["mainImage"] = Images.objects.values("id", "image").filter(imagePostId=imagePostData["id"]).first()
    tagData = Tags.objects.values('tag').filter(imagePostId=imagePostData["id"])
    return render(request, "DetailPage.html", context={"ImagePost": imagePostData, "tags": tagData})


def saveImageAngle(request):
    received_json_data = json.loads(request.body)
    print(received_json_data)
    image = Images.objects.values("image").filter(id=received_json_data["imageId"]).first()["image"]
    print(image)
    import PIL
    from django.conf import settings
    from PIL import Image
    import os
    im1 = Image.open(os.path.join(settings.MEDIA_ROOT, image))
    im1 = im1.rotate(-received_json_data["angle"], PIL.Image.NEAREST, expand=1)
    im1.save(os.path.join(settings.MEDIA_ROOT, image))
    return JsonResponse({"result": "true"})