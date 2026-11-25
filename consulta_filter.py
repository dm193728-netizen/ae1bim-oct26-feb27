from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from configuracion import cadena_base_datos
from crear_base_entidades import Consultorio

# 1. Nos conectamos con la base de datos para iniciar una sesión de consulta
engine = create_engine(cadena_base_datos)
Session = sessionmaker(bind=engine)
session = Session()

# 2. Filtramos los consultorios cuya especialidad sea exactamente "Cirugía"
consultorios = session.query(Consultorio).filter(
    Consultorio.especialidad == "Cirugía"
).all()

print("=== CONSULTORIOS DE ESPECIALIDAD 'Cirugía' (.filter) ===")
for c in consultorios:
    print(f"{c} | Clínica: {c.clinica.nombre_comercial}")