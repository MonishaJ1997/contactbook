from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.core.mail import send_mail
from django.conf import settings
from .models import Contact
from .forms import FeedbackForm

@login_required
def contact_list(request):
    contacts = Contact.objects.filter(user=request.user)
    return render(request, "contacts/contact_list.html", {"contacts": contacts})

@login_required
def add_contact(request):
    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        phone = request.POST.get("phone")

        Contact.objects.create(
            user=request.user,
            name=name,
            email=email,
            phone=phone
        )
        return redirect("contacts:contact_list")

    return render(request, "contacts/add_contact.html")

def feedback(request):
    if request.method == "POST":
        form = FeedbackForm(request.POST)
        if form.is_valid():
            subject = "📩 User Feedback"
            message = f"From: {form.cleaned_data['name']} <{form.cleaned_data['email']}>\n\n{form.cleaned_data['message']}"
            send_mail(subject, message, settings.DEFAULT_FROM_EMAIL, [settings.EMAIL_HOST_USER])
            return render(request, "contacts/thanks.html")
    else:
        form = FeedbackForm()

    return render(request, "contacts/feedback.html", {"form": form})

from django.shortcuts import get_object_or_404

@login_required
def delete_contact(request, contact_id):
    contact = get_object_or_404(Contact, id=contact_id, user=request.user)

    if request.method == "POST":
        contact.delete()
        return redirect("contacts:contact_list")

    return render(request, "contacts/delete_contact.html", {"contact": contact})

