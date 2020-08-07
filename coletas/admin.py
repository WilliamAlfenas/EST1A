import csv
from django.db import models
from django.contrib import admin
from django.http import HttpResponse
from datetime import datetime
from .models import Paciente, Sintoma, \
    Cidade, Comorbidade, Alergia, Forma_Tratamento, \
    Fase, Origem, Dias_Sintoma, Medicoes_dia, DiagFinal
from django import forms

### cfehome.utils.py or the root of your project conf
def get_model_field_names(model, ignore_fields=['content_object']):
    '''
    ::param model is a Django model class
    ::param ignore_fields is a list of field names to ignore by default
    This method gets all model field names (as strings) and returns a list 
    of them ignoring the ones we know don't work (like the 'content_object' field)
    '''
    model_fields = model._meta.get_fields()
    model_field_names = list(set([f.name for f in model_fields if f.name not in ignore_fields]))
    return model_field_names


def get_lookup_fields(model, fields=None):
    '''
    ::param model is a Django model class
    ::param fields is a list of field name strings.
    This method compares the lookups we want vs the lookups
    that are available. It ignores the unavailable fields we passed.
    '''
    model_field_names = get_model_field_names(model)
    if fields is not None:
        '''
        we'll iterate through all the passed field_names
        and verify they are valid by only including the valid ones
        '''
        lookup_fields = []
        for x in fields:
            if "__" in x:
                # the __ is for ForeignKey lookups
                lookup_fields.append(x)
            elif x in model_field_names:
                lookup_fields.append(x)
    else:
        '''
        No field names were passed, use the default model fields
        '''
        lookup_fields = model_field_names
    return lookup_fields

def qs_to_dataset(qs, fields=None):
    '''
    ::param qs is any Django queryset
    ::param fields is a list of field name strings, ignoring non-model field names
    This method is the final step, simply calling the fields we formed on the queryset
    and turning it into a list of dictionaries with key/value pairs.
    '''
    
    lookup_fields = get_lookup_fields(qs.model, fields=fields)

    return [
        [
            dic[fd] if fd in dic else None
            for fd in lookup_fields
        ]
        for dic in qs.values()
    ]

def download_csv(modeladmin, request, queryset):
    # Create the HttpResponse object with the appropriate CSV header.
    response = HttpResponse(content_type='text/csv')
    ts = datetime.timestamp(datetime.now())
    model = queryset.model
    response['Content-Disposition'] = f'attachment; filename="{model.__name__}{ts}.csv"'

    writer = csv.writer(response)
    writer.writerow(get_lookup_fields(model))
    writer.writerows(qs_to_dataset(queryset))

    return response

download_csv.short_description = 'Baixar os items selecionados em CSV'

class CustomAdmin(admin.ModelAdmin):
    class Media:
        css = {
             'all': ('custom.css',)
        }
    actions = [download_csv]

class Dias_SintomaInLine(admin.TabularInline):
    model = Dias_Sintoma
    fieldsets = [
        (None, {
            'fields': [
                'sintoma', 
                'dia1', 'dia2', 'dia3', 
                'dia4', 'dia5', 'dia6', 
                'dia7', 'dia8', 'dia9'],
            #'readonly_fields': ('intervalo')
        })
    ]
    
    extra = 3

class Medicoes_diaInLine(admin.TabularInline):
    model = Medicoes_dia
    fieldsets = [
        (None, {
            'fields': [
                'medicao', 
                'dia1', 'dia2', 'dia3', 
                'dia4', 'dia5', 'dia6', 
                'dia7', 'dia8', 'dia9'],
            #'readonly_fields': ('intervalo')
        }),
    ]
    widgets = {
        'dia1': forms.NumberInput(attrs={'style': 'width: 100px'}),
    }
    
    extra = 1

class PacienteAdmin(CustomAdmin):
    inlines = [Dias_SintomaInLine, Medicoes_diaInLine]
    search_fields = ['nome', 'sexo', 'idade']


admin.site.register(Paciente, PacienteAdmin)
admin.site.register(Sintoma, CustomAdmin)
admin.site.register(Cidade, CustomAdmin)
admin.site.register(Comorbidade, CustomAdmin)
admin.site.register(Alergia, CustomAdmin)
admin.site.register(Forma_Tratamento, CustomAdmin)
admin.site.register(Fase, CustomAdmin)
admin.site.register(Origem, CustomAdmin)
admin.site.register(DiagFinal, CustomAdmin)
admin.site.site_header = 'Grupo Covid19 - Estágio 1A'
admin.site.site_title = 'Grupo Covid19 - Estágio 1A'