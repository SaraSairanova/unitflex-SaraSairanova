def convert_temperature(from_unit:str, to_unit:str, value:float)->float: 
    if from_unit == 'fahrenheit' and to_unit == 'celsius':
        return fah_to_cel(value)
    elif from_unit == 'celsius' and to_unit == 'fahrenheit':
        return cel_to_fah(value)
    else:
        raise ValueError('Invalid conversion: ' + from_unit + ' to ' + to_unit)
def fah_to_cel(t:float) -> float:
    return (t-32)*(5/9)

def cel_to_fah(t:float) -> float:
    return (t/(5/9))+32