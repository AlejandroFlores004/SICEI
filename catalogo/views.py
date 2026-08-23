import json

from django.forms import modelform_factory, TextInput
from django.http import HttpResponseNotFound
from django.shortcuts import render

from .models import (
    CatalogoParticipante,
    CatalogoObjetivos,
    CatalogoAgenda,
    CatalogoHallazgo,
    CatalogoFortaleza,
    CatalogoLimitacion,
    CatalogoRecomendacion,
    CatalogoActividad,
)

CATALOGOS = {
    'participantes': {'model': CatalogoParticipante, 'nombre': 'Participantes', 'singular': 'Participante'},
    'objetivos': {'model': CatalogoObjetivos, 'nombre': 'Objetivos', 'singular': 'Objetivo'},
    'agenda': {'model': CatalogoAgenda, 'nombre': 'Agenda', 'singular': 'Punto de agenda'},
    'hallazgos': {'model': CatalogoHallazgo, 'nombre': 'Hallazgos', 'singular': 'Hallazgo'},
    'fortalezas': {'model': CatalogoFortaleza, 'nombre': 'Fortalezas', 'singular': 'Fortaleza'},
    'limitaciones': {'model': CatalogoLimitacion, 'nombre': 'Limitaciones', 'singular': 'Limitación'},
    'recomendaciones': {'model': CatalogoRecomendacion, 'nombre': 'Recomendaciones', 'singular': 'Recomendación'},
    'actividades': {'model': CatalogoActividad, 'nombre': 'Actividades', 'singular': 'Actividad'},
}

NOMBRE_WIDGET = TextInput(attrs={
    'class': 'input input-bordered w-full',
    'placeholder': 'Escribe un nombre...',
    'autofocus': True,
})


def _form_class(model):
    return modelform_factory(model, fields=['nombre'], widgets={'nombre': NOMBRE_WIDGET})


def _panel_context(slug):
    info = CATALOGOS[slug]
    return {
        'slug': slug,
        'info': info,
        'items': info['model'].objects.all(),
    }


def _trigger_header(mensaje, tipo='success', cerrar_modal=False):
    return json.dumps({
        'catalogoAccion': {
            'mensaje': mensaje,
            'tipo': tipo,
            'cerrarModal': cerrar_modal,
        }
    })


def catalogo_home(request):
    slug_activo = 'participantes'
    breadcrumbs = [
        {'name': 'Inicio', 'url': '/'},
        {'name': 'Catálogos', 'url': None},
    ]
    context = {
        'breadcrumbs': breadcrumbs,
        'catalogos': CATALOGOS,
        'slug_activo': slug_activo,
        **_panel_context(slug_activo),
    }
    return render(request, 'catalogoHome.html', context)


def catalogo_panel(request, catalogo):
    if catalogo not in CATALOGOS:
        return HttpResponseNotFound()
    return render(request, 'partials/catalogo/_panel.html', _panel_context(catalogo))


def catalogo_create(request, catalogo):
    if catalogo not in CATALOGOS:
        return HttpResponseNotFound()
    info = CATALOGOS[catalogo]
    Form = _form_class(info['model'])

    if request.method == 'POST':
        form = Form(request.POST)
        if form.is_valid():
            form.save()
            response = render(request, 'partials/catalogo/_panel.html', _panel_context(catalogo))
            response['HX-Retarget'] = '#catalogo-panel'
            response['HX-Reswap'] = 'outerHTML'
            response['HX-Trigger'] = _trigger_header(
                f"{info['singular']} agregado correctamente.", cerrar_modal=True
            )
            return response
        return render(request, 'partials/catalogo/_form.html', {
            'form': form, 'slug': catalogo, 'info': info,
        })

    form = Form()
    return render(request, 'partials/catalogo/_form.html', {
        'form': form, 'slug': catalogo, 'info': info,
    })
