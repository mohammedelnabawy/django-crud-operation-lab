from django.urls import path , include

    # from . import views
import polls.views 
from polls.views import index 


urlpatterns = [
    path("", index, name="index"),
]