from sqlalchemy import create_engine, or_
from sqlalchemy.orm import sessionmaker

from configuracion import cadena_base_datos
from crear_base_entidades import HistoriaClinica

# 1. Nos conectamos con la base de datos para iniciar una sesión de consulta
engine = create_engine(cadena_base_datos)
Session = sessionmaker(bind=engine)
session = Session()

# 2. Filtramos las historias clínicas cuyo diagnóstico contenga "Infección" O "Fractura"
historias = session.query(HistoriaClinica).filter(
    or_(
        HistoriaClinica.diagnostico_principal.like("%Infección%"),
        HistoriaClinica.diagnostico_principal.like("%Fractura%")
    )
).all()

print("=== HISTORIAS CLÍNICAS CON DIAGNÓSTICO DE INFECCIÓN O FRACTURA (or_) ===")
for h in historias:
    print(f"{h} | Veterinario: {h.veterinario.nombres_apellidos}")