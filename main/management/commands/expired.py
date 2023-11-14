# myapp/management/commands/send_single_expired_document_reminder.py
from django.core.management.base import BaseCommand
from main.models import Registration
from django.core.mail import send_mail
import logging
import datetime

logger = logging.getLogger(__name__)

class Command(BaseCommand):
    help = 'Send reminders for single expired document (either visa or passport)'

    def handle(self, *args, **options):
        # Get today's date
        today = datetime.date.today()

        # Get all registrations
        registrations = Registration.objects.all()

        for registration in registrations:
            visa_expiry = registration.visa_expiry_date
            passport_expiry = registration.passport_expiry

            if visa_expiry and datetime.datetime.strptime(visa_expiry, "%Y-%m-%d").date() <= today:
                # Visa has expired
                subject = 'Important Notice: Temporary Suspension of Pakistan Association of Rwanda Membership'
                message = f'''
                Dear {registration.name},

                I hope this message finds you in good health. We are writing to inform you of a critical matter regarding your membership with the Pakistan Association of Rwanda.

                It has come to our attention that your visa has expired, and we must prioritize compliance with legal and organizational requirements. In light of this situation, we are temporarily suspending your membership with immediate effect.

                Here are the details of the suspension:

                - Visa Expiry Date: {visa_expiry}

                You have 30 days from the date of this notice to complete the renewal process for your visa. Failure to do so within this timeframe will result in the permanent suspension of your membership with the Pakistan Association of Rwanda.

                We sincerely hope that you will take the necessary actions to renew your visa and reinstate your membership with us.

                Best regards,
                Management
                Pakistan Association of Rwanda
                info@pkar.rw
                '''

            elif passport_expiry and datetime.datetime.strptime(passport_expiry, "%Y-%m-%d").date() <= today:
                # Passport has expired
                subject = 'Important Notice: Temporary Suspension of Pakistan Association of Rwanda Membership'
                message = f'''
                Dear {registration.name},

                I hope this message finds you in good health. We are writing to inform you of a critical matter regarding your membership with the Pakistan Association of Rwanda.

                It has come to our attention that your passport has expired, and we must prioritize compliance with legal and organizational requirements. In light of this situation, we are temporarily suspending your membership with immediate effect.

                Here are the details of the suspension:

                - Passport Expiry Date: {passport_expiry}

                You have 30 days from the date of this notice to complete the renewal process for your passport. Failure to do so within this timeframe will result in the permanent suspension of your membership with the Pakistan Association of Rwanda.

                We sincerely hope that you will take the necessary actions to renew your passport and reinstate your membership with us.

                Best regards,
                Management
                Pakistan Association of Rwanda
                info@pkar.rw
                '''
            else:
                continue  # Neither visa nor passport has expired for this member

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
                logger.info(f"Email sent successfully to {registration.user.email} for expired document reminder.")
            except Exception as e:
                logger.error(f"Failed to send an email to {registration.user.email}: {e}")
