# Praveen Lama
# IS 211
# Assignment 6
# Fall 2017


class ConversionNotPossibleException(Exception):
    def __init__(self, message):
        self.message = "Conversion is not possible due to unit incompatibility."


def convert(fromUnit, toUnit, value):

    fromIsTempUnit = False
    fromIsDistUnit = False
    toIsTempUnit = False
    toIsDistUnit = False

    if fromUnit == "Fahrenheit" or fromUnit == "Kelvin" or fromUnit == "Celcius":
        fromIsTempUnit = True
    if fromUnit == "Meters" or fromUnit == "Yards" or fromUnit == "Miles":
        fromIsDistUnit = True
    if toUnit == "Fahrenheit" or toUnit == "Kelvin" or toUnit == "Celcius":
        toIsTempUnit = True
    if toUnit == "Meters" or toUnit == "Yards" or toUnit == "Miles":
        toIsDistUnit = True

    if fromIsTempUnit and toIsTempUnit: 
        celcius = value
        if fromUnit == "Kelvin":
            celcius = value - 273.15
        if fromUnit == "Fahrenheit":
            celcius = ((value-32.0)*(5.0/9.0))

        kelvin = celcius + 273.15
        fahrenheit = (celcius*(9.0/5.0))+32

        if toUnit == "Fahrenheit": return fahrenheit
        if toUnit == "Celcius": return celcius
        if toUnit == "Kelvin": return kelvin

    elif fromIsDistUnit and toIsDistUnit: 
        miles = value
        if fromUnit == "Yards":
            miles = value/1760.0
        if fromUnit == "Meters":
            miles = value/1609.344

        yards = miles*1760.0
        meters = miles*1609.344

        if toUnit == "Miles": return miles
        if toUnit == "Yards": return yards
        if toUnit == "Meters": return meters

    else:  
        raise ConversionNotPossibleException("Conversion is not possible due to unit incompatibility.")
