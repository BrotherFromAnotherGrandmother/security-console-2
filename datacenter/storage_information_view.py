from django.utils.timezone import localtime
from datacenter.models import Visit
from django.shortcuts import render
from .assistant_functions import format_duration

def storage_information_view(request):
    unleaved_visits = Visit.objects.filter(leaved_at=None)

    non_closed_visits = []
    for visit in unleaved_visits:
        visit.duration = visit.get_duration()
        non_closed_visits.append({
            'who_entered': visit.passcard.owner_name,
            'entered_at': localtime(visit.entered_at),
            'duration': format_duration(visit.duration),
            'is_strange': visit.is_long(),
        })

    context = {
        'non_closed_visits': non_closed_visits,
    }
    return render(request, 'storage_information.html', context)
