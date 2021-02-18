PI = 3.14159265358979

def circle_size(radius):
    return PI*(radius**2)
def circle_length(radius):
    return 2*PI*radius
if __name__ == "__main__":
    r = int(input("원의 반지름의 길이를 입력하세요: "))
    print(f'반지름이 {r}인 원의 면적: {circle_size(r)}')
    print(f'반지름이 {r}인 원의 둘레: {circle_length(r)}')
    