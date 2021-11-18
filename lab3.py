# ZAD 1
def numbers(n:int):
    print(n)
    n-=1
    if(n!=-1):
        numbers(n)

numbers(5)

# ZAD 2
def fib(n: int) -> int:
    if n==0:
        wynik = 0
    elif n==1:
        wynik = 1
    else:
        wynik = fib(n-1) + fib(n-2)
    return wynik

print(fib(12))

# ZAD 3
def power(number: int, n: int) -> int:
    if n>0:
        wynik = number * power(number,n-1)
    elif n==0:
        wynik=1
    return wynik

print(power(6,2))