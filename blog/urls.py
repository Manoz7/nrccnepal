from django.urls import path
from blog import views

urlpatterns = [
    path("", views.blog, name="blog"),
	path("details/", views.single_blog, name="single_blog"),

]