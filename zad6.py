def func(a: list, b: list) -> list:
    res1 = a + b
    res1 = [el ** 3 for el in res1]
    res = []
    for el in res1:
        if el not in res:
            res.append(el)
    return res


res = func([1, 2, 3, 4, 5, 6, 7], [2, 7, 4, 12, 8, 1, 20, 6])

print(res)