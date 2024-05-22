from datetime import datetime


def validate_date_format(cls, date):
    """
    Validate if the given date string is in the format 'YYYY-MM-DD'.

    Parameters:
    - date (str): The date string to validate.

    Returns:
    - str: The input date string if it matches the format.

    Raises:
    - ValueError: If the date string does not match the format 'YYYY-MM-DD'.
    """
    try:
        datetime.strptime(date, '%Y-%m-%d')  # Check if the date string matches the format
        return date
    except:
        raise ValueError('Date not in the appropriate format, to the date field you must send a string in the format: '
                         '"YYYY-MM-DD"')
