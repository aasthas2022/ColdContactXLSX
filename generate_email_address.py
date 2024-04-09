# generate_email_address.py
import logging

# Set up logging
logger = logging.getLogger(__name__)

def generate_email_address(first_name, last_name, email, company_name):
    logger.info("Generating email addresses...")
    if email:
        logger.info("Using provided email address.")
        return email
    elif first_name and last_name:
        email1 = f"{first_name.lower()[0]}.{last_name.lower()}@{company_name.lower()}.com"
        email2 = f"{first_name.lower()}.{last_name.lower()[0]}@{company_name.lower()}.com"
        email3 = f"{first_name.lower()}_{last_name.lower()}@{company_name.lower()}.com"
        email4 = f"{first_name.lower()}{last_name.lower()}@{company_name.lower()}.com"
        logger.info(f"Generated email addresses: '{email1}', '{email2}', '{email3}', '{email4}'.")
        return email1, email2, email3, email4
    elif first_name:
        email = f"{first_name.lower()}@{company_name.lower()}.com"
        logger.info(f"Generated email address: '{email}'.")
        return email
    else:
        logger.warning("Unable to generate email address, insufficient data.")
        return None
