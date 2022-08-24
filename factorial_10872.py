
def factorial(parm):
    if parm<=1:
        return 1

    return parm*factorial(parm-1)

parm=int(input())
print(factorial(parm))