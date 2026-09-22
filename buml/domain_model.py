####################
# STRUCTURAL MODEL #
####################

from besser.BUML.metamodel.structural import (
    Class, Property, Method, Parameter,
    BinaryAssociation, Generalization, DomainModel,
    Enumeration, EnumerationLiteral, Multiplicity,
    StringType, IntegerType, FloatType, BooleanType,
    TimeType, DateType, DateTimeType, TimeDeltaType,
    AnyType, Constraint, AssociationClass, Metadata, MethodImplementationType
)

# Enumerations
TipoMensaje: Enumeration = Enumeration(
    name="TipoMensaje",
    literals={
            EnumerationLiteral(name="solicitud"),
			EnumerationLiteral(name="aclaracion")
    }
)

# Classes
Usuario = Class(name="Usuario")
Vehiculo = Class(name="Vehiculo")
Viaje = Class(name="Viaje")
Regla = Class(name="Regla")
Mensaje = Class(name="Mensaje")
Pais = Class(name="Pais")
Marca = Class(name="Marca")
Modelo = Class(name="Modelo")
Localidad = Class(name="Localidad")
Provincia = Class(name="Provincia")

# Usuario class attributes and methods
Usuario_codUsuario: Property = Property(name="codUsuario", type=IntegerType, is_id=True)
Usuario_nombre: Property = Property(name="nombre", type=StringType)
Usuario_apellido1: Property = Property(name="apellido1", type=StringType)
Usuario_apellido2: Property = Property(name="apellido2", type=StringType, is_optional=True)
Usuario_nif: Property = Property(name="nif", type=StringType)
Usuario_telefono: Property = Property(name="telefono", type=StringType)
Usuario_email: Property = Property(name="email", type=StringType)
Usuario_fechaNac: Property = Property(name="fechaNac", type=DateType)
Usuario.attributes={Usuario_apellido1, Usuario_apellido2, Usuario_codUsuario, Usuario_email, Usuario_fechaNac, Usuario_nif, Usuario_nombre, Usuario_telefono}

# Vehiculo class attributes and methods
Vehiculo_codVehiculo: Property = Property(name="codVehiculo", type=IntegerType, is_id=True)
Vehiculo_matricula: Property = Property(name="matricula", type=StringType, is_external_id=True)
Vehiculo_numPlazas: Property = Property(name="numPlazas", type=IntegerType)
Vehiculo_color: Property = Property(name="color", type=StringType)
Vehiculo_descripcion: Property = Property(name="descripcion", type=StringType, is_optional=True)
Vehiculo.attributes={Vehiculo_codVehiculo, Vehiculo_color, Vehiculo_descripcion, Vehiculo_matricula, Vehiculo_numPlazas}

# Viaje class attributes and methods
Viaje_codViaje: Property = Property(name="codViaje", type=IntegerType, is_id=True)
Viaje_fechaHoraSalida: Property = Property(name="fechaHoraSalida", type=DateTimeType)
Viaje_numPlazas: Property = Property(name="numPlazas", type=IntegerType)
Viaje_precioPersona: Property = Property(name="precioPersona", type=FloatType)
Viaje_aceptacionAuto: Property = Property(name="aceptacionAuto", type=BooleanType)
Viaje.attributes={Viaje_aceptacionAuto, Viaje_codViaje, Viaje_fechaHoraSalida, Viaje_numPlazas, Viaje_precioPersona}

# Regla class attributes and methods
Regla_codRegla: Property = Property(name="codRegla", type=IntegerType, is_id=True)
Regla_nombre: Property = Property(name="nombre", type=StringType)
Regla.attributes={Regla_codRegla, Regla_nombre}

# Mensaje class attributes and methods
Mensaje_codMensaje: Property = Property(name="codMensaje", type=IntegerType, is_id=True)
Mensaje_tipo: Property = Property(name="tipo", type=TipoMensaje)
Mensaje_fecha: Property = Property(name="fecha", type=DateTimeType)
Mensaje_texto: Property = Property(name="texto", type=StringType)
Mensaje.attributes={Mensaje_codMensaje, Mensaje_fecha, Mensaje_texto, Mensaje_tipo}

