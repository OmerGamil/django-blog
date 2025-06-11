from django.shortcuts import render, get_object_or_404
from .models import About

# Create your views here.
def about_me(request):

    queryset = About.objects.order_by("-updated_on").first()
    about_page = queryset

    return render(
        request,
        "about/about.html",
        {"about": about_page}
    )
