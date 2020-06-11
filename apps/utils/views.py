import pyexcel
from django.http import HttpResponse
from apps.utils.models_direction import State, City, Colony
from engine import settings


def process_state(request):
    """
    Function to upload catalog Periodo to the database
    :param request:
    :return: umber of records crated in Period table
    """
    try:
        records = pyexcel.iget_records(file_name='static/files/state.xlsx')
    except Exception as err:
        return err
    count_created = 0
    for item in records:
        try:
            obj, created = State.objects.get_or_create(
                name=item['state'].upper(),
            )
        except Exception as err:
            return err

        if created:
            count_created += 1
    return HttpResponse('Se crearon: %s' % count_created )


def process_city(request):
    """
    Function to upload catalog Periodo to the database
    :param request:
    :return: umber of records crated in Period table
    """
    try:
        records = pyexcel.iget_records(file_name='static/files/city.xlsx')
    except Exception as err:
        return err
    count_created = 0
    for item in records:
        try:

            state = State.objects.get(id=item['state'])

            obj, created = City.objects.get_or_create(
                name=item['city'].upper(),
                cp=item['cp'],
                state=state,
            )
        except Exception as err:
            return err

        if created:
            count_created += 1
    return HttpResponse('Se crearon: %s' % count_created )


def process_colony(request):
    """
    Function to upload catalog Periodo to the database
    :param request:
    :return: umber of records crated in Period table
    """
    count_created = 0
    try:
        records = pyexcel.iget_records(file_name='static/files/colony.xlsx')
    except Exception as err:
        return err

    for item in records:
        try:
            city = City.objects.get(id=item['city'])

            obj, created = Colony.objects.get_or_create(
                name=item['colony'].upper(),
                city=city,
            )
        except Exception as err:
            return err

        if created:
            count_created += 1
    return HttpResponse('Se crearon: %s' % count_created)

