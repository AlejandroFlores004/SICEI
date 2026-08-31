from django.core.paginator import Paginator
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.db.models import Count
from django.utils import timezone

from organizacion.models import Escuela
from actividad.models import Informe, Actividad
from easyaudit.models import CRUDEvent

MESES_ES = [
    "", "enero", "febrero", "marzo", "abril", "mayo", "junio",
    "julio", "agosto", "septiembre", "octubre", "noviembre", "diciembre",
]


def _escuelas_no_visitadas_qs(hoy):
    escuelas_visitadas_ids = Informe.objects.filter(
        fecha__year=hoy.year, fecha__month=hoy.month
    ).values_list('escuela_id', flat=True).distinct()

    return Escuela.objects.filter(estado=True).exclude(
        id__in=escuelas_visitadas_ids
    ).select_related('distrito', 'monitor__usuario')


def dashboardView(request):
    hoy = timezone.localdate()

    escuelas_activas = Escuela.objects.filter(estado=True)
    total_escuelas = escuelas_activas.count()

    escuelas_no_visitadas = _escuelas_no_visitadas_qs(hoy)
    escuelas_no_visitadas_count = escuelas_no_visitadas.count()
    escuelas_visitadas_count = total_escuelas - escuelas_no_visitadas_count
    porcentaje_visitadas = round(
        (escuelas_visitadas_count / total_escuelas) * 100
    ) if total_escuelas else 0

    informes_mes_count = Informe.objects.filter(
        fecha__year=hoy.year, fecha__month=hoy.month
    ).count()

    actividades_top = list(
        Actividad.objects.values('actividad__nombre')
        .annotate(total=Count('id'))
        .order_by('-total')[:8]
    )

    EVENTOS_LABELS = {
        CRUDEvent.CREATE: ('Creación', 'badge-success'),
        CRUDEvent.UPDATE: ('Edición', 'badge-info'),
        CRUDEvent.DELETE: ('Eliminación', 'badge-error'),
    }
    eventos_auditoria = []
    for evento in CRUDEvent.objects.select_related('user', 'content_type').order_by('-datetime')[:6]:
        label, badge = EVENTOS_LABELS.get(evento.event_type, ('Cambio', 'badge-ghost'))
        eventos_auditoria.append({
            'tipo_label': label,
            'tipo_badge': badge,
            'modelo': evento.content_type.name if evento.content_type else '—',
            'objeto': evento.object_repr,
            'usuario': evento.user.get_username() if evento.user else 'Sistema',
            'fecha': evento.datetime,
        })

    context = {
        'mes_actual': f"{MESES_ES[hoy.month]} {hoy.year}",
        'total_escuelas': total_escuelas,
        'escuelas_visitadas_count': escuelas_visitadas_count,
        'escuelas_no_visitadas_count': escuelas_no_visitadas_count,
        'porcentaje_visitadas': porcentaje_visitadas,
        'informes_mes_count': informes_mes_count,
        'escuelas_no_visitadas': escuelas_no_visitadas[:8],
        'actividades_labels': [a['actividad__nombre'] for a in actividades_top],
        'actividades_data': [a['total'] for a in actividades_top],
        'eventos_auditoria': eventos_auditoria,
    }
    return render(request, 'dashboard.html', context)


def escuelasPendientesModal(request):
    hoy = timezone.localdate()
    paginator = Paginator(_escuelas_no_visitadas_qs(hoy), 10)
    page_obj = paginator.get_page(request.GET.get('page'))
    return render(request, 'partials/dashboard/_escuelas_pendientes_tabla.html', {'page_obj': page_obj})


def login_view(request):
    if request.user.is_authenticated:
        return redirect("home")  # change to your home url name

    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect("home")  # change to your home url name
        else:
            messages.error(request, "Invalid username or password.")

    return render(request, "registration/login.html")


def logout_view(request):
    logout(request)
    messages.success(request, "Has cerrado sesión correctamente.")
    return redirect("login")