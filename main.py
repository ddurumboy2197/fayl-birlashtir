def eng_uzun_qator(fayl):
    with open(fayl, 'r') as file:
        qatorlar = file.readlines()
    return max(qatorlar, key=len)

print(eng_uzun_qator('fayl.txt'))
```

Bu kod faylda eng uzun qatorni topish uchun mo'ljallangan. Uning ishlashi uchun quyidagilar sharti bo'ladi:

1. Fayl mavjud bo'lishi kerak.
2. Fayl ichida qatorlar oxirida oxirgi belgi bo'lishi kerak.
3. Fayl ichida qatorlar orasida bo'sh qatorlar bo'lishi mumkin.
