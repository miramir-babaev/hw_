a,b  = map(int, input('Введите сумму и произведение чисел => ').split())
res = []
for i in range(a + b):
    if i == (a * i - b)**0.5:
        res.append(i)
print(*res if len(res) == 2 else res + res)
