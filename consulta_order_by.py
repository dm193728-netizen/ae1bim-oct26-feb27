from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from configuracion import cadena_base_datos
from crear_base_entidades import Veterinario

# 1. Nos conectamos con la base de datos para iniciar una sesión de consulta
engine = create_engine(cadena_base_datos)
Session = sessionmaker(bind=engine)
session = Session()

# 2. Obtenemos todos los veterinarios ordenados alfabéticamente por nombres y apellidos
veterinarios = session.query(Veterinario).order_by(
    Veterinario.nombres_apellidos
).all()

print("=== VETERINARIOS ORDENADOS ALFABÉTICAMENTE (.order_by) ===")
for v in veterinarios:
    print(
        f"{v} | Consultorio: {v.consultorio.nombre_numero} "
        f"| Clínica: {v.consultorio.clinica.nombre_comercial}"
    )