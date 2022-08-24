

def fibonacci(param):
    if fibonacci_arr[param]!=-1: # 중복 계산 x
        return fibonacci_arr[param]

    fibonacci_arr[param]=fibonacci(param-1)+fibonacci(param-2)
    return fibonacci_arr[param]

param=int(input())
if param==0 or param==1: #input 사전처리
    print(param)
else:
    fibonacci_arr=[-1 for _ in range(param+1)]
    fibonacci_arr[0]=0
    fibonacci_arr[1]=1
    print(fibonacci(param))