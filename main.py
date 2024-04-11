# main.py
import logging
from dotenv import load_dotenv
import os
from excel_reader import read_data_from_excel
from email_sender import send_email
from generate_email_address import generate_email_address

# Set up logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def main():
    # Load environment variables from .env file
    load_dotenv()
    logger.info("Loaded environment variables from .env file.")

    # Path to the Excel file
    excel_file = 'recruiters.xlsx'
    # Name of the sheet containing data
    sheet_name = 'Sheet1'
    logger.info(f"Reading data from Excel file: '{excel_file}', sheet: '{sheet_name}'")
    
    # Read sender's email credentials from environment variables
    sender_email = os.getenv('EMAIL_USERNAME')
    sender_password = os.getenv('EMAIL_PASSWORD')
    
    # Read email template
    with open('email_assets/email_template.txt', 'r') as file:
        email_template = file.read()
    logger.info("Read email template.")
    
    
    # Read email template with formatting
    # with open('email_assets/email_template_with_formatting.txt', 'r') as file:
    #     email_template = file.read()
    # logger.info("Read email template.")
    
    # Read data from Excel file
    data = read_data_from_excel(excel_file, sheet_name)
    logger.info(f"Read {len(data)} rows of data from Excel file.")

    # Send emails
    for row in data:
        first_name, last_name, email, company_name, designation = row
        recipient_emails = generate_email_address(first_name, last_name, email, company_name)
        if isinstance(recipient_emails, tuple):
            for recipient_email in recipient_emails:
                subject = f"[Aastha Shukla]: Exploring Full-Time SDE Roles at {company_name}" # customize as per your name
                message = email_template.format(first_name=first_name, last_name=last_name, email=recipient_email, company_name=company_name, designation=designation if designation else "esteemed employee")
                send_email(sender_email, sender_password, recipient_email, subject, message, company_name)
                logger.info(f"Email sent successfully to {recipient_email}")
        elif recipient_emails:
            subject = f"[Aastha Shukla]: Exploring Full-Time SDE Roles at {company_name}" # customize as per your name
            message = email_template.format(first_name=first_name, last_name=last_name, email=recipient_emails, company_name=company_name, designation=designation if designation else "esteemed employee")
            send_email(sender_email, sender_password, recipient_emails, subject, message, company_name)
            logger.info(f"Email sent successfully to {recipient_emails}")

if __name__ == "__main__":
    main()
