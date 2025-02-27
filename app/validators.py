def validate_input(value, unit_from, unit_to):
    """
    Validate the input for conversion functions.

    :param value: The value to be converted.
    :param unit_from: The unit to convert from.
    :param unit_to: The unit to convert to.
    :return: A tuple (error_message, valid_value). If valid, error_message is None, and valid_value is a float.
    """
    if not value:
        return 'Please enter a value to convert.', None
    try:
        value = float(value)
        if value <= 0:
            return 'Please enter a positive number greater than zero.', None
    except ValueError:
        return 'Invalid input. Please enter a numeric value.', None

    if not unit_from or not unit_to:
        return 'Please select both units for conversion.', None

    return None, value
