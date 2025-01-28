def convert_units(value, unit_from, unit_to, conversions):
    """
    Generic function to convert between units.

    :param value: Numeric value to convert.
    :param unit_from: Unit to convert from.
    :param unit_to: Unit to convert to.
    :param conversions: Dictionary containing unit conversion factors.
    :return: Converted value as a formatted string.
    """
    
    if unit_from not in conversions or unit_to not in conversions:
        return 'Invalid units'

    base_unit_value = float(value) * conversions[unit_from]  # Convert to base unit
    converted_value = base_unit_value / conversions[unit_to]  # Convert to target unit
    
    return f"{value} {unit_from} = {converted_value} {unit_to}"

def convert_length(value, unit_from, unit_to):
    """Convert length units."""
    conversions = {
        'millimeter': 0.001,
        'centimeter': 0.01,
        'meter': 1,
        'kilometer': 1000,
        'inch': 0.0254,
        'foot': 0.3048,
        'yard': 0.9144,
        'mile': 1609.34
    }
    return convert_units(value, unit_from, unit_to, conversions)

def convert_weight(value, unit_from, unit_to):
    """Convert weight units."""
    conversions = {
        'milligram': 0.001,
        'gram': 1,
        'kilogram': 1000,
        'ounce': 28.3495,
        'pound': 453.592
    }
    return convert_units(value, unit_from, unit_to, conversions)

def convert_temperature(value, unit_from, unit_to):
    """
    Convert temperature units (Celsius, Fahrenheit, Kelvin).

    :param value: Numeric value to convert.
    :param unit_from: Unit to convert from (celsius, fahrenheit, kelvin).
    :param unit_to: Unit to convert to (celsius, fahrenheit, kelvin).
    :return: Converted temperature as a formatted string.
    """
    if unit_from == unit_to:
        return f"{value} {unit_from} = {value} {unit_to}"

    temperature_conversions = {
        ('celsius', 'fahrenheit'): lambda v: (v * 9 / 5) + 32,
        ('celsius', 'kelvin'): lambda v: v + 273.15,
        ('fahrenheit', 'celsius'): lambda v: (v - 32) * 5 / 9,
        ('fahrenheit', 'kelvin'): lambda v: (v - 32) * 5 / 9 + 273.15,
        ('kelvin', 'celsius'): lambda v: v - 273.15,
        ('kelvin', 'fahrenheit'): lambda v: (v - 273.15) * 9 / 5 + 32
    }

    try:
        result = temperature_conversions.get((unit_from, unit_to), lambda v: 'Invalid units')(value)
        return f"{value} {unit_from} = {result} {unit_to}"
    except Exception:
        return "Invalid input value"