import random

#while True:
num1 = random.randint(1,100)
num2 = random.randint(1,100)

result = int(input(f'{num1}-{num2}='))

if result == (num1-num2) :
    print("정답입니다.")
else :
    print("틀렸습니다.")