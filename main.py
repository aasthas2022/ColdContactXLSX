# main.py
"""
Entry point of ColdContactXLSX.
"""

import logging

from scheduler.schedule_now import send_emails_now
from scheduler.send_emails_at_specific_time import schedule_emails

# Set up logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def main():
    choice = input("Do you want to send the email now or schedule it for a specific time? (now/schedule): ").lower()

    if choice == 'now':
        send_emails_now()
    elif choice == 'schedule':
        schedule_emails()
    else:
        print("Invalid choice. Please enter 'now' or 'schedule'.")

if __name__ == "__main__":
    main()
