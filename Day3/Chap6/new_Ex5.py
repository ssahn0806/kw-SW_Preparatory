y = int(input("임의의 정수(1~9) 입력 : "))

for i in range (1,y+1,1): # step size =1 은 생략하는게 일반적!
    print()
    for t in range (1,y+1,1):
        if i >= t:
            print(1*t,end = '')