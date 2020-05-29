from django.core.exceptions import ObjectDoesNotExist
from django.http import JsonResponse

from apps.utils.models_direction import City, Colony


def get_direction(request):
    data = dict()
    try:
        city = City.objects.get(cp=request.GET.get('cp'))
        data['state'] = city.state.name
        data['city'] = city.name
        data['colony'] = list(Colony.objects.values('id', 'name').filter(city=city))
    except ObjectDoesNotExist:
        data['state'] = 'Sin estado'
        data['city'] = 'Sin municipio'
        data['colony'] = list()
    return JsonResponse(data)
