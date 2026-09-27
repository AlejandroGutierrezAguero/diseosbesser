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
Rol: Enumeration = Enumeration(
    name="Rol",
    literals={
            EnumerationLiteral(name="administracion"),
			EnumerationLiteral(name="monitor"),
			EnumerationLiteral(name="mantenimiento")
    }
)

# Classes
Usuario = Class(name="Usuario", metadata=Metadata(description="email like \'%@%\' -----------------------------\ntelefono 9 dígitos -----------------------------------\nDNI like [0-9]{8}[A-Z] ---------------------------\nfechaNac < fechaAlta < fechaBaja"))
Abono = Class(name="Abono", metadata=Metadata(description="Si familiar es false, el abono solo puede tener un abonado. ----------------------------\nfechaIni < fechaFin -------------------------------\ncoste >= 0 ----------------------------------\ncc 24 dígitos"))
TipoAbono = Class(name="TipoAbono", metadata=Metadata(description="duracion >= 1\nprecioIndividual >= 0\nprecioFamiliar >= 0"))
Curso = Class(name="Curso", metadata=Metadata(description="fechaIni < fechaFin\nprecio >= 0"))
TipoCurso = Class(name="TipoCurso", metadata=Metadata(description="aforo > 0\nprecio >= 0\nedadMin >= 0\nedad Max >= 1"))
Empleado = Class(name="Empleado", metadata=Metadata(description="cc 24 dígitos"))
Proceso = Class(name="Proceso", metadata=Metadata(description="fechaIni < fechaFin"))
TipoProceso = Class(name="TipoProceso")
Frecuencia = Class(name="Frecuencia", metadata=Metadata(description="unidad in (\'d\', \'s\', m\', a\')\ncantidad >= 0"))
Fecha = Class(name="Fecha", metadata=Metadata(description="01 <= dia <= 31\n01 <= mes <= 12"))
Cliente = Class(name="Cliente")

# Usuario class attributes and methods
Usuario_telefono: Property = Property(name="telefono", type=StringType)
Usuario_DNI: Property = Property(name="DNI", type=StringType, is_external_id=True)
Usuario_fechaNac: Property = Property(name="fechaNac", type=DateType)
Usuario_fechaAlta: Property = Property(name="fechaAlta", type=DateType)
Usuario_fechaBaja: Property = Property(name="fechaBaja", type=DateType, is_optional=True)
Usuario_idUsuario: Property = Property(name="idUsuario", type=IntegerType, is_id=True)
Usuario_nombre: Property = Property(name="nombre", type=StringType)
Usuario_apellido1: Property = Property(name="apellido1", type=StringType)
Usuario_apellido2: Property = Property(name="apellido2", type=StringType, is_optional=True)
Usuario_email: Property = Property(name="email", type=StringType)
Usuario.attributes={Usuario_DNI, Usuario_apellido1, Usuario_apellido2, Usuario_email, Usuario_fechaAlta, Usuario_fechaBaja, Usuario_fechaNac, Usuario_idUsuario, Usuario_nombre, Usuario_telefono}

# Abono class attributes and methods
Abono_idAbono: Property = Property(name="idAbono", type=IntegerType, is_id=True)
Abono_fechaIni: Property = Property(name="fechaIni", type=DateType)
Abono_fechaFin: Property = Property(name="fechaFin", type=DateType)
Abono_coste: Property = Property(name="coste", type=FloatType)
Abono_cc: Property = Property(name="cc", type=StringType)
Abono_familiar: Property = Property(name="familiar", type=BooleanType)
Abono.attributes={Abono_cc, Abono_coste, Abono_familiar, Abono_fechaFin, Abono_fechaIni, Abono_idAbono}

# TipoAbono class attributes and methods
TipoAbono_idTipoAbono: Property = Property(name="idTipoAbono", type=IntegerType, is_id=True)
TipoAbono_duracion: Property = Property(name="duracion", type=IntegerType)
TipoAbono_precioIndividual: Property = Property(name="precioIndividual", type=FloatType)
TipoAbono_precioFamiliar: Property = Property(name="precioFamiliar", type=FloatType)
TipoAbono.attributes={TipoAbono_duracion, TipoAbono_idTipoAbono, TipoAbono_precioFamiliar, TipoAbono_precioIndividual}

