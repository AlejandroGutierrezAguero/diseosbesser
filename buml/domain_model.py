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

# Classes
Usuario = Class(name="Usuario")

# Usuario class attributes and methods

# Domain Model
domain_model = DomainModel(
    name="Class_Diagram",
    types={Usuario},
    associations={},
    generalizations={},
    metadata=None
)
