---

# 📗 2. BUILTINS GUIDE (.md)

📄 `BUILTINS_GUIDE.md`

```md id="m2"
# OSCi Built-in Functions 📦

Builtins — OSCi ichidagi tayyor funksiyalar.

Ular Python kutubxonalariga o‘xshaydi, lekin OSCi uchun soddalashtirilgan.

---

# ⚙️ BUILTINS NIMA QILADI?

- matematik funksiyalar
- string ishlash
- fayl tizimi
- system yordamchi funksiyalar
- random / time

---

# 🧩 35 TA BUILTIN FUNKSIYA

## 📢 OUTPUT / INPUT

| Funksiya | Nima qiladi |
|----------|------------|
| chiqar | ekranga chiqaradi |
| kirit | foydalanuvchi input |

---

## 🔢 MATEMATIKA

| Funksiya | Nima qiladi |
|----------|------------|
| qo'sh | qo‘shish |
| ayir | ayirish |
| kopaytir | ko‘paytirish |
| bolish | bo‘lish |
| qoldiq | mod |
| daraja | power |
| max_son | maksimal |
| min_son | minimal |

---

## 🔤 STRING

| Funksiya | Nima qiladi |
|----------|------------|
| matn | stringga o‘tkazish |
| katta | upper case |
| kichik | lower case |
| almashtir | replace |
| boshlanadi | startswith |
| tugaydi | endswith |
| bol | split |
| birlashtir | join |

---

## 📂 FILE SYSTEM

| Funksiya | Nima qiladi |
|----------|------------|
| fayl_yoz | file yozish |
| fayl_oqi | file o‘qish |
| mavjudmi | file bor-yo‘qligini tekshirish |
| o'chir_fayl | file o‘chirish |
| katalog_yarat | papka yaratish |
| katalog_royxat | papka ichini ko‘rish |

---

## ⏱ SYSTEM

| Funksiya | Nima qiladi |
|----------|------------|
| vaqt | timestamp |
| kut | delay (sleep) |

---

## 🎲 RANDOM

| Funksiya | Nima qiladi |
|----------|------------|
| tasodifiy | 0-1 random |
| butun_tasodifiy | range random |

---

## 🧠 HELP

| Funksiya | Nima qiladi |
|----------|------------|
| yordam | barcha funksiyalar ro‘yxati |

---

# 🚀 MISOL

```osc
boshlash

son = qo'sh(10, 20)
chiqar son

matn = katta("salom")
chiqar matn

tugat
