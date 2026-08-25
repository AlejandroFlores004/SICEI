from django import forms
from django.forms import inlineformset_factory
from django_select2.forms import Select2Widget

from organizacion.models import Escuela
from .models import (
    Informe, Acuerdo, Participante, Objetivo, Actividad, Agenda,
    Hallazgo, Fortaleza, Limitacion, Recomendacion, Otros,
)

INPUT = 'input input-bordered w-full'
SELECT = 'select select-bordered w-full'
TEXTAREA = 'textarea textarea-bordered w-full'


class InformeForm(forms.ModelForm):
    class Meta:
        model = Informe
        fields = ['fecha', 'escuela']
        widgets = {
            'fecha': forms.DateInput(attrs={'class': INPUT, 'type': 'date'}),
            'escuela': Select2Widget(attrs={'class': SELECT}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['escuela'].queryset = Escuela.objects.filter(estado=True)


class ActividadForm(forms.ModelForm):
    class Meta:
        model = Actividad
        fields = ['actividad', 'descripcion']
        labels = {'actividad': 'Actividad', 'descripcion': 'Descripción'}
        widgets = {
            'actividad': Select2Widget(attrs={'class': SELECT}),
            'descripcion': forms.Textarea(attrs={'class': TEXTAREA, 'rows': 2}),
        }


class ParticipanteForm(forms.ModelForm):
    class Meta:
        model = Participante
        fields = ['tipoParticipante', 'cantidadHombre', 'cantidadMujer']
        labels = {
            'tipoParticipante': 'Tipo de participante',
            'cantidadHombre': 'Hombres',
            'cantidadMujer': 'Mujeres',
        }
        widgets = {
            'tipoParticipante': Select2Widget(attrs={'class': SELECT}),
            'cantidadHombre': forms.NumberInput(attrs={'class': INPUT, 'min': 0, 'value': 0}),
            'cantidadMujer': forms.NumberInput(attrs={'class': INPUT, 'min': 0, 'value': 0}),
        }


class ObjetivoForm(forms.ModelForm):
    class Meta:
        model = Objetivo
        fields = ['objetivo']
        labels = {'objetivo': 'Objetivo'}
        widgets = {
            'objetivo': Select2Widget(attrs={'class': SELECT}),
        }


class AgendaForm(forms.ModelForm):
    class Meta:
        model = Agenda
        fields = ['agenda', 'descripcion']
        labels = {'agenda': 'Punto de agenda', 'descripcion': 'Descripción'}
        widgets = {
            'agenda': Select2Widget(attrs={'class': SELECT}),
            'descripcion': forms.Textarea(attrs={'class': TEXTAREA, 'rows': 2}),
        }


class HallazgoForm(forms.ModelForm):
    class Meta:
        model = Hallazgo
        fields = ['hallazgo', 'descripcion']
        labels = {'hallazgo': 'Hallazgo', 'descripcion': 'Descripción'}
        widgets = {
            'hallazgo': Select2Widget(attrs={'class': SELECT}),
            'descripcion': forms.Textarea(attrs={'class': TEXTAREA, 'rows': 2}),
        }


class FortalezaForm(forms.ModelForm):
    class Meta:
        model = Fortaleza
        fields = ['fortaleza', 'descripcion']
        labels = {'fortaleza': 'Fortaleza', 'descripcion': 'Descripción'}
        widgets = {
            'fortaleza': Select2Widget(attrs={'class': SELECT}),
            'descripcion': forms.Textarea(attrs={'class': TEXTAREA, 'rows': 2}),
        }


class LimitacionForm(forms.ModelForm):
    class Meta:
        model = Limitacion
        fields = ['limitacion', 'descripcion']
        labels = {'limitacion': 'Limitación', 'descripcion': 'Descripción'}
        widgets = {
            'limitacion': Select2Widget(attrs={'class': SELECT}),
            'descripcion': forms.Textarea(attrs={'class': TEXTAREA, 'rows': 2}),
        }


class RecomendacionForm(forms.ModelForm):
    class Meta:
        model = Recomendacion
        fields = ['recomendacion', 'descripcion']
        labels = {'recomendacion': 'Recomendación', 'descripcion': 'Descripción'}
        widgets = {
            'recomendacion': Select2Widget(attrs={'class': SELECT}),
            'descripcion': forms.Textarea(attrs={'class': TEXTAREA, 'rows': 2}),
        }


class OtrosForm(forms.ModelForm):
    class Meta:
        model = Otros
        fields = ['descripcion']
        labels = {'descripcion': 'Descripción'}
        widgets = {
            'descripcion': forms.Textarea(attrs={'class': TEXTAREA, 'rows': 2}),
        }


class AcuerdoForm(forms.ModelForm):
    class Meta:
        model = Acuerdo
        fields = ['nombre', 'responsable', 'fecha']
        labels = {'nombre': 'Acuerdo', 'responsable': 'Responsable', 'fecha': 'Fecha'}
        widgets = {
            'nombre': forms.TextInput(attrs={'class': INPUT, 'placeholder': 'Acuerdo'}),
            'responsable': forms.TextInput(attrs={'class': INPUT, 'placeholder': 'Responsable'}),
            'fecha': forms.DateInput(attrs={'class': INPUT, 'type': 'date'}),
        }


ActividadFormSet = inlineformset_factory(
    Informe, Actividad, form=ActividadForm, extra=1, can_delete=True
)
ParticipanteFormSet = inlineformset_factory(
    Informe, Participante, form=ParticipanteForm, extra=1, can_delete=True
)
ObjetivoFormSet = inlineformset_factory(
    Informe, Objetivo, form=ObjetivoForm, extra=1, can_delete=True
)
AgendaFormSet = inlineformset_factory(
    Informe, Agenda, form=AgendaForm, extra=1, can_delete=True
)
HallazgoFormSet = inlineformset_factory(
    Informe, Hallazgo, form=HallazgoForm, extra=1, can_delete=True
)
FortalezaFormSet = inlineformset_factory(
    Informe, Fortaleza, form=FortalezaForm, extra=1, can_delete=True
)
LimitacionFormSet = inlineformset_factory(
    Informe, Limitacion, form=LimitacionForm, extra=1, can_delete=True
)
RecomendacionFormSet = inlineformset_factory(
    Informe, Recomendacion, form=RecomendacionForm, extra=1, can_delete=True
)
OtrosFormSet = inlineformset_factory(
    Informe, Otros, form=OtrosForm, extra=1, can_delete=True
)
AcuerdoFormSet = inlineformset_factory(
    Informe, Acuerdo, form=AcuerdoForm, extra=1, can_delete=True
)

SECCIONES_FORMSETS = [
    ('actividades', ActividadFormSet, 'Actividades técnicas realizadas', 'actividad'),
    ('participantes', ParticipanteFormSet, 'Cantidad de participantes', 'participante'),
    ('objetivos', ObjetivoFormSet, 'Objetivos de la visita', 'objetivo'),
    ('agendas', AgendaFormSet, 'Agenda desarrollada', 'punto de agenda'),
    ('hallazgos', HallazgoFormSet, 'Hallazgos de la visita', 'hallazgo'),
    ('fortalezas', FortalezaFormSet, 'Fortalezas', 'fortaleza'),
    ('limitaciones', LimitacionFormSet, 'Limitantes u oportunidades de mejora', 'limitante'),
    ('recomendaciones', RecomendacionFormSet, 'Recomendaciones', 'recomendación'),
    ('otros', OtrosFormSet, 'Otros', 'observación'),
    ('acuerdos', AcuerdoFormSet, 'Acuerdos', 'acuerdo'),
]
