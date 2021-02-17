score = int(input("성적을 입력하시오: "))
credit = 'F'
if score >= 90 :
    credit = 'A'
elif score >= 80 :
    credit = 'B'
elif score >= 70 :
    credit = 'C'
elif score >= 60 :
    credit = 'D'

print(f'{credit}학점입니다.')