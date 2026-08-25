import json

from django.contrib import messages
from django.db import transaction
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse

from .forms import InformeForm, SECCIONES_FORMSETS
from .models import Informe


def _build_secciones(data, instance):
    return [
        {
            'prefix': prefix,
            'titulo': titulo,
            'boton': boton,
            'formset': FormSetClass(data, instance=instance, prefix=prefix),
        }
        for prefix, FormSetClass, titulo, boton in SECCIONES_FORMSETS
    ]


def _trigger_header(mensaje, tipo='success'):
    return json.dumps({'informeAccion': {'mensaje': mensaje, 'tipo': tipo}})


def informe_list(request):
    breadcrumbs = [
        {'name': 'Inicio', 'url': '/'},
        {'name': 'Informe de actividad', 'url': None},
    ]
    context = {
        'breadcrumbs': breadcrumbs,
        'informes': Informe.objects.select_related('escuela').prefetch_related('actividades__actividad'),
    }
    return render(request, 'actividadHome.html', context)


def informe_form(request, pk=None):
    informe = get_object_or_404(Informe, pk=pk) if pk else None
    breadcrumbs = [
        {'name': 'Inicio', 'url': '/'},
        {'name': 'Informe de actividad', 'url': reverse('actividad_home')},
        {'name': 'Editar informe' if informe else 'Nuevo informe', 'url': None},
    ]

    if request.method == 'POST':
        form = InformeForm(request.POST, instance=informe)
        secciones = _build_secciones(request.POST, informe)
        formsets_validos = all(s['formset'].is_valid() for s in secciones)

        if form.is_valid() and formsets_validos:
            with transaction.atomic():
                informe = form.save()
                for seccion in secciones:
                    formset = seccion['formset']
                    formset.instance = informe
                    formset.save()
            messages.success(
                request,
                'Informe actualizado correctamente.' if pk else 'Informe creado correctamente.',
            )
            return redirect('actividad_home')
    else:
        form = InformeForm(instance=informe)
        secciones = _build_secciones(None, informe)

    context = {
        'form': form,
        'informe': informe,
        'secciones': secciones,
        'breadcrumbs': breadcrumbs,
    }
    return render(request, 'informeForm.html', context)


def informe_detalle(request, pk):
    informe = get_object_or_404(
        Informe.objects.select_related('escuela', 'escuela__distrito'),
        pk=pk,
    )
    context = {
        'informe': informe,
        'actividades': informe.actividades.select_related('actividad'),
        'participantes': informe.participantes.select_related('tipoParticipante'),
        'objetivos': informe.objetivos.select_related('objetivo'),
        'agendas': informe.agendas.select_related('agenda'),
        'hallazgos': informe.hallazgos.select_related('hallazgo'),
        'fortalezas': informe.fortalezas.select_related('fortaleza'),
        'limitaciones': informe.limitaciones.select_related('limitacion'),
        'recomendaciones': informe.recomendaciones.select_related('recomendacion'),
        'otros': informe.otros.all(),
        'acuerdos': informe.acuerdos.all(),
    }
    return render(request, 'partials/actividad/_detalle.html', context)


def informe_delete(request, pk):
    informe = get_object_or_404(Informe, pk=pk)
    if request.method == 'POST':
        informe.delete()
        response = render(request, 'partials/actividad/_lista.html', {
            'informes': Informe.objects.select_related('escuela').prefetch_related('actividades__actividad'),
        })
        response['HX-Trigger'] = _trigger_header('Informe eliminado correctamente.')
        return response
    return redirect('actividad_home')
