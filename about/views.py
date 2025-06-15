from django.shortcuts import render
from django.contrib import messages
from .models import About
from .forms import CollaborateForm

# Create your views here.
def about_me(request):
    """
    Handles the rendering of the About page and processing of collaboration requests.

    GET:
        - Retrieves the most recently updated About entry from the database.
        - Renders the About page with the content and an empty collaboration form.

    POST:
        - Accepts submitted collaboration requests from users.
        - Validates and saves the request if valid.
        - Displays a success message to the user.

    Context:
        about (About): The latest About page content.
        collaborate_form (CollaborateForm): The form for submitting collaboration requests.

    Returns:
        HttpResponse: Rendered 'about/about.html' template with context data.
    """

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
