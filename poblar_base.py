from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from configuracion import cadena_base_datos
from crear_base_entidades import Clinica, Consultorio, Veterinario, HistoriaClinica

# 1. Conectamos con el motor y creamos una sesión de trabajo
engine = create_engine(cadena_base_datos)
Session = sessionmaker(bind=engine)
session = Session()

# 2. Creamos las instancias de Clínicas (Nivel 1)
clinica1 = Clinica(
    nombre_comercial="Patitas y Bigotes",
    direccion="Quito - Av. Universitaria y 18 de Noviembre",
    medico_responsable="Dr. Carlos Ruiz"
)
clinica2 = Clinica(
    nombre_comercial="Mi amigo bigotes",
    direccion="Quito - Calle 10 de Agosto y Bolívar",
    medico_responsable="Dra. María Paz"
)

# 3. Creamos instancias de Consultorios asociados a cada Clínica (Nivel 2)
cons1 = Consultorio(
    nombre_numero="Consultorio 101",
    especialidad="Medicina General",
    clinica=clinica1
)
cons2 = Consultorio(
    nombre_numero="Consultorio 102",
    especialidad="Cirugía",
    clinica=clinica1
)
cons3 = Consultorio(
    nombre_numero="Consultorio 201",
    especialidad="Dermatología",
    clinica=clinica2
)

# 4. Creamos instancias de Veterinarios asociados a cada Consultorio (Nivel 3)
vet1 = Veterinario(
    nombres_apellidos="Juan Pérez",
    correo_electronico="juan.perez@patitas.com",
    licencia_profesional="LIC-001",
    consultorio=cons1
)
vet2 = Veterinario(
    nombres_apellidos="Ana Gómez",
    correo_electronico="ana.gomez@patitas.com",
    licencia_profesional="LIC-002",
    consultorio=cons2
)
vet3 = Veterinario(
    nombres_apellidos="Luis Torres",
    correo_electronico="luis.torres@bigotes.com",
    licencia_profesional="LIC-003",
    consultorio=cons3
)

# 5. Creamos las instancias de Historias Clínicas elaboradas por cada Veterinario (Nivel 4)
hist1 = HistoriaClinica(
    fecha_atencion="2026-03-01",
    diagnostico_principal="Infección estomacal",
    tratamiento_prescrito="Antibiótico oral por 7 días",
    nombre_mascota="Firulais",
    veterinario=vet1
)
hist2 = HistoriaClinica(
    fecha_atencion="2026-03-02",
    diagnostico_principal="Fractura de pata",
    tratamiento_prescrito="Cirugía ortopédica y reposo",
    nombre_mascota="Luna",
    veterinario=vet2
)
hist3 = HistoriaClinica(
    fecha_atencion="2026-03-03",
    diagnostico_principal="Dermatitis alérgica",
    tratamiento_prescrito="Baños medicados semanales",
    nombre_mascota="Max",
    veterinario=vet3
)
hist4 = HistoriaClinica(
    fecha_atencion="2026-03-04",
    diagnostico_principal="Control general",
    tratamiento_prescrito="Vacunación anual",
    nombre_mascota="Rocky",
    veterinario=vet1
)

# 6. Agregagamos todos los objetos a la sesión y confirmamos los cambios en SQLite
session.add_all([
    clinica1, clinica2,
    cons1, cons2, cons3,
    vet1, vet2, vet3,
    hist1, hist2, hist3, hist4
])
session.commit()

print("Datos insertados correctamente en la base de datos.")