from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from configuracion import cadena_base_datos
from crear_base_entidades import Clinica

# 1. Nos conectamos a la base de datos para iniciar una sesión de consulta
engine = create_engine(cadena_base_datos)
Session = sessionmaker(bind=engine)
session = Session()

# 2. Obtenemos todas las clínicas registradas usando .all()
clinicas = session.query(Clinica).all()

print("=== CLÍNICAS Y NÚMERO DE HISTORIAS CLÍNICAS ASOCIADAS ===")
for clinica in clinicas:
    total_historias = 0

    # Navegamos según la jerarquía establecia: 1. Clínica -> 2. Consultorios -> 3. Veterinarios -> 4. Historias Clínicas
    for consultorio in clinica.consultorios:
        for veterinario in consultorio.veterinarios:
            total_historias += len(veterinario.historias_clinicas)

    print(f"Clínica: {clinica.nombre_comercial} | Responsable: {clinica.medico_responsable}")
    print(f"   -> Historias Clínicas asociadas: {total_historias}")
    print("-" * 55)