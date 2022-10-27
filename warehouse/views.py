from django.shortcuts import render
from warehouse.models import Component


def index(request):
    components = Component.objects.all()

    context = {
        'components': components,
    }
    return render(request, 'warehouse/index.html', context)
