# OSCi Core Guide 🚀

OSCi — O‘zbekcha programming language interpreter.

---

# 🧠 CORE NIMA QILADI?

`core.py` — bu OSCi ning yuragi.

U:
- `.osc` faylni o‘qiydi
- satrlarni tushunadi
- keywordlarni bajaradi
- builtins bilan ishlaydi
- env (o‘zgaruvchilar) boshqaradi

---

# ⚙️ ASOSIY TUSHUNCHALAR

## 1. env (muhit)
Barcha o‘zgaruvchilar va funksiyalar shu yerda saqlanadi.

---

## 2. execute()
Har bir qatorni tekshiradi va bajaradi.

---

## 3. eval_expr()
Ifodalarni hisoblaydi:
- 5 + 5
- son > 3
- "salom"

---

# 🧩 KEYWORDLAR (35 TA)

| Keyword | Nima qiladi |
|--------|------------|
| boshlash | dastur boshlanishi |
| tugat | dasturni to‘xtatish |
| chiqar | ekranga chiqarish |
| agar | shart (if) |
| bo‘lsa | shart oxiri |
| bo‘lmasa | else |
| aks_holda | elif |
| takror | while sikl |
| har | for sikl |
| qadamda | range for |
| to‘xtat | break |
| keyingisi | continue |
| qaytar | return |
| funktsiya | function |
| sinf | class |
| meros | inheritance |
| yangi | object init |
| o'chir | delete |
| tekshir | assert |
| xato | error |
| usla | try |
| tut | except |
| nihoyat | finally |
| import | module import |
| dan_import | from import |
| global | global variable |
| mahalli | local scope |
| haqiqat | True |
| yolg'on | False |
| bo'sh | None |
| va | and |
| yoki | or |
| emas | not |
| yozuvchi | yield |
| kutuvchi | async |

---

# 🔥 CORE FLOW

```text
.osc file
   ↓
run_file()
   ↓
run_lines()
   ↓
execute()
   ↓
eval_expr()
   ↓
env (builtins + variables)
