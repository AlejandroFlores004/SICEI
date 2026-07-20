# SICEI
## Sistema de Información de Centros Escolares Intervenidos

SICEI es una plataforma web desarrollada para apoyar a la Dirección Departamental de Educación en la gestión, monitoreo y seguimiento de los centros escolares intervenidos.

El sistema centraliza información relacionada con actividades académicas, recursos utilizados, necesidades reportadas por los centros educativos y otros indicadores relevantes para la toma de decisiones.

---

# Objetivos

Proporcionar una herramienta que permita:

- Monitorear los centros escolares intervenidos.
- Registrar actividades realizadas por docentes.
- Dar seguimiento a las necesidades de los centros educativos.
- Gestionar recursos utilizados en actividades académicas.
- Facilitar la toma de decisiones mediante información actualizada y consolidada.
- Generar reportes para autoridades educativas.

---

# Funcionalidades

## Gestión de Centros Escolares

- Registro de centros escolares.
- Administración de directores.
- Consulta de información institucional.

## Gestión Académica

- Administración de ciclos educativos.
- Administración de grados.
- Administración de secciones.
- Asignación de docentes.

## Gestión de Actividades

- Registro de actividades realizadas por docentes.
- Clasificación de actividades.
- Consulta por fecha, grado, sección o docente.
- Registro de recursos utilizados.

## Gestión de Necesidades

- Registro de necesidades reportadas por los centros escolares.
- Seguimiento del estado de atención.
- Consulta de necesidades pendientes y resueltas.

## Gestión de Catálogos

- Tipos de actividades.
- Tipos de recursos.
- Tipos de necesidades.
- Ciclos académicos.
- Secciones.

## Reportes

- Actividades por centro escolar.
- Actividades por docente.
- Actividades por grado y sección.
- Necesidades pendientes.
- Necesidades resueltas.
- Indicadores para la Dirección Departamental.

---

# Arquitectura del Proyecto

```text
sicei/
│
├── catalogos/
├── core/
├── academico/
├── actividades/
├── necesidades/
├── reportes/
│
├── config/
├── docker/
├── requirements/
│
├── docker-compose.yml
├── Dockerfile
└── manage.py
```

---

# Tecnologías Utilizadas

- Python 3.12
- Django
- PostgreSQL
- Docker
- Docker Compose

---

# Requisitos

Antes de iniciar, verificar que se encuentren instalados:

```bash
docker --version
docker compose version
```

---

# Instalación

## Clonar repositorio

```bash
git clone <url-repositorio>
cd sicei
```

---

# Variables de Entorno

Crear un archivo `.env` en la raíz del proyecto.

```env
DEBUG=True

SECRET_KEY=your-secret-key

DB_NAME=sicei
DB_USER=postgres
DB_PASSWORD=postgres
DB_HOST=db
DB_PORT=5432
```

---

# Levantar el Proyecto

## Construir contenedores

```bash
docker compose build
```

## Iniciar servicios

```bash
docker compose up -d
```

## Verificar contenedores

```bash
docker compose ps
```

## Ver logs

```bash
docker compose logs -f
```

---

# Base de Datos

## Crear migraciones

```bash
docker compose exec web python manage.py makemigrations
```

## Aplicar migraciones

```bash
docker compose exec web python manage.py migrate
```

---

# Usuario Administrador

Crear un superusuario para acceder al panel administrativo.

```bash
docker compose exec web python manage.py createsuperuser
```

---

# Acceso al Sistema

Aplicación:

```text
http://localhost:8000
```

Panel Administrativo:

```text
http://localhost:8000/admin
```

---

# Comandos Útiles

## Ingresar al contenedor

```bash
docker compose exec web bash
```

## Ejecutar shell de Django

```bash
docker compose exec web python manage.py shell
```

## Ejecutar pruebas

```bash
docker compose exec web python manage.py test
```

## Reiniciar contenedores

```bash
docker compose restart
```

## Detener servicios

```bash
docker compose down
```

## Eliminar contenedores y volúmenes

```bash
docker compose down -v
```

---

# Estado del Proyecto

## Fase 1 - Diseño

- [x] Levantamiento de requerimientos.
- [x] Diseño conceptual de la base de datos.
- [x] Definición de módulos.
- [x] Configuración inicial del proyecto.
- [ ] Implementación de modelos.
- [ ] Configuración de Django Admin.
- [ ] Sistema de autenticación y permisos.
- [ ] Desarrollo de reportes.
- [ ] Dashboard para toma de decisiones.

---

# Módulos del Sistema

| Módulo | Descripción |
|----------|-------------|
| Catálogos | Información de referencia utilizada por el sistema |
| Core | Gestión de centros escolares y directores |
| Académico | Gestión de docentes, grados y secciones |
| Actividades | Registro de actividades y recursos utilizados |
| Necesidades | Registro y seguimiento de necesidades |
| Reportes | Consultas e indicadores para la toma de decisiones |

---

# Autor

Sistema de Información de Centros Escolares Intervenidos (SICEI)

Proyecto desarrollado para apoyar la gestión y seguimiento de centros escolares intervenidos por la Dirección Departamental de Educación.
