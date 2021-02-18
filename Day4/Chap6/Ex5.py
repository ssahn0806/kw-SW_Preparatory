sum = 0
while True:
    number = int(input("정수를 입력하시오(종료:0) : "))
    if number == 0:
        break
    else :
        sum += number

print(f'합은 {sum} 입니다.')
