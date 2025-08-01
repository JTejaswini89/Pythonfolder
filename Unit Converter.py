print("Temperature Converter:")
def celsiusFahrenheit():
    n = float(input("Enter Celsius value: "))
    f = (n*9/5)+32
    c = (f-32)*5/9
    print(f"Celsius -> Fahrenheit: {f:.2f}")
    print(f"Fahrenheit -> Celsius: {c:.2f}")

def celsiusKelvin():
    n = float(input("Enter Celsius value: "))
    k = n+273.15
    c = k-273.15
    print(f"Celsius -> Kelvin: {k:.2f}")
    print(f"Kelvin -> Celsius: {c:.2f}")

def fahrenheitKelvin():
    n = float(input("Enter Fahrenheit value: "))
    k = ((n-32)*5/9)+273.15
    f = ((k-273.15)*9/5)+ 32
    print(f"Fahrenheit -> Kelvin: {k:.2f}")
    print(f"Kelvin -> Fahrenheit: {f:.2f}")

def unitConverter():
    while True:
        print("\nSelect one of these:")
        print("1. Celsius and Fahrenheit Converter")
        print("2. Celsius and Kelvin Converter")
        print("3. Fahrenheit and Kelvin Converter")
        print("4. Exit")
        choice = input("Enter your choice: ")
        if choice == "1":
            celsiusFahrenheit()
        elif choice == "2":
            celsiusKelvin()
        elif choice == "3":
            fahrenheitKelvin()
        elif choice == "4":
            print("Exiting... Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

unitConverter()
