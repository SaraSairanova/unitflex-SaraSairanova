def convert_distance(from_unit:str, to_unit:str, value:float)->float:
    if from_unit == 'kilometers' and to_unit == 'miles':
        return km_to_mile(value)
    elif from_unit == 'miles' and to_unit == 'kilometers':
        return mile_to_km(value)
    else:
        raise ValueError('Invalid conversion: ' + from_unit + ' to ' + to_unit)
def km_to_mile(distance:float) -> float:
    return distance/1.6093

def mile_to_km(distance:float)->float:
    return distance*1.6093