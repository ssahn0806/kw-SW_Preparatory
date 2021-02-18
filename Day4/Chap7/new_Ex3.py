import time
def fibonacci(n):

    fib = []
    fib.append(1)
    fib.append(1)
    for i in range(2,n):
        fib.append(fib[i-2]+fib[i-1])
    return fib[n-1]
        
if __name__ == "__main__":
    print("### 피보나치 수열 구하기(비재귀) ###")
    print("\n"*2)
    count = int(input("몇 번째 수열까지 출력할까요 : "))
    start = time.time()
    for i in range(1,count+1):
        print("%8d" %fibonacci(i),end='\t')
        #print(f'\t{fibonacci(i)}',end='\t')
        if i%5 == 0:
            print()
    print(f'\n실행시간:{time.time()-start}')
