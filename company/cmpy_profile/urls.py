from django.urls import path
from . import views

urlpatterns = [
    path("",views.Home, name="Home"),
    path("services/",views.Services, name="Services"),
    path("about/",views.About, name="About"),
    path("contact/",views.Contacts, name="Contact"),
    path("blog/",views.Blog, name="Blog"),
    path("web_dev/",views.Webapp, name="Webapp"),
    path("mob_dev/",views.Mobapp, name="Mobapp"),
    path("cloud/",views.Cloud, name="Cloud"),
    path("video_edit/",views.Video_edit, name="Video_edit"),
    path("cms/",views.Cms, name="Cms"),
    path("ui_ux/",views.Ui_Ux, name="Ui_Ux"),
    path("hdr/",views.Hdr, name="Hdr"),
    path("submission/",views.submission, name="Submission"),
]