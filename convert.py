def convert():
    print("""
Conversions from:

Length:
 * Meter, m
 * Centimeter, cm
 * Kilometer, km
 
Speed: 
 * Kilometers per hour, km/h
 * Meters per second, m/s
 
Mass:
 * Kilograms, kg
 * Grams, g

Area:
 * Square meters, m^2
 * Square centimeters, cm^2
 * Acres, a
 * Hectares, ha
 * Square kilometers, km^2
 
Volume:
 * Cubic meters, m^3
 * Cubic centimeters, cm^3
 
P.S. Sorry, no small units or big units, or imperial units
 """)
    choice = ""
    while choice != "exit":
        try:
            choice = input("From what you want to convert (to exit type \"exit\"): ").lower()

            if choice in ["m", "meter"]:
                choice = input("to cm or km")
                if choice == "cm":
                    meter = int(input("Enter the length in meter:"))
                    centimeter = 100 * meter
                    print("The length in centimetre is", round(centimeter, 2))

                elif choice == "km":
                    m = input("Enter distance in Meter: ")
                    m = float(m)
                    km = m / 1000
                    print("%0.3f Meter = %0.3f Kilometer" % (m, km))

                else:
                    print("There was a problem!")

            elif choice in ["centimeter", "cm"]:
                cm = float(input("Enter distance in centimeters: "))
                m = cm / 100
                print(f"Distance in metres is {round(m)}")

            elif choice in ["kilometer", "km"]:
                km = input("Enter distance in kilometer: ")
                # Converting to float data type
                km = float(km)
                # Converting to meter
                m = km * 1000
                # Displaying output
                print("%0.3f Kilometer = %0.3f Meter" % (km, m))

            elif choice in ["kilometers per hour", "km/h"]:
                kmh = float(input("Speed in km/h: "))
                ms = (kmh * 1000)/3600
                print(f"Speed in m/s {round(ms,2)}")

            elif choice in ["meters per second", "m/s"]:
                ms = float(input("Speed in m/s: "))
                kmh = (ms / 1000)*3600
                print(f"Speed in km/h: {round(kmh, 2)}")

            elif choice in ["kilograms", "kg"]:
                kilograms = float(input("Mass in kilograms: "))
                grams = kilograms * 1000
                print(f"Mass in grams {grams}")

            elif choice in ["grams", "g"]:
                grams = float(input("Mass in grams: "))
                kilograms = grams / 1000
                print(f"Mass in kilograms: {kilograms}")

            elif choice in ["square meters", "m^2"]:
                choice = input("To cm^2, a, ha, or km^2").lower()

                if choice == "cm^2":
                    m2 = input("Area in square meters: ")
                    m2 = float(m2)
                    cm2 = m2 * 10000
                    print("%0.3f m2 = %0.3f cm2" % (m2, cm2))
                elif choice == "a":
                    m2 = input("Area in square meters: ")
                    m2 = float(m2)
                    acre = m2 / 100
                    print("%0.3f m2 = %0.3f āri" % (m2, acre))
                elif choice == "ha":
                    m2 = float(input("Area in square meters: "))
                    ha = m2 / 10000
                    print("%0.3f m2 = %0.3f āri" % (m2, ha))
                elif choice == "km^2":
                    m2 = float(input("Area in square meters: "))
                    km2 = m2 / 100000
                    print("%0.3f m2 = %0.3f āri" % (m2, km2))
                else:
                    print("There was a problem")

            elif choice in ["square centimeters", "cm^2"]:
                cm2 = input("Area in square centimeters: ")
                cm2 = float(cm2)
                m2 = cm2 / 10000
                print("%0.3f cm2 = %0.3f m2" % (cm2, m2))

            elif choice in ["acres", "a"]:
                choice = input("To m^2, ha, km^2").lower()

                if choice == "m^2":
                    a = input("Area in acres: ")
                    a = float(a)
                    m2 = a * 100
                    print("%0.3f a = %0.3f m2" %(a, m2))
                elif choice == "ha":
                    a = input("Area in acres: ")
                    a = float(a)
                    ha = a / 100
                    print("%0.3f a = %0.3f ha" %(a, ha))
                elif choice == "km^2":
                    a = input("Area in acres: ")
                    a = float(a)
                    ha = a / 10000
                    print("%0.3f a = %0.3f km2" %(a, ha))
                else:
                    print("There was a problem!")

            elif choice in ["hectares", "ha"]:
                choice = input("To m^2, a, km^2").lower()

                if choice in ["square metres", "m^2"]:
                    ha = input("Area in acres: ")
                    ha = float(ha)
                    m2 = ha * 10000
                    print("%0.3f ha = %0.3f m2" %(ha, m2))
                elif choice in ["acres", "a"]:
                    ha = input("Area in acres: ")
                    ha = float(ha)
                    a = ha * 100
                    print("%0.3f ha = %0.3f m2" %(ha, a))
                elif choice in ["square kilometres", "km^2"]:
                    ha = input("Area in hectares: ")
                    ha = float(ha)
                    km2 = ha / 100
                    print("%0.3f ha = %0.3f m2" %(ha, km2))
                else:
                    print("There was a problem")

            elif choice in ["square kilometres", "km^2"]:
                choice = input("To m^2, a, ha").lower()

                if choice in ["square metres", "m^2"]:
                    km2 = input("Area in square kilometres: ")
                    km2 = float(km2)
                    ha = km2 * 100
                    print("%0.3f ha = %0.3f m2" % (km2, ha))
                elif choice in ["acres", "a"]:
                    km2 = input("Area in square kilometres: ")
                    km2 = float(km2)
                    a = km2 * 10000
                    print("%0.3f ha = %0.3f m2" % (km2, a))
                elif choice in ["hectares", "ha"]:
                    km2 = input("Area in square kilometres: ")
                    km2 = float(km2)
                    ha = km2 * 100
                    print("%0.3f ha = %0.3f m2" % (km2, ha))
                else:
                    print("There was a problem")

            elif choice in ["cubic meters", "m^3"]:
                m3 = input("Volume in  cubic meters: ")
                m3 = float(m3)
                cm3 = m3 * 1000000
                print("%0.3f m3 = %0.3f cm3" % (m3, cm3))

            elif choice in ["cubic centimeters", "cm^3"]:
                cm3 = input("Volume in cubic centimeters: ")
                cm3 = float(cm3)
                m3 = cm3 / 1000000
                print("%0.3f cm3 = %0.3f m3" % (cm3, m3))

            elif choice == "exit":
                continue

            else:
                print("Sorry, there was a problem!")

        except ValueError:
            print("There was a problem")