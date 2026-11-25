from sqlalchemy import create_engine, and_
from sqlalchemy.orm import sessionmaker

from configuracion import cadena_base_datos
from crear_base_entidades import HistoriaClinica

# 1. Nos conectamos con la base de datos para iniciar una sesión de consulta
engine = create_engine(cadena_base_datos)
Session = sessionmaker(bind=engine)
session = Session()

# 2. Filtramos las historias clínicas donde la mascota sea "Luna" Y la atención haya sido en marzo de 2026
historias = session.query(HistoriaClinica).filter(
    and_(
        HistoriaClinica.nombre_mascota == "Luna",
        HistoriaClinica.fecha_atencion.like("2026-03%")
    )
).all()

print("=== HISTORIAS CLÍNICAS DE 'Luna' EN MARZO DE 2026 (and_) ===")
for h in historias:
    print(
        f"{h} | Tratamiento: {h.tratamiento_prescrito} "
        f"| Veterinario: {h.veterinario.nombres_apellidos}"
    )