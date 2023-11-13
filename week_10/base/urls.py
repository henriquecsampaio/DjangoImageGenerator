from django.urls import path
from .views import *

urlpatterns = [
    path('', home, name="Home"),
    path('courses', courses, name="courses"),
    path('generate_image', generate_image, name="generate_image"),
    path('get_xkcd', get_xkcd, name="get_xkcd"),
    path('get_dog', get_dog, name="get_dog"),
    path('generate_qr_code', generate_qr_code, name="generate_qr_code"),
]
