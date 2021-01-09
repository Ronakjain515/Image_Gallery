import json

from django.http import JsonResponse
from django.shortcuts import render
from pip._vendor.requests import Response

from .models import ImagePost, Tags, Images
from django.core.paginator import Paginator

# Create your views here.


def index(request):
    page_no = 1
    tags = []
    imagePost = []

    if request.POST:
        page_no = request.POST.get("pageno")
        tagsPostData = request.POST.get("tags")
        if tagsPostData != "":
            for tag in tagsPostData.split(","):
                tags.append(tag)
            imageIdTags = Tags.objects.values("imagePostId").filter(tag__in=tags).distinct()
            imagePost = list(ImagePost.objects.values("id", "name").order_by("id").filter(id__in=imageIdTags))
        else:
            imagePost = list(ImagePost.objects.values("id", "name").order_by("id"))
    else:
        imagePost = list(ImagePost.objects.values("id", "name").order_by("id"))

    for i in range(0, len(imagePost)):
        temp = Images.objects.values("image").filter(imagePostId=imagePost[i]["id"]).first()
        imagePost[i]["mainImage"] = temp["image"]

    paginator = Paginator(imagePost, 8)
    page_image = paginator.get_page(page_no)
    return render(request, "index.html", context={"imagePost": page_image, "tags": tags})


def viewDetailsPost(request, ImagePostParameter):
    imagePostData = ImagePost.objects.values('id', 'name', 'date').filter(name=ImagePostParameter).first()
    imagePostData["mainImage"] = Images.objects.values("id", "image").filter(imagePostId=imagePostData["id"])
    print(imagePostData)
    tagData = Tags.objects.values('tag').filter(imagePostId=imagePostData["id"])
    return render(request, "DetailPage.html", context={"ImagePost": imagePostData, "tags": tagData})


def saveImageAngle(request):
    received_json_data = json.loads(request.body)
    image = Images.objects.values("image").filter(id=received_json_data["imageId"]).first()["image"]
    import PIL
    from django.conf import settings
    from PIL import Image
    import os
    im1 = Image.open(os.path.join(settings.MEDIA_ROOT, image))
    im1 = im1.rotate(-received_json_data["angle"], PIL.Image.NEAREST, expand=1)
    im1.save(os.path.join(settings.MEDIA_ROOT, image))
    return JsonResponse({"result": "true"})

def searchTag(request):
    searchData = request.GET.get("term")
    result = list(Tags.objects.values_list("tag", flat=True).filter(tag__contains=searchData).distinct())
    return JsonResponse(result, safe=False)

def isTagComplete(request):
    result = "false"
    try:
        tagData = json.loads(request.body)["tagData"]
        tagCount = Tags.objects.filter(tag__iexact=tagData).count()
        if tagCount > 0:
            print(tagCount)
            result = "true"
    except:
        pass
    return JsonResponse({"result": result})
