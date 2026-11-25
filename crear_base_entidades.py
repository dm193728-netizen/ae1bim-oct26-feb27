from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.orm import declarative_base, relationship

# Realizamos la importación de la cadena de conexión que fue definida en archivo: configuracion.py
from configuracion import cadena_base_datos

# 1. Creamos el motor de conexión hacia la base de datos SQLite
engine = create_engine(cadena_base_datos)

# 2. Se crea la clase base de la cual heredarán todas nuestras entidades ORM
Base = declarative_base()


# Desccripción de las entidades ORM que representan las tablas de la base de datos

class Clinica(Base):
    __tablename__ = 'clinicas'

    id = Column(Integer, primary_key=True)
    nombre_comercial = Column(String, nullable=False)
    direccion = Column(String, nullable=False)
    medico_responsable = Column(String, nullable=False)

    # Definición de relación 1:N -> Una clínica tiene varios consultorios
    consultorios = relationship(
        "Consultorio",
        back_populates="clinica",
        cascade="all, delete-orphan"
    )

    def __repr__(self):
        return (
            f"Clínica: {self.nombre_comercial} | "
            f"Dirección: {self.direccion} | "
            f"Responsable: {self.medico_responsable}"
        )


class Consultorio(Base):
    __tablename__ = 'consultorios'

    id = Column(Integer, primary_key=True)
    nombre_numero = Column(String, nullable=False)
    especialidad = Column(String, nullable=False)

    # Se establece la clave foránea obligatoria hacia 'clinicas' (1 clínica -> N consultorios)
    clinica_id = Column(Integer, ForeignKey('clinicas.id'), nullable=False)

    # Se establecen las relaciones bidireccionales entre Consultorio y Clinica, así como entre Consultorio y Veterinario
    clinica = relationship("Clinica", back_populates="consultorios")
    veterinarios = relationship(
        "Veterinario",
        back_populates="consultorio",
        cascade="all, delete-orphan"
    )

    def __repr__(self):
        return (
            f"Consultorio: {self.nombre_numero} | "
            f"Especialidad: {self.especialidad}"
        )


class Veterinario(Base):
    __tablename__ = 'veterinarios'

    id = Column(Integer, primary_key=True)
    nombres_apellidos = Column(String, nullable=False)
    correo_electronico = Column(String, nullable=False)
    licencia_profesional = Column(String, nullable=False, unique=True)

    # Se establece la clave foránea obligatoria hacia 'consultorios' (1 consultorio -> N veterinarios)
    consultorio_id = Column(Integer, ForeignKey('consultorios.id'), nullable=False)

    # Se establecen las relaciones bidireccionales entre Veterinario y Consultorio, así como entre Veterinario e HistoriaClinica
    consultorio = relationship("Consultorio", back_populates="veterinarios")
    historias_clinicas = relationship(
        "HistoriaClinica",
        back_populates="veterinario",
        cascade="all, delete-orphan"
    )

    def __repr__(self):
        return (
            f"Veterinario: {self.nombres_apellidos} | "
            f"Licencia: {self.licencia_profesional}"
        )


class HistoriaClinica(Base):
    __tablename__ = 'historias_clinicas'

    id = Column(Integer, primary_key=True)
    fecha_atencion = Column(String, nullable=False)
    diagnostico_principal = Column(String, nullable=False)
    tratamiento_prescrito = Column(String, nullable=False)
    nombre_mascota = Column(String, nullable=False)

    # Se establece la clave foránea obligatoria hacia 'veterinarios' (1 veterinario -> N historias)
    veterinario_id = Column(Integer, ForeignKey('veterinarios.id'), nullable=False)

    # Se establece la relación inversa hacia Veterinario
    veterinario = relationship("Veterinario", back_populates="historias_clinicas")

    def __repr__(self):
        return (
            f"Historia Clínica ID {self.id} | "
            f"Fecha: {self.fecha_atencion} | "
            f"Mascota: {self.nombre_mascota} | "
            f"Diagnóstico: {self.diagnostico_principal}"
        )


# 3. Se genera físicamente todas las tablas en la base de datos SQLite
Base.metadata.create_all(engine)