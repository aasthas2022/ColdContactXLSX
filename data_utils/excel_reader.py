# data_utils/excel_reader.py
"""
Module to read data from an Excel file.
"""

import logging
import openpyxl

# Set up logging
logger = logging.getLogger(__name__)

def read_data_from_excel(file_path, sheet_name):
    """
    Reads data from an Excel file.

    Args:
        file_path (str): Path to the Excel file.
        sheet_name (str): Name of the sheet to read data from.

    Returns:
        list: List of tuples containing data read from the Excel file.
    """
    logger.info(f"Reading data from Excel file: '{file_path}', sheet: '{sheet_name}'")
    data = []
    try:
        workbook = openpyxl.load_workbook(file_path)
        sheet = workbook[sheet_name]
        for row in sheet.iter_rows(values_only=True):
            first_name, last_name, email, company_name, *designation = row
            data.append((first_name, last_name, email, company_name, designation[0] if designation else None))
    except Exception as e:
        logger.error("Error reading Excel file:", exc_info=True)
    logger.info(f"Read {len(data)} rows of data from Excel file.")
    return data
