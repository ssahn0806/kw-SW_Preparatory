numbers = []
index = 'a'
print("4개의 정수를 입력하시오.")
for i in range(4):
    numbers.append(int(input(f'{chr(ord(index)+i)} : ')))
max = numbers[0]

for i in numbers:
    if i > max:
        max = i
    else :
        continue
print(f'최댓값 : {max}')