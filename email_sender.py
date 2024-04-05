# email_sender.py
import logging
from email.mime.application import MIMEApplication
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

# Set up logging
logger = logging.getLogger(__name__)

def send_email(sender_email, sender_password, recipient_email, subject, message):
    logger.info(f"Sending email to: {recipient_email}")
    try:
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(sender_email, sender_password)
        
        msg = MIMEMultipart()
        msg['From'] = sender_email
        msg['To'] = recipient_email
        msg['Subject'] = subject
        msg.attach(MIMEText(message, 'plain'))
        # msg.attach(MIMEText(message, 'html')) - uncommet if you want your message to be formatted
        
        # Attach resume file from the root folder
        resume_filename = "email_assets/AasthaShukla_SDE_Resume.pdf" # Update as necessary
        with open(resume_filename, 'rb') as file:
            resume_attachment = MIMEApplication(file.read(), Name=resume_filename)
        resume_attachment['Content-Disposition'] = f'attachment; filename="{resume_filename}"'
        msg.attach(resume_attachment)
        
        server.sendmail(sender_email, recipient_email, msg.as_string())
        logger.info(f"Email sent successfully to {recipient_email}")

        server.quit()
    except Exception as e:
        logger.error("Error sending email:", exc_info=True)
