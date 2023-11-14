# myapp/management/commands/send_passport_expiry_reminders.py
from django.core.management.base import BaseCommand
from main.models import Registration
from django.core.mail import send_mail
import logging
import datetime

logger = logging.getLogger(__name__)

class Command(BaseCommand):
    help = 'Send passport expiry reminders'

    def handle(self, *args, **options):
        # Get today's date
        today = datetime.date.today()

        # Get all registrations
        registrations = Registration.objects.all()

        for registration in registrations:
            # Check if passport_expiry is provided
            if registration.passport_expiry:
                passport_expiry_date = datetime.datetime.strptime(registration.passport_expiry, "%Y-%m-%d").date()
                # Check if the passport has already expired
                if passport_expiry_date <= today:
                    print(f'{registration.name} - Passport has already expired.')
                    continue  # Passport has already expired
                days_left_passport = (passport_expiry_date - today).days

                # Check if passport is nearing expiration (e.g., within 30 days)
                if days_left_passport <= 30:
                    type_of_expiry = 'Passport'
                    expiry_date = passport_expiry_date
                    print(f'{registration.name} - Sending Passport Reminder.')
                    print(f'{registration.name} - Passport Validity: {days_left_passport} days.')

                    # Prepare the email message
                    subject = f'{type_of_expiry} Expiry Alert from Pakistan Association of Rwanda Member'
                    message = f'''
                    Dear {registration.name},

                    I hope this message finds you well. We would like to bring to your attention an important matter regarding your travel documents.

                    We have noticed that your {type_of_expiry.lower()} is nearing its expiration date, and it's crucial to take action to ensure you maintain your legal status and travel capabilities. Here are the details:

                    {type_of_expiry} Expiry Date: {expiry_date.strftime('%Y-%m-%d')}

                    To avoid any inconvenience, travel restrictions, or potential legal issues, we recommend that you initiate the renewal process for your {type_of_expiry.lower()} as soon as possible.

                    Best regards,
                    Management,
                    Pakistan Association of Rwanda.
                    info@pkar.rw
                    '''

                    # Send an email reminder
                    try:
                        from_email = 'info@pkar.rw'
                        recipient_list = [registration.user.email]  # Use the user's email field

                        send_mail(
                            subject,
                            message,
                            from_email,
                            recipient_list,
                            fail_silently=False,
                        )
                        logger.info(f"Email sent successfully to {registration.user.email} for {type_of_expiry} expiry reminder.")
                    except Exception as e:
                        logger.error(f"Failed to send an email to {registration.user.email}: {e}")
                else:
                    print(f'{registration.name} - No email to be sent for this member.')
