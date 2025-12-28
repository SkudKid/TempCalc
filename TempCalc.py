# TempConverter Written by Miguel Joseph
# Started & completed 12/28/25
# Program 1 of many post-college graduation to practice Python skills. starting basic to work onto more complex work.
#FIXED ON GITHUB, NEW REPO UNDER TEMPCALC

ERROR_NUM = "Invalid input. Please enter a numeric value."
ERROR_MENU = "Invalid menu option. Please enter a numeric value between 1 and 3."

def get_temperature(unit):
    try:
        return float(input(f"Enter temperature in {unit}: "))
    except ValueError:
        print(ERROR_NUM)
        return None

def get_choice():
    try:
        return int(input("Select an option (1-3): "))
    except ValueError:
        print(ERROR_MENU)
        return None

def cel_to_fah(temp): #ask user celsius temperature and convert to fahrenheit
    return temp * (9 / 5) + 32

def fah_to_cel(temp): #ask user fahrenheit temperature and convert to celsius
    return (temp - 32) * 5 / 9

def main(): #display main menu to user and ask for users input for an option
    print("=== Miguel Joseph's Temperature Converter ===")
    print("1. Celsius to Fahrenheit")
    print("2. Fahrenheit to Celsius")
    print("3. Quit")

    while True:
        choice = get_choice()
        if choice is None:
            continue
        elif choice == 1:
            unit = "Celsius"
            cel = get_temperature(unit)
            if cel is None:
                continue
            print(f"{cel}°C is equal to {cel_to_fah(cel):.1f}°F")
        elif choice == 2:
            unit = "Fahrenheit"
            fah = get_temperature(unit)
            if fah is None:
                continue
            print(f"{fah}°F is equal to {fah_to_cel(fah):.1f}°C")
        elif choice == 3:
            print("Goodbye!")
            return 0
        else:
            print(ERROR_MENU)
            continue

if __name__ == "__main__":
    main()