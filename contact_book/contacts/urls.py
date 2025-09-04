from django.urls import path
from . import views

app_name = "contacts"



urlpatterns = [
    path("", views.contact_list, name="contact_list"),
    path("add/", views.add_contact, name="add_contact"),
    path("feedback/", views.feedback, name="feedback"),
    path("delete/<int:contact_id>/", views.delete_contact, name="delete_contact"),  # 👈 new
]
