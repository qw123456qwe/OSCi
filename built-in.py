# ===== OSCi BUILT-INS (35 ta) =====

# 1
def chiqar(*args):
    print(*args)

# 2
def kirit(prompt=""):
    return input(prompt)

# 3
def uzunlik(x):
    return len(x)

# 4
def tur(x):
    return type(x).__name__

# 5
def son(x):
    return int(x)

# 6
def haqiqiy(x):
    return float(x)

# 7
def matn(x):
    return str(x)

# 8
def royxat(*args):
    return list(args)

# 9
def qosh(a, b):
    return a + b

# 10
def ayir(a, b):
    return a - b

# 11
def kopaytir(a, b):
    return a * b

# 12
def bolish(a, b):
    return a / b

# 13
def qoldiq(a, b):
    return a % b

# 14
def daraja(a, b):
    return a ** b

# 15
def max_son(*args):
    return max(args)

# 16
def min_son(*args):
    return min(args)

# 17
def tasodifiy():
    import random
    return random.random()

# 18
def butun_tasodifiy(a, b):
    import random
    return random.randint(a, b)

# 19
def vaqt():
    import time
    return time.time()

# 20
def kut(sec):
    import time
    time.sleep(sec)

# 21
def fayl_yoz(nomi, matn):
    with open(nomi, "w", encoding="utf-8") as f:
        f.write(matn)

# 22
def fayl_oqi(nomi):
    with open(nomi, "r", encoding="utf-8") as f:
        return f.read()

# 23
def mavjudmi(nomi):
    import os
    return os.path.exists(nomi)

# 24
def o'chir_fayl(nomi):
    import os
    if os.path.exists(nomi):
        os.remove(nomi)

# 25
def katalog_yarat(nomi):
    import os
    os.makedirs(nomi, exist_ok=True)

# 26
def katalog_royxat(nomi="."):
    import os
    return os.listdir(nomi)

# 27
def birlashtir(*args):
    return "".join(map(str, args))

# 28
def katta(matn):
    return str(matn).upper()

# 29
def kichik(matn):
    return str(matn).lower()

# 30
def almashtir(matn, eski, yangi):
    return str(matn).replace(eski, yangi)

# 31
def boshlanadi(matn, prefix):
    return str(matn).startswith(prefix)

# 32
def tugaydi(matn, suffix):
    return str(matn).endswith(suffix)

# 33
def bol(matn, sep=" "):
    return str(matn).split(sep)

# 34
def birlashtir_royxat(lst, sep=" "):
    return sep.join(map(str, lst))

# 35
def yordam():
    print("OSCi built-in funksiyalar mavjud (35 ta).")
