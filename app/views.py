from django.shortcuts import render

from app.utils import convert_length, convert_weight, convert_temperature
from app.validators import validate_input


def index(request):
    result = None
    if request.method == 'POST':
        value = request.POST.get('value')
        unit_from = request.POST.get('unit_from')
        unit_to = request.POST.get('unit_to')

        # Validate input
        error_message, valid_value = validate_input(value, unit_from, unit_to)
        if error_message:
            result = error_message
        else:
            result = convert_length(valid_value, unit_from, unit_to)

    return render(request, 'index.html', {'result': result})


def weight(request):
    result = None
    if request.method == 'POST':
        value = request.POST.get('value')
        unit_from = request.POST.get('unit_from')
        unit_to = request.POST.get('unit_to')

        # Validate input
        error_message, valid_value = validate_input(value, unit_from, unit_to)
        if error_message:
            result = error_message
        else:
            result = convert_weight(valid_value, unit_from, unit_to)

    return render(request, 'weight.html', {'result': result})


def temperature(request):
    result = None
    if request.method == 'POST':
        value = request.POST.get('value')
        unit_from = request.POST.get('unit_from')
        unit_to = request.POST.get('unit_to')

        # Validate input
        error_message, valid_value = validate_input(value, unit_from, unit_to)
        if error_message:
            result = error_message
        else:
            result = convert_temperature(valid_value, unit_from, unit_to)

    return render(request, 'temperature.html', {'result': result})
