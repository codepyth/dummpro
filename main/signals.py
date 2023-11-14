# myapp/signals.py
from django.db.models.signals import post_save,pre_save
from django.dispatch import receiver
from django.contrib.auth import get_user_model
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from datetime import datetime
from .models import Registration
User = get_user_model()

@receiver(post_save, sender=User)
def send_welcome_email(sender, instance, created, **kwargs):
    if created:
        # Email configuration
        smtp_server = 'mail.pkar.rw'
        smtp_port = 465
        smtp_username = 'info@pkar.rw'
        smtp_password = '@PkAr2022RW%*'
        recipient_email = instance.email  # Get the user's email address from the instance

        # Create the email message
        subject = 'Welcome! Your Signup is Confirmed'
        body = f'Dear {instance.username},\n\nCongratulations!\n\nYour signup is complete, and here are the key details:\n\n' \
               f'Name: {instance.get_full_name()}\nEmail: {instance.email}\nSignup Date: {datetime.now().strftime("%Y-%m-%d %H:%M:%S")}\n\n' \
               f'Feel free to reach out to our support team at info@pkar.rw if you have any questions or need assistance.\n\nBest regards,\nManagement\nPakistan Association of Rwanda\ninfo@pkar.rw'

        msg = MIMEMultipart()
        msg['From'] = smtp_username
        msg['To'] = recipient_email
        msg['Subject'] = subject
        msg.attach(MIMEText(body, 'plain'))

        # Connect to the SMTP server with SSL/TLS
        try:
            server = smtplib.SMTP_SSL(smtp_server, smtp_port)
            server.login(smtp_username, smtp_password)

            # Send the email
            server.sendmail(smtp_username, recipient_email, msg.as_string())
            print('Welcome email sent successfully!')
        except Exception as e:
            print('Error: Could not send welcome email -', str(e))
        finally:
            server.quit()



def send_approval_email(user_email,user_name):
    # Email configuration
    smtp_server = 'mail.pkar.rw'  # SMTP server
    smtp_port = 465  # SMTP port for SSL/TLS
    smtp_username = 'info@pkar.rw'  # Your email address
    smtp_password = '@PkAr2022RW%*'  # Your email password (replace with the actual password)

    # Create the email message
    subject = 'Registration Approved - Welcome to Pakistan Association of Rwanda'

    body = f"""
    Dear {user_email},\n

    We are delighted to inform you that your application for registration with the Pakistan Association of Rwanda has been approved. Welcome to our community!\n

    Here are the details regarding your registration:\n

    - Full Name: {user_name}\n
    - Email Address: {user_email}\n
    - Application Date: {datetime.now().strftime("%Y-%m-%d %H:%M:%S")}\n\n

    If you have any questions or need further assistance, please do not hesitate to contact our support team at info@pkar.rw.\n

    Best regards,
    Management
    Pakistan Association of Rwanda
    info@pkar.rw
    """
    msg = MIMEMultipart()
    msg['From'] = smtp_username
    msg['To'] = user_email  # Send the email to the user's email address
    msg['Subject'] = subject
    msg.attach(MIMEText(body, 'plain'))

    # Connect to the SMTP server with SSL/TLS
    try:
        server = smtplib.SMTP_SSL(smtp_server, smtp_port)
        server.login(smtp_username, smtp_password)

        # Send the email
        server.sendmail(smtp_username, user_email, msg.as_string())
        print('Approval Email sent successfully!')
    except Exception as e:
        print('Error: Could not send approval email -', str(e))
    finally:
        server.quit()