# Pais class attributes and methods
Pais_codPais: Property = Property(name="codPais", type=IntegerType, is_id=True)
Pais_nombre: Property = Property(name="nombre", type=StringType)
Pais.attributes={Pais_codPais, Pais_nombre}

# Marca class attributes and methods
Marca_codMarca: Property = Property(name="codMarca", type=IntegerType, is_id=True)
Marca_nombre: Property = Property(name="nombre", type=StringType)
Marca.attributes={Marca_codMarca, Marca_nombre}

# Modelo class attributes and methods
Modelo_codModelo: Property = Property(name="codModelo", type=IntegerType, is_id=True)
Modelo_nombre: Property = Property(name="nombre", type=StringType)
Modelo.attributes={Modelo_codModelo, Modelo_nombre}

# Localidad class attributes and methods
Localidad_codLocalidad: Property = Property(name="codLocalidad", type=IntegerType, is_id=True)
Localidad_nombre: Property = Property(name="nombre", type=StringType)
Localidad.attributes={Localidad_codLocalidad, Localidad_nombre}

# Provincia class attributes and methods
Provincia_codProvincia: Property = Property(name="codProvincia", type=IntegerType, is_id=True)
Provincia_nombre: Property = Property(name="nombre", type=StringType)
Provincia.attributes={Provincia_codProvincia, Provincia_nombre}

