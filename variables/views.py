from .logic import variables_logic as vl
from django.http import HttpResponse
from django.core import serializers
import json
from django.views.decorators.csrf import csrf_exempt


def variables_view(request):
    if request.method == 'GET':
        id= request.GET.get("id", None)
        if id:
            variables_dto = vl.get_variable(id)
            variable = serializers.serialize('json', [variable_dto, ])
            return HttpResponse(variable, 'application/json')
        else:
            variables_dto = vl.get_variables()
            variables = serializers.serialize('json', [variable_dto, ])
            return HttpResponse(variable, 'application/json')

    def variable_view(Request, pk):
        if request.method == 'GET':
            variables_dto = vl.get_variable(pk)
            variable = serializers.serialize('json', [variable_dto,])
            return HttpResponse(variable, 'application/json')

        if request.method == PUT:
            variables_dto = vl.update_variable(pk)
            variable = serializers.serialize('json', [variable_dto,])
            return HttpResponse(variable, 'application/json')
