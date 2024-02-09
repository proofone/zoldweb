from django.core.serializers import serialize
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, render, HttpResponse
from .models import User, Community, CommunityMembership, Location, OtherEntity


def get_serialized_objects(request, model):
    kwargs = {
        'order': '-pk',
        'offset': 0,
        'size': 10,
        'filter': {}
    }
    for k, v in request.GET.items():
        if k in kwargs:
            kwargs[k] = v
        
        # if kwarg contains name of a model field, add it as filter arg:
        elif k in [f.name for f in model._meta.concrete_fields]:
            kwargs['filter'].update({k: v})
            
    qs = model.objects.filter(**kwargs['filter']).order_by(kwargs['order'])
    retval = qs[kwargs['offset']:kwargs['offset']+kwargs['size']]
    
    return serialize('json', retval) 


@login_required
def communities(request):
    return HttpResponse(content=get_serialized_objects(request, Community))


@login_required
def users(request):
    return HttpResponse(content=get_serialized_objects(request, User))
