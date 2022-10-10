def func(a : int) -> bool:
    if a % 2 == 0:
        return True
    return False

res = func(6)

if res:
    print('Liczba jest przysta')
else:
    print('Liczba jest nieparzysta')