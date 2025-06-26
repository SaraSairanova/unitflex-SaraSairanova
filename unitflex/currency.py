def convert_currency(from_unit: str, to_unit: str, value: float) -> float:
    if from_unit == 'usd' and to_unit == 'eur':
        return usd_to_eur(value)
    elif from_unit == 'eur' and to_unit == 'usd':
        return eur_to_usd(value)
    else:
        raise ValueError('Invalid conversion: ' + from_unit + ' to ' + to_unit)
def usd_to_eur(money:float) -> float:
    return money/0.86

def eur_to_usd(money:float)->float:
    return money*0.86