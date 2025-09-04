from django.db.models.signals import post_save
from django.dispatch import receiver
from django.core.mail import mail_admins
from .models import Contact

@receiver(post_save, sender=Contact)
def notify_admin_new_contact(sender, instance, created, **kwargs):
    if created:
        subject = "📘 New Contact Added"
        message = f"A new contact has been added by {instance.user.username}:\n\n" \
                  f"Name: {instance.name}\n" \
                  f"Email: {instance.email}\n" \
                  f"Phone: {instance.phone}"
        mail_admins(subject, message)
