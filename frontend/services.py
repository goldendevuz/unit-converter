from icecream import ic


def convert(value, unit_from, unit_to):
    ic(value, unit_from, unit_to)
    # Example conversion logic for length
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

    if unit_from not in conversions or unit_to not in conversions:
        return 'Invalid units'

    meters = value * conversions[unit_from]
    ic(value)
    ic(meters / conversions[unit_to])
    return f"{value} {unit_from} = {meters / conversions[unit_to]} {unit_to}" # :.2f


def convert_weight(value, unit_from, unit_to):
    # Example conversion logic for weight
    conversions = {
        'milligram': 0.001,
        'gram': 1,
        'kilogram': 1000,
        'ounce': 28.3495,
        'pound': 453.592
    }

    if unit_from not in conversions or unit_to not in conversions:
        return 'Invalid units'

    grams = value * conversions[unit_from]
    return f"{value} {unit_from} = {grams / conversions[unit_to]:.2f} {unit_to}"


def convert_temperature(value, unit_from, unit_to):
    if unit_from == unit_to:
        return f"{value} {unit_from} = {value} {unit_to}"

    result = 0
    if unit_from == 'celsius':
        if unit_to == 'fahrenheit':
            result = (value * 9 / 5) + 32
        elif unit_to == 'kelvin':
            result = value + 273.15
    elif unit_from == 'fahrenheit':
        if unit_to == 'celsius':
            result = (value - 32) * 5 / 9
        elif unit_to == 'kelvin':
            result = (value - 32) * 5 / 9 + 273.15
    elif unit_from == 'kelvin':
        if unit_to == 'celsius':
            result = value - 273.15
        elif unit_to == 'fahrenheit':
            result = (value - 273.15) * 9 / 5 + 32
    else:
        return 'Invalid units'

    return f"{value} {unit_from} = {result:.2f} {unit_to}"
