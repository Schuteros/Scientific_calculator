import math


def solver():
    print("""
With specific formulas we can calculate:

Areas of geometric figures:
 * rectangles, r
 * squares, sq
 * right triangles, rt
 * irregular triangles, it
 * circle, c
 
Volume of solid geometric figures:
 * cuboid, c
 * cylinder, cy

Pythagorean theorem

Circle definitions:
 * length
 * diameter
 * radius

The sum of the internal angles

""")

    print("Choose what to calculate:\n"
          " * Area, a\n"
          " * Volume, v\n"
          " * Pythagorean theorem, pt\n"
          " * Circle definitions, cd\n"
          "* The sum of the internal angles, ts")

    choice = ""

    while choice != "exit":
        try:
            choice = input("Input: ").lower()

            if choice in ["area", "a"]:
                choice = input("Chose the figure to measure area: ").lower()

                if choice in ["rectangle", "r"]:
                    # Reading length from user
                    length = float(input("Rectangle length: "))
                    # Reading width(breadth) from user
                    breadth = float(input("Rectangle width: "))
                    # Calculating area
                    area = length * breadth
                    # Displaying results
                    print(f"Rectangle area is {round(area, 2)}")

                elif choice in ["square", "sq"]:
                    side = int(input("Side length of square: "))
                    area = side * side
                    print("Area of square is " + str(area))

                elif choice in ["right triangles", "rt"]:
                    width = float(input('Side of triangle: '))
                    height = float(input('Height of triangle: '))
                    # calculate the area
                    area = 0.5 * width * height
                    print("Area of right triangle : %.2f" % area)

                elif choice in ["irregular triangle", "ir"]:
                    width = float(input('Side of the irregular triangle: '))
                    height = float(input('Height of the irregular triangle: '))

                    # calculate the area
                    area = 0.5 * width * height

                    print("\n Area of irregular triangle : %.2f" % area)

                elif choice in ["circle", "c"]:
                    r = float(input("Radius of a circle: "))
                    area = math.pi * r * r
                    print("Area of circle: %.2f" % area)

                else:
                    print("There was a problem!")
            elif choice in ["volume", "v"]:
                choice = input("Chose the figure to measure volume: ").lower()

                if choice in ["cuboid", "c"]:
                    # Python Program to Calculate the Volume and Surface Area of Cuboid

                    # Take the input from the User
                    length = float(input("Cuboid length: "))
                    width = float(input("Cuboid width: "))
                    height = float(input("Cuboid height: "))

                    # Calculate the Volume
                    volume = length * width * height

                    # Print the Output
                    print("Volume of cuboid= %.2f" % volume)

                elif choice in ["cylinder", "cy"]:
                    radius = float(input('Radius of cylinder: '))
                    height = float(input('Height of cylinder: '))

                    volume = (1.0/3) * math.pi * radius * radius * height

                    print("Volume of cylinder %.2f" % volume)

                else:
                    print("There was a problem")

            elif choice in ["pythagorean theorem", "pt"]:
                mala = input("Calculate hypotenuse - h or leg - l: ").lower()

                # hypotenuse
                if mala == "h":
                    a = float(input("Length of first leg: "))
                    b = float(input("Length of second leg: "))
                    h = math.sqrt(a ** 2 + b ** 2)
                    print(f"Length of hypotenuse: {h}")
                # leg
                elif mala == "l":
                    a = float(input("Length of leg: "))
                    b = float(input("Length of hypotenuse: "))
                    k = math.sqrt(b ** 2 - a ** 2)
                    print(f"Length of hypotenuse: {k}")
                else:
                    print("There was a problem")

            elif choice in ["circle definitions", "cd"]:
                choice = input("""
    Calculate:
     * radius, r
     * diameter, d
     * length of circle, l""").lower()

                if choice in ["radius, r"]:
                    choice = input("From diameter or length of circle: ").lower()

                    if choice in ["diameter", "d"]:
                        # diametrs uz radius
                        diameter = input("Diameter of radius: ")
                        diameter = float(diameter)
                        radius = diameter / 2
                        print(f"Radius of circle: {radius}")
                    elif choice in ["length of circle", "l"]:
                        # radius uz rinka linijas garumu
                        length = input("Length of a circle: ")
                        length = float(length)
                        radius = length / 2 / math.pi
                        print(f"Radius of a circle:  {radius}")
                    else:
                        print("There was a problem")

                elif choice in ["diameter", "d"]:
                    choice = input("From diameter or length of circle: ").lower()

                    if choice in ["radius", "r"]:
                        # radius uz diametru
                        radius = input("Radius of a circle: ")
                        radius = float(radius)
                        diameter = radius * 2
                        print(f"Diameter of a circle: {diameter}")
                    elif choice in ["length of a circle", "l"]:
                        # Length of a circle to radius
                        length = input("Length of a circle: ")
                        length = float(length)
                        diameter = length / math.pi
                        print(f"Radius of a circle: {diameter}")
                    else:
                        print("There was a problem")

                elif choice in ["length of a circle", "l"]:
                    choice = input("From diameter or radius of circle: ").lower()

                    if choice in ["radius", "r"]:
                        # rinka linijas garums uz radiusu
                        radius = input("Radius of a circle: ")
                        radius = float(radius)
                        length = radius * 2 * math.pi
                        print(f"Length of a circle {length}")
                    elif choice in ["diameter", "d"]:
                        diameter = input("Diameter of a circle: ")
                        diameter = float(diameter)
                        length = diameter * math.pi
                        print(f"Length of a circle {length}")

            elif choice in ["The sum of internal angles", "ts"]:
                n = int(input("Number of sides: "))
                if n < 3:
                    sum_of_angles = 0
                else:
                    sum_of_angles = (n - 2) * 180

                print(f"The sum of internal angles: {sum_of_angles}")

            else:
                print("There was a problem!")

        except ValueError:
            print("There was a problem")
