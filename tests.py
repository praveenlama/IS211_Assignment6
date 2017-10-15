# Praveen Lama
# IS 211
# Assignment 6
# Fall 2017

import conversions
import unittest
import random
import conversions_refactored


class KnownValues(unittest.TestCase):
    knownValues = ((0.0, 273.15, 32.0),
                    (300.0, 573.15, 572.0),
                    (25.49, 298.64, 77.882),
                    (200, 473.15, 392),
                    (150.00, 423.15, 302.00),
                    (-220.00, 53.15, -364.00),
                    (-40.0, 233.15, -40.0),
                    )

    def testConvertCelciusToKelvin(self):
        print("\nNow testing convertCelciusToKelvin() function:")

        for i in range(0,len(self.knownValues)):
            result = conversions.convertCelciusToKelvin(self.knownValues[i][0]) 
            kelvin = self.knownValues[i][1]
            self.assertEqual(kelvin, result) 
            print("   testing celcius = %f; %f = %f; Passed" % (self.knownValues[i][0], kelvin, result))

    def testConvertCelciusToFahrenheit(self):
        print("\nNow testing convertCelciusToFahrenheit function:")

        for i in range(0,len(self.knownValues)):
            result = conversions.convertCelciusToFahrenheit(self.knownValues[i][0]) 
            fahrenheit = self.knownValues[i][2]
            self.assertEqual(fahrenheit, result) 
            print("   testing celcius = %f; %f = %f; Passed" % (self.knownValues[i][0], fahrenheit, result))

    def testConvertFahrenheitToCelcius(self):
        print("\nNow testing convertFahrenheitToCelcius function:")

        for i in range(0,len(self.knownValues)):
            result = conversions.convertFahrenheitToCelcius(self.knownValues[i][2]) 
            celcius = self.knownValues[i][0]
            self.assertEqual(celcius, result) 
            print("   testing fahrenheit = %f; %f = %f; Passed" % (self.knownValues[i][2], celcius, result))

    def testConvertFahrenheitToKelvin(self):
        print("\nNow testing convertFahrenheitToKelvin function:")

        for i in range(0,len(self.knownValues)):
            result = conversions.convertFahrenheitToKelvin(self.knownValues[i][2]) 
            kelvin = self.knownValues[i][1]
            self.assertEqual(kelvin, result) 
            print("   testing fahrenheit = %f; %f = %f; Passed" % (self.knownValues[i][2], kelvin, result))

    def testConvertKelvinToCelcius(self):
        print("\nNow testing convertKelvinToCelcius function:")

        for i in range(0,len(self.knownValues)):
            result = conversions.convertKelvinToCelcius(self.knownValues[i][1]) 
            celcius = self.knownValues[i][0]
            self.assertEqual(celcius, result) 
            print("   testing kelvin = %f; %f = %f; Passed" % (self.knownValues[i][1], celcius, result))

    def testConvertKelvinToFahrenheit(self):
        print("\nNow testing convertKelvinToFahrenheit function:")

        for i in range(0,len(self.knownValues)):
            result = conversions.convertKelvinToFahrenheit(self.knownValues[i][1]) 
            fahrenheit = self.knownValues[i][2]
            self.assertEqual(fahrenheit, result) 
            print("   testing kelvin = %f; %f = %f; Passed" % (self.knownValues[i][1], fahrenheit, result))


class KnownTemperatureValues(unittest.TestCase):
    knownTemperatureValues = ((0.0, 273.15, 32.0),
                              (300.0, 573.15, 572.0),
                              (25.49, 298.64, 77.882),
                              (200, 473.15, 392),
                              (150.00, 423.15, 302.00),
                              (-220.00, 53.15, -364.00),
                              (-40.0, 233.15, -40.0),
                              )

    def testConvert(self):
        print("\nNow testing convert() function with temperature:")

        for i in range(0, len(self.knownTemperatureValues)):
            print("   TESTING ROUND %i" % (i + 1))

            ck = conversions_refactored.convert("Celcius", "Kelvin", self.knownTemperatureValues[i][0])
            self.assertAlmostEqual(ck, self.knownTemperatureValues[i][1], 4)
            print("      Checking %f celcius is converted to %f kelvin; actual: %f" % (
            self.knownTemperatureValues[i][0], self.knownTemperatureValues[i][1], ck))

            cf = conversions_refactored.convert("Celcius", "Fahrenheit", self.knownTemperatureValues[i][0])
            self.assertAlmostEqual(cf, self.knownTemperatureValues[i][2], 4)
            print("      Checking %f celcius is converted to %f fahrenheit; actual: %f" % (
            self.knownTemperatureValues[i][0], self.knownTemperatureValues[i][2], cf))

            kc = conversions_refactored.convert("Kelvin", "Celcius", self.knownTemperatureValues[i][1])
            self.assertAlmostEqual(kc, self.knownTemperatureValues[i][0], 4)
            print("      Checking %f kelvin is converted to %f celcius; actual: %f" % (
            self.knownTemperatureValues[i][1], self.knownTemperatureValues[i][0], kc))

            kf = conversions_refactored.convert("Kelvin", "Fahrenheit", self.knownTemperatureValues[i][1])
            self.assertAlmostEqual(kf, self.knownTemperatureValues[i][2], 4)
            print("      Checking %f kelvin is converted to %f fahrenheit; actual: %f" % (
            self.knownTemperatureValues[i][1], self.knownTemperatureValues[i][2], kf))

            fc = conversions_refactored.convert("Fahrenheit", "Celcius", self.knownTemperatureValues[i][2])
            self.assertAlmostEqual(fc, self.knownTemperatureValues[i][0], 4)
            print("      Checking %f fahrenheit is converted to %f celcius; actual: %f" % (
            self.knownTemperatureValues[i][2], self.knownTemperatureValues[i][0], fc))

            fk = conversions_refactored.convert("Fahrenheit", "Kelvin", self.knownTemperatureValues[i][2])
            self.assertAlmostEqual(fk, self.knownTemperatureValues[i][1], 4)
            print("      Checking %f fahrenheit is converted to %f kelvin; actual: %f" % (
            self.knownTemperatureValues[i][2], self.knownTemperatureValues[i][1], fk))
            print("")


