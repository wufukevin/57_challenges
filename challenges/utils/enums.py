from enum import Enum


class MeasureUnit(Enum):
    Imperial = 'Imperial'
    Metric = 'Metric'


class ImperialLengthUnit(Enum):
    Feet = 'Feet'
    Inches = 'Inches'


class ImperialWeightUnit(Enum):
    Pounds = 'Pounds'
    Stones = 'Stones'


class MetricLengthUnit(Enum):
    Meter = 'Meter'
    Centimeter = 'Centimeter'


class MetricWeightUnit(Enum):
    Kilogram = 'Kilogram'
    Gram = 'Gram'
