from django.urls import path
from core.views import index, blog, blog_details, service_details, service_pages, portfolio_details

app_name = "core"

urlpatterns = [
    path("", index, name="index"),


    path("blog/", blog, name="blog"),
    path("blog_details/", blog_details, name="blog-details"),
    path("portfolio_details/", portfolio_details, name="portfolio"),
    path("service_details/", service_details, name="service"),
    path("service_page", service_pages, name="page"),
]