class KnownDistanceValues(unittest.TestCase):
    knownDistanceValues = ((0, 0, 0),
                           (1, 1760, 1609.344),
                           (15, 26400, 24140.16),
                           (0.0006213712, 1.0936133, 1),
                           (0.0005682, 1, 0.91440))

    def testConvert(self):
        print("\nNow testing convert() function with distance:")

        for i in range(0, len(self.knownDistanceValues)):
            print("   TESTING ROUND %i" % (i + 1))

            iy = conversions_refactored.convert("Miles", "Yards", self.knownDistanceValues[i][0])
            self.assertAlmostEqual(iy, self.knownDistanceValues[i][1], 4)
            print("      Checking %f miles is converted to %f yards; actual: %f" % (
            self.knownDistanceValues[i][0], self.knownDistanceValues[i][1], iy))

            ie = conversions_refactored.convert("Miles", "Meters", self.knownDistanceValues[i][0])
            self.assertAlmostEqual(ie, self.knownDistanceValues[i][2], 4)
            print("      Checking %f miles is converted to %f meters; actual: %f" % (
            self.knownDistanceValues[i][0], self.knownDistanceValues[i][2], ie))

            yi = conversions_refactored.convert("Yards", "Miles", self.knownDistanceValues[i][1])
            self.assertAlmostEqual(yi, self.knownDistanceValues[i][0], 4)
            print("      Checking %f yards is converted to %f miles; actual: %f" % (
            self.knownDistanceValues[i][1], self.knownDistanceValues[i][0], yi))

            ye = conversions_refactored.convert("Yards", "Meters", self.knownDistanceValues[i][1])
            self.assertAlmostEqual(ye, self.knownDistanceValues[i][2], 4)
            print("      Checking %f yards is converted to %f meters; actual: %f" % (
            self.knownDistanceValues[i][1], self.knownDistanceValues[i][2], ye))

            ei = conversions_refactored.convert("Meters", "Miles", self.knownDistanceValues[i][2])
            self.assertAlmostEqual(ei, self.knownDistanceValues[i][0], 4)
            print("      Checking %f meters is converted to %f miles; actual: %f" % (
            self.knownDistanceValues[i][2], self.knownDistanceValues[i][0], ei))

            ey = conversions_refactored.convert("Meters", "Yards", self.knownDistanceValues[i][2])
            self.assertAlmostEqual(ey, self.knownDistanceValues[i][1], 4)
            print("      Checking %f meters is converted to %f yards; actual: %f" % (
            self.knownDistanceValues[i][2], self.knownDistanceValues[i][1], ey))
            print("")


class SanityCheck(unittest.TestCase):
    def testSanity(self):
        print("\nNow testing sanity of convert():")
        for i in range(0, 5):
            print("   TESTING ROUND %i" % (i + 1))

            celciusInput = random.random() * 100
            celciusConverted = conversions_refactored.convert("Celcius", "Celcius", celciusInput)
            self.assertAlmostEqual(celciusInput, celciusConverted, 4)
            print("      %f Celcius converted to Celcius is %f" % (celciusInput, celciusConverted))

            kelvinInput = random.random() * 1000
            kelvinConverted = conversions_refactored.convert("Kelvin", "Kelvin", kelvinInput)
            self.assertAlmostEqual(kelvinInput, kelvinConverted, 4)
            print("      %f Kelvin converted to Kelvin is %f" % (kelvinInput, kelvinConverted))

            fahrenheitInput = random.random() * 100
            fahrenheitConverted = conversions_refactored.convert("Fahrenheit", "Fahrenheit", fahrenheitInput)
            self.assertAlmostEqual(fahrenheitInput, fahrenheitConverted, 4)
            print("      %f Fahrenheit converted to Fahrenheit is %f" % (fahrenheitInput, fahrenheitConverted))

            metersInput = random.random() * 100
            metersConverted = conversions_refactored.convert("Meters", "Meters", metersInput)
            self.assertAlmostEqual(metersInput, metersConverted, 4)
            print("      %f Meters converted to Meters is %f" % (metersInput, metersConverted))

            yardsInput = random.random() * 100
            yardsConverted = conversions_refactored.convert("Yards", "Yards", yardsInput)
            self.assertAlmostEqual(yardsInput, yardsConverted, 4)
            print("      %f Yards converted to Yards is %f" % (yardsInput, yardsConverted))

            milesInput = random.random() * 100
            milesConverted = conversions_refactored.convert("Miles", "Miles", milesInput)
            self.assertAlmostEqual(milesInput, milesConverted, 4)
            print("      %f Miles converted to Miles is %f" % (milesInput, milesConverted))
            print("")


