def add(x,y):
    return x+y
def sub(x,y):
    return x-y
def mul(x,y):
    return x*y
def div(x,y):
    return x/y
            
        
if __name__ == "__main__":
    print("사칙연산 : 임의의 두 정수를 입력하시오...")
    numbers = []
    index='x'
    for i in range(2):
        numbers.append(int(input(f'{i+1}번째 정수({chr(ord(index)+i)}): ')))
    
    print(f'{numbers[0]} + {numbers[1]} = {add(numbers[0],numbers[1])}')
    print(f'{numbers[0]} - {numbers[1]} = {sub(numbers[0],numbers[1])}')
    print(f'{numbers[0]} * {numbers[1]} = {mul(numbers[0],numbers[1])}')
    print(f'{numbers[0]} / {numbers[1]} = {div(numbers[0],numbers[1])}')