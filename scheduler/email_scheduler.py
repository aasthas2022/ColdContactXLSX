# scheduler/email_scheduler.py

import logging
import os
from dotenv import load_dotenv
from email_utils.email_sender import send_email
from data_utils.excel_reader import read_data_from_excel
from data_utils.generate_email_address import generate_email_address

logger = logging.getLogger(__name__)

def load_email_settings():
    """
    Loads email settings from environment variables.

    Returns:
        tuple: Tuple containing email username and password.
    """
    load_dotenv()
    logger.info("Loaded environment variables from .env file.")
    return os.getenv('EMAIL_USERNAME'), os.getenv('EMAIL_PASSWORD')

def read_email_template():
    """
    Reads the email template from a file.

    Returns:
        str: Email template.
    """
    with open('email_assets/email_template.txt', 'r') as file:
        email_template = file.read()
    logger.info("Read email template.")
    return email_template

def read_excel_data():
    """
    Reads data from an Excel file.

    Returns:
        list: List of tuples containing data read from the Excel file.
    """
    excel_file = 'recruiters.xlsx'
    sheet_name = 'Sheet1'
    logger.info(f"Reading data from Excel file: '{excel_file}', sheet: '{sheet_name}'")
    return read_data_from_excel(excel_file, sheet_name)