class IncompatibleUnits(unittest.TestCase):
    def testIncompatibleUnits(self):
        print("\nNow testing all incompatible units raises ConversionNotPossibleException:")

        print("   Checking if Miles-Celcius raises ConversionNotPossibleException")
        self.assertRaises(conversions_refactored.ConversionNotPossibleException, conversions_refactored.convert,
                          "Miles", "Celcius", 0)

        print("   Checking if Miles-Kelvin raises ConversionNotPossibleException")
        self.assertRaises(conversions_refactored.ConversionNotPossibleException, conversions_refactored.convert,
                          "Miles", "Kelvin", 0)

        print("   Checking if Miles-Fahrenheit raises ConversionNotPossibleException")
        self.assertRaises(conversions_refactored.ConversionNotPossibleException, conversions_refactored.convert,
                          "Miles", "Fahrenheit", 0)

        print("   Checking if Yards-Celcius raises ConversionNotPossibleException")
        self.assertRaises(conversions_refactored.ConversionNotPossibleException, conversions_refactored.convert,
                          "Yards", "Celcius", 0)

        print("   Checking if Yards-Kelvin raises ConversionNotPossibleException")
        self.assertRaises(conversions_refactored.ConversionNotPossibleException, conversions_refactored.convert,
                          "Yards", "Kelvin", 0)

        print("   Checking if Yards-Fahrenheit raises ConversionNotPossibleException")
        self.assertRaises(conversions_refactored.ConversionNotPossibleException, conversions_refactored.convert,
                          "Yards", "Fahrenheit", 0)

        print("   Checking if Meters-Celcius raises ConversionNotPossibleException")
        self.assertRaises(conversions_refactored.ConversionNotPossibleException, conversions_refactored.convert,
                          "Meters", "Celcius", 0)

        print("   Checking if Meters-Kelvin raises ConversionNotPossibleException")
        self.assertRaises(conversions_refactored.ConversionNotPossibleException, conversions_refactored.convert,
                          "Meters", "Kelvin", 0)

        print("   Checking if Meters-Fahrenheit raises ConversionNotPossibleException")
        self.assertRaises(conversions_refactored.ConversionNotPossibleException, conversions_refactored.convert,
                          "Meters", "Fahrenheit", 0)

        print("   Checking if Celcius-Miles raises ConversionNotPossibleException")
        self.assertRaises(conversions_refactored.ConversionNotPossibleException, conversions_refactored.convert,
                          "Celcius", "Miles", 0)

        print("   Checking if Celcius-Yards raises ConversionNotPossibleException")
        self.assertRaises(conversions_refactored.ConversionNotPossibleException, conversions_refactored.convert,
                          "Celcius", "Yards", 0)

        print("   Checking if Celcius-Meters raises ConversionNotPossibleException")
        self.assertRaises(conversions_refactored.ConversionNotPossibleException, conversions_refactored.convert,
                          "Celcius", "Meters", 0)

        print("   Checking if Kelvin-Miles raises ConversionNotPossibleException")
        self.assertRaises(conversions_refactored.ConversionNotPossibleException, conversions_refactored.convert,
                          "Kelvin", "Miles", 0)

        print("   Checking if Kelvin-Yards raises ConversionNotPossibleException")
        self.assertRaises(conversions_refactored.ConversionNotPossibleException, conversions_refactored.convert,
                          "Kelvin", "Yards", 0)

        print("   Checking if Kelvin-Meters raises ConversionNotPossibleException")
        self.assertRaises(conversions_refactored.ConversionNotPossibleException, conversions_refactored.convert,
                          "Kelvin", "Meters", 0)

        print("   Checking if Fahrenheit-Miles raises ConversionNotPossibleException")
        self.assertRaises(conversions_refactored.ConversionNotPossibleException, conversions_refactored.convert,
                          "Fahrenheit", "Miles", 0)

        print("   Checking if Fahrenheit-Yards raises ConversionNotPossibleException")
        self.assertRaises(conversions_refactored.ConversionNotPossibleException, conversions_refactored.convert,
                          "Fahrenheit", "Yards", 0)

        print("   Checking if Fahrenheit-Meters raises ConversionNotPossibleException")
        self.assertRaises(conversions_refactored.ConversionNotPossibleException, conversions_refactored.convert,
                          "Fahrenheit", "Meters", 0)

if __name__ == "__main__":
    unittest.main()
