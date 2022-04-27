from convert import convert
from solver import solver

print(""""
The scientific calculator v0.0.0

Made by:
    * Uldis Andrejs Kurpnieks
    * Roberts Dimza
    * Gustavs Krists Kalviņš 
    
Menu:
    * Calculator
    * Converters
    * Solvers
    * Exit
""")

choice = ""
while choice != "exit":

    choice = input("Choose from the menu: ").lower()

    if choice == "calculator":
        while choice != "exit":
            choice = input("Expression or type exit to exit:\n").lower()
            if choice != "exit":
                try:
                    answer = eval(choice)
                    print(answer)
                    continue
                except SyntaxError:
                    print("Try again!")
            else:
                choice = ""
                break

    elif choice == "converters":
        convert()
    elif choice == "solvers":
        solver()
    elif choice == "exit":
        continue
    else:
        print("Try again, there was a problem!")
