#2024_01_15_PythonProject_day02
while True:
    manu = input("1)Fahrenheit -> Celsius   2) Celsius -> Fahrenheit   3) Quit program :")
    if manu == '3':
        print("End Celsius conversion program")
        break
    if manu == '1':
        fahrenheit = float(input('Input Fahrenheit : '))
        print(f'Fahrenheit : {fahrenheit}F, Celsius : {((fahrenheit - 32.0) * 5.0 / 9.0):.4f}C')
    elif manu == '2':
        celsius = float(input('Input Celcius : '))
        print(f'Celsius : {celsius}C, Fahrenheit : {((celsius * 9.0 / 5.0) + 32.0):.4f}F')

