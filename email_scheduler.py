# email_scheduler.py

import logging
import os
from dotenv import load_dotenv
from email_sender import send_email
from excel_reader import read_data_from_excel
from generate_email_address import generate_email_address
import time
import datetime

# Set up logging
logger = logging.getLogger(__name__)

def load_email_settings():
    load_dotenv()
    logger.info("Loaded environment variables from .env file.")
    return os.getenv('EMAIL_USERNAME'), os.getenv('EMAIL_PASSWORD')

def read_email_template():
    with open('email_assets/email_template.txt', 'r') as file:
        email_template = file.read()
    logger.info("Read email template.")
    return email_template

def read_excel_data():
    excel_file = 'recruiters.xlsx'
    sheet_name = 'Sheet1'
    logger.info(f"Reading data from Excel file: '{excel_file}', sheet: '{sheet_name}'")
    return read_data_from_excel(excel_file, sheet_name)

def send_emails_now(batch_size=10):
    sender_email, sender_password = load_email_settings()
    email_template = read_email_template()
    data = read_excel_data()

    # Split the data into batches
    for i in range(0, len(data), batch_size):
        batch = data[i:i + batch_size]

        for row in batch:
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

def schedule_emails():
    specific_time = input("Enter the specific time to schedule the email (HH:MM): ")
    try:
        hour, minute = map(int, specific_time.split(':'))
        if 0 <= hour < 24 and 0 <= minute < 60:
            send_emails_at_specific_time(hour, minute)
        else:
            print("Invalid time. Please enter a valid time in HH:MM format.")
    except ValueError:
        print("Invalid time format. Please enter the time in HH:MM format.")

def send_emails_at_specific_time(hour, minute, batch_size=10):
    sender_email, sender_password = load_email_settings()
    email_template = read_email_template()
    data = read_excel_data()

    now = datetime.datetime.now()
    scheduled_time = now.replace(hour=hour, minute=minute, second=0, microsecond=0)
    if scheduled_time < now:
        scheduled_time += datetime.timedelta(days=1)

    delay = (scheduled_time - now).total_seconds()
    logger.info(f"Waiting until {scheduled_time.strftime('%H:%M')} to send emails.")
    time.sleep(delay)

    # Split the data into batches
    for i in range(0, len(data), batch_size):
        batch = data[i:i + batch_size]

        for row in batch:
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