# Curso class attributes and methods
Curso_idCurso: Property = Property(name="idCurso", type=IntegerType, is_id=True)
Curso_nombre: Property = Property(name="nombre", type=StringType)
Curso_fechaIni: Property = Property(name="fechaIni", type=DateType)
Curso_fechaFin: Property = Property(name="fechaFin", type=DateType)
Curso_precio: Property = Property(name="precio", type=FloatType)
Curso.attributes={Curso_fechaFin, Curso_fechaIni, Curso_idCurso, Curso_nombre, Curso_precio}

# TipoCurso class attributes and methods
TipoCurso_idTipoCurso: Property = Property(name="idTipoCurso", type=IntegerType, is_id=True)
TipoCurso_nombre: Property = Property(name="nombre", type=StringType)
TipoCurso_des: Property = Property(name="des", type=StringType)
TipoCurso_aforo: Property = Property(name="aforo", type=IntegerType)
TipoCurso_precio: Property = Property(name="precio", type=FloatType)
TipoCurso_edadMin: Property = Property(name="edadMin", type=IntegerType, is_optional=True)
TipoCurso_edadMax: Property = Property(name="edadMax", type=IntegerType, is_optional=True)
TipoCurso.attributes={TipoCurso_aforo, TipoCurso_des, TipoCurso_edadMax, TipoCurso_edadMin, TipoCurso_idTipoCurso, TipoCurso_nombre, TipoCurso_precio}

# Empleado class attributes and methods
Empleado_cc: Property = Property(name="cc", type=StringType)
Empleado_rol: Property = Property(name="rol", type=Rol)
Empleado.attributes={Empleado_cc, Empleado_rol}

# Proceso class attributes and methods
Proceso_idProceso: Property = Property(name="idProceso", type=IntegerType, is_id=True)
Proceso_fechaIni: Property = Property(name="fechaIni", type=DateType)
Proceso_fechaFin: Property = Property(name="fechaFin", type=DateType)
Proceso_observaciones: Property = Property(name="observaciones", type=StringType, is_optional=True)
Proceso.attributes={Proceso_fechaFin, Proceso_fechaIni, Proceso_idProceso, Proceso_observaciones}

# TipoProceso class attributes and methods
TipoProceso_idTipoProceso: Property = Property(name="idTipoProceso", type=IntegerType, is_id=True)
TipoProceso_nombre: Property = Property(name="nombre", type=StringType)
TipoProceso_desc: Property = Property(name="desc", type=StringType)
TipoProceso_instrucciones: Property = Property(name="instrucciones", type=StringType)
TipoProceso.attributes={TipoProceso_desc, TipoProceso_idTipoProceso, TipoProceso_instrucciones, TipoProceso_nombre}

# Frecuencia class attributes and methods
Frecuencia_cantidad: Property = Property(name="cantidad", type=IntegerType, is_id=True)
Frecuencia_unidad: Property = Property(name="unidad", type=StringType, is_id=True)
Frecuencia.attributes={Frecuencia_cantidad, Frecuencia_unidad}

# Fecha class attributes and methods
Fecha_dia: Property = Property(name="dia", type=IntegerType, is_id=True)
Fecha_mes: Property = Property(name="mes", type=IntegerType, is_id=True)
Fecha.attributes={Fecha_dia, Fecha_mes}

# Cliente class attributes and methods