def send_rejected_email(user_email,user_name,reason):
    # Email configuration
    smtp_server = 'mail.pkar.rw'  # SMTP server
    smtp_port = 465  # SMTP port for SSL/TLS
    smtp_username = 'info@pkar.rw'  # Your email address
    smtp_password = '@PkAr2022RW%*'  # Your email password (replace with the actual password)

    # Create the email message
    subject = ' Notification: Application for Registration – Rejection and Reason'

    body = f"""
    Dear {user_name},\n

    We hope this message finds you well. We regret to inform you that your application for registration with the Pakistan Association of Rwanda has been carefully reviewed and, unfortunately, we are unable to approve your application at this time.\n
    The reason for the rejection of your application is as follows:\n
    {reason}\n

    We encourage you to address the issue mentioned and, if applicable, submit a new application once the matter has been resolved.\n

    If you have any questions or require clarification about the rejection, please feel free to contact our support team at info@pkar.rw.\n

    Sincerely,
    Management
    Pakistan Association of Rwanda
    info@pkar.rw

    """
    msg = MIMEMultipart()
    msg['From'] = smtp_username
    msg['To'] = user_email  # Send the email to the user's email address
    msg['Subject'] = subject
    msg.attach(MIMEText(body, 'plain'))

    # Connect to the SMTP server with SSL/TLS
    try:
        server = smtplib.SMTP_SSL(smtp_server, smtp_port)
        server.login(smtp_username, smtp_password)

        # Send the email
        server.sendmail(smtp_username, user_email, msg.as_string())
        print('Approval Email sent successfully!')
    except Exception as e:
        print('Error: Could not send approval email -', str(e))
    finally:
        server.quit()


def send_pending_email(user_email,user_name):
    # Email configuration
    smtp_server = 'mail.pkar.rw'  # SMTP server
    smtp_port = 465  # SMTP port for SSL/TLS
    smtp_username = 'info@pkar.rw'  # Your email address
    smtp_password = '@PkAr2022RW%*'  # Your email password (replace with the actual password)

    # Create the email message
    subject = 'Application Submitted for Registration – Pending Admin Approval'

    body = f"""
Dear {user_name},\n

We hope this message finds you well. We would like to inform you that your application for registration with the Pakistan Association of Rwanda has been successfully submitted and is now pending approval from our administration team.\n

Here are a few details regarding your application:\n

- Name: {user_name}\n
- Email Address: {user_email}\n
- Application Date:  {datetime.now().strftime("%Y-%m-%d %H:%M:%S")}\n

If you have any questions or need to inquire about the status of your application, please feel free to contact our support team at info@pkar.rw.\n

Best regards,
Management,
Pakistan Association of Rwanda.
info@pkar.rw

    """
    msg = MIMEMultipart()
    msg['From'] = smtp_username
    msg['To'] = user_email  # Send the email to the user's email address
    msg['Subject'] = subject
    msg.attach(MIMEText(body, 'plain'))

    # Connect to the SMTP server with SSL/TLS
    try:
        server = smtplib.SMTP_SSL(smtp_server, smtp_port)
        server.login(smtp_username, smtp_password)

        # Send the email
        server.sendmail(smtp_username, user_email, msg.as_string())
        print('Approval Email sent successfully!')
    except Exception as e:
        print('Error: Could not send approval email -', str(e))
    finally:
        server.quit()


@receiver(post_save, sender=Registration)
def registration_status_changed(sender, instance, **kwargs):
    if instance.status == 'APPROVED' and instance.applied_for_edit is False:
        send_approval_email(instance.user.email,instance.name)
    elif instance.status == 'REJECTED':
        send_rejected_email(instance.user.email,instance.name,instance.reason)
    elif instance.status == 'PENDING':
        send_pending_email(instance.user.email,instance.name)




def send_edit_email(user_email,user_name):
    # Email configuration
    smtp_server = 'mail.pkar.rw'  # SMTP server
    smtp_port = 465  # SMTP port for SSL/TLS
    smtp_username = 'info@pkar.rw'  # Your email address
    smtp_password = '@PkAr2022RW%*'  # Your email password (replace with the actual password)

    # Create the email message
    subject = 'User data Update Application Submitted – Pending Admin Approval'

    body = f"""

Dear {user_name},\n

We hope you are doing well. We would like to inform you that your application for updating your data with the Pakistan Association of Rwanda has been successfully submitted and is now pending approval from our administration team.\n

Here are a few details regarding your update request:\n

- Name: {user_name}\n
- Email Address: {user_email}\n
- Update Application Date: {datetime.now().strftime("%Y-%m-%d %H:%M:%S")}\n

If you have any questions or need to inquire about the status of your application, please feel free to contact our support team at info@pkar.rw.\n

Best regards,
Management
Pakistan Association of Rwanda
info@pkar.rw

    """
    msg = MIMEMultipart()
    msg['From'] = smtp_username
    msg['To'] = user_email  # Send the email to the user's email address
    msg['Subject'] = subject
    msg.attach(MIMEText(body, 'plain'))

    # Connect to the SMTP server with SSL/TLS
    try:
        server = smtplib.SMTP_SSL(smtp_server, smtp_port)
        server.login(smtp_username, smtp_password)

        # Send the email
        server.sendmail(smtp_username, user_email, msg.as_string())
        print('Approval Email sent successfully!')
    except Exception as e:
        print('Error: Could not send approval email -', str(e))
    finally:
        server.quit()


