# scheduler/schedule_now.py

import logging
import time
from data_utils.generate_email_address import generate_email_address
from email_utils.email_sender import send_email
from scheduler.email_scheduler import load_email_settings, read_email_template, read_excel_data

logger = logging.getLogger(__name__)
MAX_RETRIES = 3


def send_emails_now(batch_size=10):
    """
    Sends emails immediately.

    Args:
        batch_size (int): Number of emails to send in each batch.
    """
    sender_email, sender_password = load_email_settings()
    email_template = read_email_template()
    data = read_excel_data()

    # Split the data into batches
    for i in range(0, len(data), batch_size):
        batch = data[i:i + batch_size]

        for row in batch:
            retries = 0
            while retries < MAX_RETRIES:
                try:
                    first_name, last_name, email, company_name, designation = row
                    recipient_emails = generate_email_address(first_name, last_name, email, company_name)
                    if isinstance(recipient_emails, tuple):
                        for recipient_email in recipient_emails:
                            subject = f"[Aastha Shukla]: Exploring Full-Time SDE Roles at {company_name}"
                            message = email_template.format(first_name=first_name, last_name=last_name, email=recipient_email,
                                                             company_name=company_name, designation=designation if designation else "esteemed employee")
                            send_email(sender_email, sender_password, recipient_email, subject, message, company_name)
                            logger.info(f"Email sent successfully to {recipient_email}")
                    elif recipient_emails:
                        subject = f"[Aastha Shukla]: Exploring Full-Time SDE Roles at {company_name}"
                        message = email_template.format(first_name=first_name, last_name=last_name, email=recipient_emails,
                                                         company_name=company_name, designation=designation if designation else "esteemed employee")
                        send_email(sender_email, sender_password, recipient_emails, subject, message, company_name)
                        logger.info(f"Email sent successfully to {recipient_emails}")
                    
                    # If email sent successfully, break out of the retry loop
                    break
                except Exception as e:
                    logger.error(f"Error sending email: {e}")
                    retries += 1
                    logger.info(f"Retrying... Retry attempt {retries}/{MAX_RETRIES}")
                    time.sleep(10)  # Wait for a few seconds before retrying

            # If maximum retries reached without success, log error
            if retries == MAX_RETRIES:
                logger.error("Max retries reached. Unable to send email.")
