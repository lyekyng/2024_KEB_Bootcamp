#for x in range (1, 6):
#    for y in range(6 , 0, -1):
nums = input("두 수를 입력하세요 : ").split()
num1 = int(nums[0])
num2 = int(nums[1])

if num1 > num2:
    tmp = num1
    num1 = num2
    num2 = tmp

isPrime = True

for i in range(num1, num2):
    if i <= 2:
        continue
    for y in range(2, i-1):
        if i%y == 0:
            print(f"{i}는 소수가 아님")
            isPrime = False
            break
        else:
            isPrime = True
    if isPrime == True:
        print(f"{i}는 소수임")