def send_edit_approved_email(user_name,user_email):
    # Email configuration
    smtp_server = 'mail.pkar.rw'  # SMTP server
    smtp_port = 465  # SMTP port for SSL/TLS
    smtp_username = 'info@pkar.rw'  # Your email address
    smtp_password = '@PkAr2022RW%*'  # Your email password (replace with the actual password)

    # Create the email message
    subject = 'User data Update Application Approved'

    body = f"""

Dear {user_name}\n

We are pleased to inform you that your application for updating your data with the Pakistan Association of Rwanda has been approved by our administration team. Your information has been successfully updated.\n

If you have any additional changes or need further assistance, please do not hesitate to contact our support team at info@pkar.rw.\n

Warm regards,
Management,
Pakistan Association of Rwanda.
info@pkar.rw
    """
    msg = MIMEMultipart()
    msg['From'] = smtp_username
    msg['To'] = user_email  # Send the email to the user's email address
    msg['Subject'] = subject
    msg.attach(MIMEText(body, 'plain'))

    # Connect to the SMTP server with SSL/TLS
    try:
        server = smtplib.SMTP_SSL(smtp_server, smtp_port)
        server.login(smtp_username, smtp_password)

        # Send the email
        server.sendmail(smtp_username, user_email, msg.as_string())
        print('Approval Email sent successfully!')

    except Exception as e:
        print('Error: Could not send approval email -', str(e))
    finally:
        server.quit()


@receiver(post_save, sender=Registration)
def asend_edit_approved_email(sender, instance, **kwargs):
    if instance.applied_for_edit is False and instance.status == 'APPROVED':
        # Change the status to "APPROVED"
        # Send the approval email
        send_edit_approved_email(instance.name, instance.user.email)



def asend_edit_reject_email(user_name,user_email,reason):
    # Email configuration
    smtp_server = 'mail.pkar.rw'  # SMTP server
    smtp_port = 465  # SMTP port for SSL/TLS
    smtp_username = 'info@pkar.rw'  # Your email address
    smtp_password = '@PkAr2022RW%*'  # Your email password (replace with the actual password)

    # Create the email message
    subject = ' Data Update Application – Rejection and Reason'

    body = f"""
Dear {user_name},\n

We hope this message finds you well. We regret to inform you that your recent application for updating your data with the Pakistan Association of Rwanda has been reviewed, and, unfortunately, we are unable to approve your update request at this time.\n

The reason for the rejection of your update application is as follows:\n

{reason}\n

We encourage you to address the issue mentioned and, if applicable, submit a new update request once the matter has been resolved.\n

If you have any questions or require clarification about the rejection, please feel free to contact our support team at info@pkar.rw. \n

Sincerely,
Management,
Pakistan Association of Rwanda.
info@pkar.rw
    """
    msg = MIMEMultipart()
    msg['From'] = smtp_username
    msg['To'] = user_email  # Send the email to the user's email address
    msg['Subject'] = subject
    msg.attach(MIMEText(body, 'plain'))

    # Connect to the SMTP server with SSL/TLS
    try:
        server = smtplib.SMTP_SSL(smtp_server, smtp_port)
        server.login(smtp_username, smtp_password)

        # Send the email
        server.sendmail(smtp_username, user_email, msg.as_string())
        print('Approval Email sent successfully!')

    except Exception as e:
        print('Error: Could not send approval email -', str(e))
    finally:
        server.quit()


@receiver(post_save, sender=Registration)
def send_edit_reject_email(sender, instance, **kwargs):
    if instance.applied_for_edit is True and instance.status == 'REJECTED' and instance.reason is not None:
        # Change the status to "APPROVED"
        # Send the approval email
        asend_edit_reject_email(instance.name, instance.user.email,instance.reason)
