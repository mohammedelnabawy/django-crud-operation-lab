from django.urls import path , include

    # from . import views
import contact.views
from contact.views import contact 


urlpatterns = [
    path("", contact, name="contact"),
]