from django.shortcuts import render
from django.contrib import messages
from .models import About
from .forms import CollaborateForm

# Create your views here.
def about_me(request):

    queryset = About.objects.order_by("-updated_on").first()
    about_page = queryset

    if request.method == "POST":
        collaborate_form = CollaborateForm(data=request.POST)
        if collaborate_form.is_valid():
            collaborate_form.save()
            messages.add_message(
                request, messages.SUCCESS,
                'Collaboration request received! I endeavour to respond within 2 working days.'
            )

    collaborate_form = CollaborateForm()
    return render(
        request,
        "about/about.html",
        {"about": about_page,
         "collaborate_form": collaborate_form,}
    )
