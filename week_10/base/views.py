from django.shortcuts import render
from django.http import HttpResponse
import requests
from random import randint
# Create your views here.

def home(request):
    return render(request, "home.html")

def courses(request):
    courses = [
        {"id":1, "name": "Python"},
        {"id":2, "name": "JavaScript"},
        {"id":3, "name": "C++"}
    ]
    context = {
        "courses" : courses
    }

    return render(request, "courses.html", context)

def generate_image(request):
    if request.method == "POST":
        print(request.POST)
        width = request.POST.get("width")
        height = request.POST.get("height")
        grayscale = request.POST.get("grayscale")
        blur = request.POST.get("blur") or 0

        param_string = ""

        blur = blur if int(blur) >= 1 and int(blur) <= 10 else None

        if blur and grayscale:
            param_string += f"?blur={blur}&grayscale"
        elif blur:
            param_string += f"?blur={blur}"
        elif grayscale:
            param_string += f"?grayscale"

        picsum_url = f"https://picsum.photos/{width}/{height}{param_string}"
        print(picsum_url)

        context = {
            "picsum_url":picsum_url
        }

        return render(request, "generate_image.html", context)
    else:
        return render(request, "generate_image.html")

def get_xkcd(request):
    if request.method == "POST":
        comic_id = request.POST.get("comic_id")

        if comic_id == "":
            comic_id = randint(1, 2500)
            comic_url = f"https://xkcd.com/{comic_id}/info.0.json"
        else: 
            comic_url = f"https://xkcd.com/{comic_id}/info.0.json"

        response = requests.get(comic_url)

        comic_data = response.json()

        img_url = comic_data.get("img")

        context = {
            "img_url": img_url
        }

        return render(request, "get_xkcd.html", context)
    return render(request, "get_xkcd.html")

def get_dog(request):
    if request.method == "POST":
        breed = request.POST.get("breed")
        subreed = request.POST.get("subreed")
        
        if breed == "" and subreed == "":
            dog_url = f"https://dog.ceo/api/breeds/image/random"
        elif breed != "" and subreed == "":
            dog_url = f"https://dog.ceo/api/breed/{breed}/images/random"
        else:
            dog_url = f"https://dog.ceo/api/breed/{breed}/{subreed}/images/random"

        response = requests.get(dog_url)
        dog_data = response.json()
        img_url = dog_data.get("message")


        context = {
            "img_url":img_url
        }

        return render(request, "get_dog.html", context)
    return render(request, "get_dog.html")

def generate_qr_code(request):
    if request.method == "POST":
        height = request.POST.get("height")
        width = request.POST.get("width")
        value = request.POST.get("value")
        img_url = f"https://image-charts.com/chart?chs={height}x{width}&cht=qr&chl={value}&choe=UTF-8"

        context = {
            'img_url': img_url
        }

        return render(request, "generate_qr_code.html", context)
    
    return render(request, "generate_qr_code.html")