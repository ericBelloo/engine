from django.core.exceptions import ObjectDoesNotExist
from django.http import JsonResponse

from apps.utils.models import CP


def get_state_city(request):
    data = dict()
    try:
        cp = CP.objects.get(cp=request.GET.get('cp'))
        data['state'] = cp.city.state.name
        data['city'] = cp.city.name
    except ObjectDoesNotExist:
        data['state'] = 'Sin estado'
        data['city'] = 'Sin municipio'
    return JsonResponse(data)
