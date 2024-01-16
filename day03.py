#2024_01_16_과제01

while True:
    manu = input("1)Fahrenheit -> Celsius   2) Celsius -> Fahrenheit   3) isPrime number program   4)Section isPrime number program : ")
    if manu == '1':
        fahrenheit = float(input('Input Fahrenheit : '))
        print(f'Fahrenheit : {fahrenheit}F, Celsius : {((fahrenheit - 32.0) * 5.0 / 9.0):.4f}C')
    elif manu == '2':
        celsius = float(input('Input Celcius : '))
        print(f'Celsius : {celsius}C, Fahrenheit : {((celsius * 9.0 / 5.0) + 32.0):.4f}F')
    elif manu == '3':
        num = int(input("3 이상의 수를 입력하세요 : "))
        bool = True

        for i in range (3, num-1):
            if num % i == 0:
                bool = False
                print("소수가 아닙니다")
                break
        if bool == True:
            print ("소수입니다")

    elif manu == '4':
        nums = input("두 수를 입력하세요 : ").split()
        num1 = int(nums[0])
        num2 = int(nums[1])

        if num1 > num2:
            num1, num2 = num2, num1

        isPrime = True

        for i in range(num1, num2):
            if i <= 2:
                continue
            for y in range(2, i - 1):
                if i % y == 0:
                    isPrime = False
                    break
                else:
                    isPrime = True
            if isPrime == True:
                print(i , end = " ")
        print()
