from django.utils.timezone import localtime

from datacenter.models import Passcard
from datacenter.models import Visit
from django.shortcuts import render


def storage_information_view(request):
    visiters = Visit.objects.filter(leaved_at=None)  # кто сейчас находится в хранилище

    non_closed_visits = []
    for visiter in visiters:
        visiter.duration = visiter.get_duration()  # присвоили каждому visiters время нахождения в хранилище
        non_closed_visits.append({
            'who_entered': f'{visiter.passcard.owner_name}',
            'entered_at': f'{localtime(visiter.entered_at)}',
            'duration': f'{format_duration(visiter.duration)}',
            'is_strange': f'{visiter.is_long()}',
        })

    context = {
        'non_closed_visits': non_closed_visits,  # не закрытые посещения
    }
    return render(request, 'storage_information.html', context)


def format_duration(duration):
    '''Returning duration in string format'''
    total_sec = duration.total_seconds()
    days = total_sec // 86400
    hours = int((total_sec - days * 86400) // 3600)
    minutes = int((total_sec - days * 86400 - hours * 3600) // 60)
    seconds = int(total_sec - days * 86400 - hours * 3600 - minutes * 60)
    return f'{hours}:{minutes}:{seconds}'
