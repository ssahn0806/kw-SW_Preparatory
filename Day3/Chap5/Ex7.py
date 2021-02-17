import random

lotto = random.randint(0,99)
num1 = lotto//10
num2 = lotto%10
#print(num1,num2)
guess = int(input("복권번호를 입력하시오(0에서 99사이):"))

print(f'당첨번호는 {lotto} 입니다.')
count = 0
money = 0

if guess//10 == num1 :
    count+=1
if guess%10 == num2 :
    count+=1

if count == 2:
    money = 100
elif count == 1:
    money = 50
else :
    money = 0

if count > 0:
    print(f'상금은 {money}만원입니다.')
else :
    print('상금은 없습니다.')