# Relationships
TipoProceso_Frecuencia: BinaryAssociation = BinaryAssociation(
    name="TipoProceso_Frecuencia",
    ends={
        Property(name="tiposProceso", type=TipoProceso, multiplicity=Multiplicity(0, 9999)),
        Property(name="frecuencia", type=Frecuencia, multiplicity=Multiplicity(0, 1))
    }
)
TipoProceso_Fecha: BinaryAssociation = BinaryAssociation(
    name="TipoProceso_Fecha",
    ends={
        Property(name="tiposProceso", type=TipoProceso, multiplicity=Multiplicity(0, 9999)),
        Property(name="fechas", type=Fecha, multiplicity=Multiplicity(0, 9999))
    }
)
Proceso_TipoProceso: BinaryAssociation = BinaryAssociation(
    name="Proceso_TipoProceso",
    ends={
        Property(name="procesos", type=Proceso, multiplicity=Multiplicity(0, 9999)),
        Property(name="tipoProceso", type=TipoProceso, multiplicity=Multiplicity(1, 1))
    }
)
Proceso_Empleado: BinaryAssociation = BinaryAssociation(
    name="Proceso_Empleado",
    ends={
        Property(name="procesos", type=Proceso, multiplicity=Multiplicity(0, 9999)),
        Property(name="empleados", type=Empleado, multiplicity=Multiplicity(0, 9999))
    }
)
Abono_TipoAbono: BinaryAssociation = BinaryAssociation(
    name="Abono_TipoAbono",
    ends={
        Property(name="abonos", type=Abono, multiplicity=Multiplicity(0, 9999)),
        Property(name="tipoAbono", type=TipoAbono, multiplicity=Multiplicity(1, 1))
    }
)
Curso_TipoCurso: BinaryAssociation = BinaryAssociation(
    name="Curso_TipoCurso",
    ends={
        Property(name="cursos", type=Curso, multiplicity=Multiplicity(0, 9999)),
        Property(name="tipoCurso", type=TipoCurso, multiplicity=Multiplicity(1, 1))
    }
)

# Association Classes
Curso_Cliente: BinaryAssociation = BinaryAssociation(
    name="Curso_Cliente",
    ends={
        Property(name="cursos", type=Curso, multiplicity=Multiplicity(0, 9999)),
        Property(name="clientes", type=Cliente, multiplicity=Multiplicity(0, 9999))
    }
)

InscripcionCurso_fechaInsc: Property = Property(name="fechaInsc", type=DateType)
InscripcionCurso = AssociationClass(
    name="InscripcionCurso",
    attributes={InscripcionCurso_fechaInsc}, association=Curso_Cliente
)

Curso_Empleado: BinaryAssociation = BinaryAssociation(
    name="Curso_Empleado",
    ends={
        Property(name="cursos", type=Curso, multiplicity=Multiplicity(0, 9999)),
        Property(name="monitores", type=Empleado, multiplicity=Multiplicity(0, 9999))
    }
)

Monitoreo_fechaAlta: Property = Property(name="fechaAlta", type=DateType)
Monitoreo_descTareas: Property = Property(name="descTareas", type=StringType, is_optional=True)
Monitoreo = AssociationClass(
    name="Monitoreo",
    attributes={Monitoreo_descTareas, Monitoreo_fechaAlta}, association=Curso_Empleado
)

Cliente_Abono: BinaryAssociation = BinaryAssociation(
    name="Cliente_Abono",
    ends={
        Property(name="abonados", type=Cliente, multiplicity=Multiplicity(1, 9999)),
        Property(name="abonos", type=Abono, multiplicity=Multiplicity(0, 9999))
    }
)

SuscripcionAbono_fechaSus: Property = Property(name="fechaSus", type=DateType)
SuscripcionAbono = AssociationClass(
    name="SuscripcionAbono",
    attributes={SuscripcionAbono_fechaSus}, association=Cliente_Abono
)


# Generalizations
gen_Cliente_Usuario = Generalization(general=Usuario, specific=Cliente)
gen_Empleado_Usuario = Generalization(general=Usuario, specific=Empleado)

# Domain Model
domain_model_metadata = Metadata(
    description="El tipo de Rol del Empleado debe ser mantenimiento",
)

domain_model = DomainModel(
    name="Class_Diagram",
    types={Usuario, Abono, TipoAbono, Curso, TipoCurso, Empleado, Proceso, TipoProceso, Frecuencia, Fecha, Cliente, InscripcionCurso, Monitoreo, SuscripcionAbono, Rol},
    associations={TipoProceso_Frecuencia, TipoProceso_Fecha, Proceso_TipoProceso, Proceso_Empleado, Abono_TipoAbono, Curso_TipoCurso, Curso_Cliente, Curso_Empleado, Cliente_Abono},
    generalizations={gen_Cliente_Usuario, gen_Empleado_Usuario},
    metadata=domain_model_metadata
)
