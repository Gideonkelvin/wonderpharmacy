import os
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
from django.utils import timezone
from django.conf import settings
from core.models import ContactUs

class EmailService:
    @classmethod
    def send_contact_form_emails(cls, contact : ContactUs):
        """
        Send confirmation email to user and notification email to admin
        
        Args:
            contact : (Contuct Us)
        """
        # Prepare context for email templates
        context = {
            'name': contact.name.capitalize(),
            'email': contact.email,
            'subject': contact.subject,
            'message': contact.message,
            'current_year': timezone.now().year,
            'submitted_at': timezone.now().strftime("%Y-%m-%d %H:%M:%S")
        }
        
        # User Confirmation Email
        try:
            user_email_html = render_to_string(
                'emails/user_contact_confirmation.html', 
                context
            )
            
            user_email = EmailMultiAlternatives(
                subject='Contact Form Submission Confirmation',
                body='Thank you for contacting us.',
                from_email=settings.DEFAULT_FROM_EMAIL,
                to=[contact.email],
                reply_to=[settings.DEFAULT_FROM_EMAIL]
            )
            
            
            user_email.attach_alternative(user_email_html, "text/html")
            user_email.send()
        except Exception as e:
            print(f"Error sending user confirmation email: {e}")
        
        # Admin Notification Email
        try:
            admin_email_html = render_to_string(
                'emails/admin_contact_notification.html', 
                context
            )
            
            admin_email = EmailMultiAlternatives(
                subject='New Contact Form Submission',
                body='A new contact form has been submitted.',
                from_email=settings.DEFAULT_FROM_EMAIL,
                to=[settings.ADMIN_EMAIL],
                reply_to=[contact.email]
            )
            
            admin_email.attach_alternative(admin_email_html, "text/html")
            admin_email.send()
        except Exception as e:
            print(f"Error sending admin notification email: {e}")