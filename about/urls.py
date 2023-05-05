from django.urls import path , include

    # from . import views
import about.views
from about.views import about 


urlpatterns = [
    path("", about, name="about"),
]