# Relationships
Viaje_Vehiculo: BinaryAssociation = BinaryAssociation(
    name="Viaje_Vehiculo",
    ends={
        Property(name="viajes", type=Viaje, multiplicity=Multiplicity(0, 9999)),
        Property(name="vehiculo", type=Vehiculo, multiplicity=Multiplicity(1, 1))
    }
)
Regla_Viaje: BinaryAssociation = BinaryAssociation(
    name="Regla_Viaje",
    ends={
        Property(name="reglas", type=Regla, multiplicity=Multiplicity(0, 9999)),
        Property(name="viajes", type=Viaje, multiplicity=Multiplicity(0, 9999))
    }
)
Mensaje_Viaje: BinaryAssociation = BinaryAssociation(
    name="Mensaje_Viaje",
    ends={
        Property(name="mensajes", type=Mensaje, multiplicity=Multiplicity(0, 9999)),
        Property(name="viaje", type=Viaje, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
Mensaje_Usuario: BinaryAssociation = BinaryAssociation(
    name="Mensaje_Usuario",
    ends={
        Property(name="mensEscritos", type=Mensaje, multiplicity=Multiplicity(0, 9999)),
        Property(name="origen", type=Usuario, multiplicity=Multiplicity(1, 1))
    }
)
Mensaje_Usuario_1: BinaryAssociation = BinaryAssociation(
    name="Mensaje_Usuario_1",
    ends={
        Property(name="mensRecibidos", type=Mensaje, multiplicity=Multiplicity(0, 9999)),
        Property(name="destino", type=Usuario, multiplicity=Multiplicity(1, 1))
    }
)
Usuario_Pais: BinaryAssociation = BinaryAssociation(
    name="Usuario_Pais",
    ends={
        Property(name="usuarios", type=Usuario, multiplicity=Multiplicity(0, 9999)),
        Property(name="nacionalidad", type=Pais, multiplicity=Multiplicity(1, 1))
    }
)
Usuario_Vehiculo: BinaryAssociation = BinaryAssociation(
    name="Usuario_Vehiculo",
    ends={
        Property(name="duenho", type=Usuario, multiplicity=Multiplicity(1, 1)),
        Property(name="vehiculos", type=Vehiculo, multiplicity=Multiplicity(1, 9999))
    }
)
Viaje_Localidad: BinaryAssociation = BinaryAssociation(
    name="Viaje_Localidad",
    ends={
        Property(name="viajesOrigen", type=Viaje, multiplicity=Multiplicity(0, 9999)),
        Property(name="origen", type=Localidad, multiplicity=Multiplicity(1, 1))
    }
)
Viaje_Localidad_1: BinaryAssociation = BinaryAssociation(
    name="Viaje_Localidad_1",
    ends={
        Property(name="viajesDestino", type=Viaje, multiplicity=Multiplicity(0, 9999)),
        Property(name="destino", type=Localidad, multiplicity=Multiplicity(1, 1))
    }
)
Localidad_Provincia: BinaryAssociation = BinaryAssociation(
    name="Localidad_Provincia",
    ends={
        Property(name="localidades", type=Localidad, multiplicity=Multiplicity(0, 9999)),
        Property(name="provincia", type=Provincia, multiplicity=Multiplicity(1, 1))
    }
)
Provincia_Pais: BinaryAssociation = BinaryAssociation(
    name="Provincia_Pais",
    ends={
        Property(name="provincias", type=Provincia, multiplicity=Multiplicity(0, 9999)),
        Property(name="pais", type=Pais, multiplicity=Multiplicity(1, 1))
    }
)
Vehiculo_Modelo: BinaryAssociation = BinaryAssociation(
    name="Vehiculo_Modelo",
    ends={
        Property(name="vehiculos", type=Vehiculo, multiplicity=Multiplicity(0, 9999)),
        Property(name="modelo", type=Modelo, multiplicity=Multiplicity(1, 1))
    }
)
Modelo_Marca: BinaryAssociation = BinaryAssociation(
    name="Modelo_Marca",
    ends={
        Property(name="modelos", type=Modelo, multiplicity=Multiplicity(0, 9999)),
        Property(name="marca", type=Marca, multiplicity=Multiplicity(1, 1))
    }
)

# Association Classes
Viaje_Usuario: BinaryAssociation = BinaryAssociation(
    name="Viaje_Usuario",
    ends={
        Property(name="viajes", type=Viaje, multiplicity=Multiplicity(0, 9999)),
        Property(name="pasajeros", type=Usuario, multiplicity=Multiplicity(1, 9999))
    }
)

Viajero_fechaHoraAceptacion: Property = Property(name="fechaHoraAceptacion", type=DateTimeType)
Viajero = AssociationClass(
    name="Viajero",
    attributes={Viajero_fechaHoraAceptacion}, association=Viaje_Usuario
)

Usuario_Usuario: BinaryAssociation = BinaryAssociation(
    name="Usuario_Usuario",
    ends={
        Property(name="valorado", type=Usuario, multiplicity=Multiplicity(0, 9999)),
        Property(name="valorador", type=Usuario, multiplicity=Multiplicity(0, 9999))
    }
)

Valoracion_texto: Property = Property(name="texto", type=StringType)
Valoracion_valor: Property = Property(name="valor", type=IntegerType)
Valoracion_fechaHora: Property = Property(name="fechaHora", type=DateTimeType)
Valoracion = AssociationClass(
    name="Valoracion",
    attributes={Valoracion_fechaHora, Valoracion_texto, Valoracion_valor}, association=Usuario_Usuario
)


# Domain Model
domain_model = DomainModel(
    name="Class_Diagram",
    types={Usuario, Vehiculo, Viaje, Regla, Mensaje, Pais, Marca, Modelo, Localidad, Provincia, Viajero, Valoracion, TipoMensaje},
    associations={Viaje_Vehiculo, Regla_Viaje, Mensaje_Viaje, Mensaje_Usuario, Mensaje_Usuario_1, Usuario_Pais, Usuario_Vehiculo, Viaje_Localidad, Viaje_Localidad_1, Localidad_Provincia, Provincia_Pais, Vehiculo_Modelo, Modelo_Marca, Viaje_Usuario, Usuario_Usuario},
    generalizations={},
    metadata=None
)
