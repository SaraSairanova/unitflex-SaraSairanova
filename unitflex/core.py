from .currency import convert_currency
from .distance import convert_distance
from .temperature import convert_temperature
def convert(domain: str, from_unit: str, to_unit: str, value: float) -> float:
    if domain == 'currency':
        return convert_currency(from_unit, to_unit, value)
    elif domain == 'distance':
        return convert_distance(from_unit, to_unit, value)
    elif domain == 'temperature':
        return convert_temperature(from_unit, to_unit, value)
    else:
        raise ValueError('Invalid domain: ' + domain )
    