# ae1bim-oct25-feb26
# Gestión de Clínicas Veterinarias con SQLAlchemy (AE1)

Este proyecto corresponde a la Actividad Experimental 1 de la asignatura **Desarrollo Basado en Plataformas Web**. El objetivo es modelar e implementar una base de datos relacional en SQLite utilizando Python y el ORM **SQLAlchemy**, sin escribir sentencias SQL manuales.

El sistema gestiona la información operativa de clínicas veterinarias siguiendo una jerarquía de relaciones uno a muchos (**1:N**):

`Clínica` → `Consultorio` → `Veterinario` → `Historia Clínica`

## Modelo de datos

Las entidades se encuentran mapeadas en `crear_base_entidades.py` con las siguientes tablas y atributos:

* **Clínica (`clinicas`):** `id`, `nombre_comercial`, `direccion` y `medico_responsable`. Una clínica puede tener varios consultorios.
* **Consultorio (`consultorios`):** `id`, `nombre_numero`, `especialidad` y `clinica_id`. Cada consultorio pertenece a una clínica y tiene asignados varios veterinarios.
* **Veterinario (`veterinarios`):** `id`, `nombres_apellidos`, `correo_electronico`, `licencia_profesional` (única) y `consultorio_id`. Cada veterinario atiende en un consultorio y registra múltiples historias clínicas.
* **Historia Clínica (`historias_clinicas`):** `id`, `fecha_atencion`, `diagnostico_principal`, `tratamiento_prescrito`, `nombre_mascota` y `veterinario_id`.

## Estructura del proyecto

* `configuracion.py`: Contiene la cadena de conexión (`sqlite:///clinicas_veterinarias.db`) compartida por todos los scripts.
* `crear_base_entidades.py`: Define las clases ORM, claves foráneas, relaciones bidireccionales y genera físicamente las tablas en SQLite.
* `poblar_base.py`: Inserta los registros de prueba (2 clínicas, 3 consultorios, 3 veterinarios y 4 historias clínicas).
* `consulta_all.py`: Lista todas las clínicas usando `.all()` y calcula el total de historias clínicas asociadas a cada una navegando sus relaciones.
* `consulta_filter.py`: Filtra los consultorios de la especialidad `"Cirugía"` mediante `.filter()`.
* `consulta_order_by.py`: Muestra los veterinarios ordenados alfabéticamente por nombre y apellido con `.order_by()`.
* `consulta_or.py`: Busca historias clínicas cuyo diagnóstico contenga `"Infección"` o `"Fractura"` combinando `or_()` y `.like()`.
* `consulta_and.py`: Filtra las historias clínicas de la mascota `"Luna"` atendidas durante marzo de 2026 utilizando `and_()`.
* `clinicas_veterinarias.db`: Base de datos SQLite generada con los datos cargados.

## Requisitos y ejecución

1. **Instalar SQLAlchemy** (si aún no está instalado en el entorno):
   ```bash
   pip install SQLAlchemy
   ```

2. **Crear la base de datos y las tablas:**
   ```bash
   python crear_base_entidades.py
   ```

3. **Cargar los datos iniciales** (ejecutar una sola vez para evitar duplicar licencias profesionales):
   ```bash
   python poblar_base.py
   ```

4. **Ejecutar las consultas:**
   ```bash
   python consulta_all.py
   python consulta_filter.py
   python consulta_order_by.py
   python consulta_or.py
   python consulta_and.py
   ```