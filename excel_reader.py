# excel_reader.py
import logging
import openpyxl

# Set up logging
logger = logging.getLogger(__name__)

def read_data_from_excel(file_path, sheet_name):
    logger.info(f"Reading data from Excel file: '{file_path}', sheet: '{sheet_name}'")
    data = []
    try:
        workbook = openpyxl.load_workbook(file_path)
        sheet = workbook[sheet_name]
        for row in sheet.iter_rows(values_only=True):
            first_name, last_name, email, company_name = row
            data.append((first_name, last_name, email, company_name))
        logger.info(f"Read {len(data)} rows of data from Excel file.")
    except Exception as e:
        logger.error("Error reading Excel file:", exc_info=True)
    return data
