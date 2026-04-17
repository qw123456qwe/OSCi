# ============================================================    
#   O'ZBEKCHA INTERPRETER — 35 ta o'z keyword bilan    
# ============================================================    
# 35 ta O'ZBEKCHA KEYWORD:    
#  1.  boshlash       — dastur boshi    
#  2.  tugat          — dasturni to'xtat    
#  3.  chiqar         — ekranga chiqar (print)    
#  4.  agar           — shart (if)    
#  5.  bo'lsa         — shart oxiri (then)    
#  6.  bo'lmasa       — aks holda (else)    
#  7.  aks_holda      — elif (else if)    
#  8.  takror         — while sikli    
#  9.  har            — for sikli    
# 10.  qadamda        — for ... in range(...)    
# 11.  to'xtat        — break    
# 12.  keyingisi      — continue    
# 13.  qaytar         — return    
# 14.  funktsiya      — def    
# 15.  sinf           — class    
# 16.  meros          — extends / inherit    
# 17.  yangi          — new / __init__ call    
# 18.  o'chir         — del    
# 19.  tekshir        — assert    
# 20.  xato           — raise Exception    
# 21.  usla           — try    
# 22.  tut            — except    
# 23.  nihoyat        — finally    
# 24.  import         — import (modul olish)    
# 25.  dan_import     — from ... import ...    
# 26.  global         — global o'zgaruvchi    
# 27.  mahalli        — nonlocal    
# 28.  haqiqat        — True    
# 29.  yolg'on        — False    
# 30.  bo'sh          — None    
# 31.  va             — and    
# 32.  yoki           — or    
# 33.  emas           — not    
# 34.  yozuvchi       — yield (generator)    
# 35.  kutuvchi       — async/await    
# ============================================================    
    
import re    
import sys    
import math    
import importlib    
    
    
def run_file(path):    
    with open(path, "r", encoding="utf-8") as f:    
        raw_lines = f.readlines()    
    
    lines = [l.rstrip("\n") for l in raw_lines]    
    run_lines(lines)    
    
    
def run_lines(lines):
    env = {
        "haqiqat": True,
        "yolg'on": False,
        "bo'sh": None,
    }

    # 🔥 builtins ni qo‘shamiz
    for name in dir(osc_builtins):
        if not name.startswith("_"):
            env[name] = getattr(osc_builtins, name)

    i = 0
    while i < len(lines):
        i = execute(lines, i, env)    
# ============================================================    
#   ASOSIY IJRO    
# ============================================================    
    
def execute(lines, i, env):    
    line = lines[i].strip()    
    
    # Bo'sh yoki izoh    
    if not line or line.startswith("#"):    
        return i + 1    
    
    tokens = line.split()    
    keyword = tokens[0]    
    
    # --------------------------------------------------------    
    # 1. boshlash    
    # --------------------------------------------------------    
    if keyword == "boshlash":    
        print("🚀 Dastur boshlandi")    
        return i + 1    
    
    # --------------------------------------------------------    
    # 2. tugat    
    # --------------------------------------------------------    
    if keyword == "tugat":    
        print("🛑 Dastur tugadi")    
        sys.exit(0)    
    
    # --------------------------------------------------------    
    # 3. chiqar    
    # --------------------------------------------------------    
    if keyword == "chiqar":    
        expr = line[len("chiqar"):].strip()    
        val = eval_expr(expr, env)    
        print(val)    
        return i + 1    
    
    # --------------------------------------------------------    
    # 4-7. agar ... bo'lsa / bo'lmasa / aks_holda    
    # --------------------------------------------------------    
    if keyword == "agar":    
        return exec_if(lines, i, env)    
    
    # --------------------------------------------------------    
    # 8. takror (while)    
    # --------------------------------------------------------    
    if keyword == "takror":    
        return exec_while(lines, i, env)    
    
    # --------------------------------------------------------    
    # 9-10. har / qadamda (for)    
    # --------------------------------------------------------    
    if keyword == "har" or keyword == "qadamda":    
        return exec_for(lines, i, env)    
    
    # --------------------------------------------------------    
    # 11. to'xtat (break)    
    # --------------------------------------------------------    
    if keyword == "to'xtat":    
        raise BreakSignal()    
    
    # --------------------------------------------------------    
    # 12. keyingisi (continue)    
    # --------------------------------------------------------    
    if keyword == "keyingisi":    
        raise ContinueSignal()    
    
    # --------------------------------------------------------    
    # 13. qaytar (return)    
    # --------------------------------------------------------    
    if keyword == "qaytar":    
        expr = line[len("qaytar"):].strip()    
        val = eval_expr(expr, env) if expr else None    
        raise ReturnSignal(val)    
    
    # --------------------------------------------------------    
    # 14. funktsiya (def)    
    # --------------------------------------------------------    
    if keyword == "funktsiya":    
        return exec_def(lines, i, env)    
    
    # --------------------------------------------------------    
    # 15-16. sinf / meros (class)    
    # --------------------------------------------------------    
    if keyword == "sinf":    
        return exec_class(lines, i, env)    
    
    # --------------------------------------------------------    
    # 18. o'chir (del)    
    # --------------------------------------------------------    
    if keyword == "o'chir":    
        var = tokens[1]    
        if var in env:    
            del env[var]    
        return i + 1    
    
    # --------------------------------------------------------    
    # 19. tekshir (assert)    
    # --------------------------------------------------------    
    if keyword == "tekshir":    
        expr = line[len("tekshir"):].strip()    
        val = eval_expr(expr, env)    
        if not val:    
            raise AssertionError(f"tekshir muvaffaqiyatsiz: {expr}")    
        return i + 1    
    
    # --------------------------------------------------------    
    # 20. xato (raise)    
    # --------------------------------------------------------    
    if keyword == "xato":    
        msg = line[len("xato"):].strip().strip('"').strip("'")    
        raise RuntimeError(f"❌ Xato: {msg}")    
    
    # --------------------------------------------------------    
    # 21-23. usla / tut / nihoyat (try/except/finally)    
    # --------------------------------------------------------    
    if keyword == "usla":    
        return exec_try(lines, i, env)    
    
    # --------------------------------------------------------    
    # 24. import    
    # --------------------------------------------------------    
    if keyword == "import":    
        mod_name = tokens[1]    
        alias = tokens[3] if len(tokens) > 3 and tokens[2] == "sifatida" else mod_name    
        env[alias] = importlib.import_module(mod_name)    
        return i + 1    
    
    # --------------------------------------------------------    
    # 25. dan_import (from X import Y)    
    # --------------------------------------------------------    
    if keyword == "dan_import":    
        # dan_import math olib sqrt    
        mod_name = tokens[1]    
        func_name = tokens[3] if len(tokens) > 3 else None    
        mod = importlib.import_module(mod_name)    
        if func_name:    
            env[func_name] = getattr(mod, func_name)    
        return i + 1    
    
    # --------------------------------------------------------    
    # 26. global    
    # --------------------------------------------------------    
    if keyword == "global":    
        # global nom = qiymat    
        rest = line[len("global"):].strip()    
        if "=" in rest:    
            var, val_str = rest.split("=", 1)    
            env[var.strip()] = eval_expr(val_str.strip(), env)    
        return i + 1    
    
    # --------------------------------------------------------    
    # 27. mahalli (nonlocal-like — ichki env belgisi)    
    # --------------------------------------------------------    
    if keyword == "mahalli":    
        var = tokens[1]    
        env[f"__mahalli_{var}"] = True    
        return i + 1    
    
    # --------------------------------------------------------    
    # 34. yozuvchi (yield - generatorni ro'yxatga yig'ish)    
    # --------------------------------------------------------    
    if keyword == "yozuvchi":    
        expr = line[len("yozuvchi"):].strip()    
        val = eval_expr(expr, env)    
        if "__generator_list" not in env:    
            env["__generator_list"] = []    
        env["__generator_list"].append(val)    
        return i + 1    
    
    # --------------------------------------------------------    
    # 35. kutuvchi (async simulation — natijani saqlaydi)    
    # --------------------------------------------------------    
    if keyword == "kutuvchi":    
        expr = line[len("kutuvchi"):].strip()    
        val = eval_expr(expr, env)    
        env["__kutuvchi_natija"] = val    
        print(f"⏳ Kutuvchi natija: {val}")    
        return i + 1    
    
    # --------------------------------------------------------    
    # O'ZGARUVCHI TAYINLASH:  nom = qiymat    
    # --------------------------------------------------------    
    if "=" in line and not line.startswith("="):    
        return exec_assign(line, i, env)    
    
    # --------------------------------------------------------    
    # Noma'lum    
    # --------------------------------------------------------    
    print(f"⚠️  Noma'lum buyruq: {line}")    
    return i + 1    
    
    
# ============================================================    
#   IF / ELIF / ELSE    
# ============================================================    
    
def exec_if(lines, start, env):    
    """    
    agar <shart> bo'lsa    
        ...    
    aks_holda <shart> bo'lsa    
        ...    
    bo'lmasa    
        ...    
    tugat_agar    
    """    
    branches = []   # (condition_str | None, [body_lines])    
    current_cond = lines[start].strip()    
    current_cond = re.sub(r"^agar\s+", "", current_cond)    
    current_cond = re.sub(r"\s+bo'lsa$", "", current_cond)    
    current_body = []    
    i = start + 1    
    
    while i < len(lines):    
        stripped = lines[i].strip()    
    
        if stripped.startswith("aks_holda"):    
            branches.append((current_cond, current_body))    
            current_cond = re.sub(r"^aks_holda\s+", "", stripped)    
            current_cond = re.sub(r"\s+bo'lsa$", "", current_cond)    
            current_body = []    
    
        elif stripped == "bo'lmasa":    
            branches.append((current_cond, current_body))    
            current_cond = None    
            current_body = []    
    
        elif stripped == "tugat_agar":    
            branches.append((current_cond, current_body))    
            i += 1    
            break    
    
        else:    
            current_body.append(lines[i])    
    
        i += 1    
    
    # Bajar    
    for cond, body in branches:    
        if cond is None:    
            run_block(body, env)    
            break    
        if eval_expr(cond, env):    
            run_block(body, env)    
            break    
    
    return i    
    
    
# ============================================================    
#   WHILE (takror)    
# ============================================================    
    
def exec_while(lines, start, env):    
    """    
    takror <shart> bo'lguncha    
        ...    
    tugat_takror    
    """    
    header = lines[start].strip()    
    cond_str = re.sub(r"^takror\s+", "", header)    
    cond_str = re.sub(r"\s+bo'lguncha$", "", cond_str)    
    
    body = []    
    i = start + 1    
    while i < len(lines):    
        if lines[i].strip() == "tugat_takror":    
            i += 1    
            break    
        body.append(lines[i])    
        i += 1    
    
    while eval_expr(cond_str, env):    
        try:    
            run_block(body, env)    
        except BreakSignal:    
            break    
        except ContinueSignal:    
            continue    
    
    return i    
    
    
# ============================================================    
#   FOR (har / qadamda)    
# ============================================================    
    
def exec_for(lines, start, env):    
    """    
    har <o'zgaruvchi> <ro'yxat_expr> da    
        ...    
    tugat_har    
    
    qadamda <o'zgaruvchi> <boshlanish> <tugash> <qadam(ixtiyoriy)>    
        ...    
    tugat_har    
    """    
    header = lines[start].strip()    
    body = []    
    i = start + 1    
    while i < len(lines):    
        if lines[i].strip() == "tugat_har":    
            i += 1    
            break    
        body.append(lines[i])    
        i += 1    
    
    if header.startswith("qadamda"):    
        # qadamda i 0 10 2    
        parts = header.split()    
        var = parts[1]    
        bosh = int(eval_expr(parts[2], env))    
        tug = int(eval_expr(parts[3], env))    
        qadam = int(eval_expr(parts[4], env)) if len(parts) > 4 else 1    
        iterable = range(bosh, tug, qadam)    
    else:    
        # har x [1,2,3] da  yoki  har x royhat da    
        parts = header.split()    
        var = parts[1]    
        expr = " ".join(parts[2:-1])  # oxirgi "da" ni tashlab    
        iterable = eval_expr(expr, env)    
    
    for val in iterable:    
        env[var] = val    
        try:    
            run_block(body, env)    
        except BreakSignal:    
            break    
        except ContinueSignal:    
            continue    
    
    return i    
    
    
# ============================================================    
#   FUNKTSIYA (def)    
# ============================================================    
    
def exec_def(lines, start, env):    
    """    
    funktsiya salomlash(ism, yosh)    
        chiqar ism    
    tugat_funktsiya    
    """    
    header = lines[start].strip()    
    match = re.match(r"funktsiya\s+(\w+)(.*?)", header)    
    if not match:    
        return start + 1    
    
    fname = match.group(1)    
    params = [p.strip() for p in match.group(2).split(",") if p.strip()]    
    
    body = []    
    i = start + 1    
    while i < len(lines):    
        if lines[i].strip() == "tugat_funktsiya":    
            i += 1    
            break    
        body.append(lines[i])    
        i += 1    
    
    def func(*args):    
        local_env = dict(env)    
        for p, a in zip(params, args):    
            local_env[p] = a    
        try:    
            run_block(body, local_env)    
        except ReturnSignal as r:    
            return r.value    
        return None    
    
    env[fname] = func    
    return i    
    
    
# ============================================================    
#   SINF (class)    
# ============================================================    
    
def exec_class(lines, start, env):    
    """    
    sinf Mashina    
        funktsiya yangi(ism)    
            o'z.ism = ism    
        tugat_funktsiya    
    tugat_sinf    
    """    
    header = lines[start].strip()    
    parts = header.split()    
    cname = parts[1]    
    parent_name = parts[3] if len(parts) > 3 and parts[2] == "meros" else None    
    
    body_lines = []    
    i = start + 1    
    while i < len(lines):    
        if lines[i].strip() == "tugat_sinf":    
            i += 1    
            break    
        body_lines.append(lines[i])    
        i += 1    
    
    class_env = {}    
    run_block(body_lines, class_env)    
    
    parent = env.get(parent_name, object) if parent_name else object    
    attrs = {k: v for k, v in class_env.items() if callable(v)}    
    NewClass = type(cname, (parent,), attrs)    
    env[cname] = NewClass    
    return i    
    
    
# ============================================================    
#   TRY / EXCEPT / FINALLY (usla / tut / nihoyat)    
# ============================================================    
    
def exec_try(lines, start, env):    
    """    
    usla    
        ...    
    tut    
        ...    
    nihoyat    
        ...    
    tugat_usla    
    """    
    try_body = []    
    except_body = []    
    finally_body = []    
    section = "try"    
    i = start + 1    
    
    while i < len(lines):    
        stripped = lines[i].strip()    
        if stripped == "tut":    
            section = "except"    
        elif stripped == "nihoyat":    
            section = "finally"    
        elif stripped == "tugat_usla":    
            i += 1    
            break    
        else:    
            if section == "try":    
                try_body.append(lines[i])    
            elif section == "except":    
                except_body.append(lines[i])    
            else:    
                finally_body.append(lines[i])    
        i += 1    
    
    try:    
        run_block(try_body, env)    
    except (RuntimeError, Exception) as e:    
        env["__xato"] = str(e)    
        run_block(except_body, env)    
    finally:    
        run_block(finally_body, env)    
    
    return i    
    
    
# ============================================================    
#   O'ZGARUVCHI TAYINLASH    
# ============================================================    
    
def exec_assign(line, i, env):    
    # Qo'shish bilan tayinlash: x += 5    
    for op in ["+=", "-=", "*=", "/="]:    
        if op in line:    
            var, val_str = line.split(op, 1)    
            var = var.strip()    
            val = eval_expr(val_str.strip(), env)    
            ops = {    
                "+=": lambda a, b: a + b,    
                "-=": lambda a, b: a - b,    
                "*=": lambda a, b: a * b,    
                "/=": lambda a, b: a / b,    
            }    
            env[var] = ops[op](env.get(var, 0), val)    
            return i + 1    
    
    # Oddiy: x = ifoda    
    var, val_str = line.split("=", 1)    
    env[var.strip()] = eval_expr(val_str.strip(), env)    
    return i + 1    
    
    
# ============================================================    
#   IFODA HISOBLASH    
# ============================================================    
    
def eval_expr(expr, env):    
    expr = expr.strip()    
    
    # O'zbekcha haqiqat/yolg'on/bo'sh    
    replacements = {    
        "haqiqat": "True",    
        "yolg'on": "False",    
        "bo'sh":   "None",    
        " va ":    " and ",    
        " yoki ":  " or ",    
        " emas ":  " not ",    
    }    
    for uz, py in replacements.items():    
        expr = expr.replace(uz, py)    
    
    try:    
        return eval(expr, {"__builtins__": __builtins__}, env)    
    except Exception as e:    
        raise RuntimeError(f"Ifoda xatosi '{expr}': {e}")    
    
    
# ============================================================    
#   BLOK IJROSI    
# ============================================================    
    
def run_block(body_lines, env):    
    i = 0    
    while i < len(body_lines):    
        i = execute(body_lines, i, env)    
    
    
# ============================================================    
#   SIGNAL CLASSLARI    
# ============================================================    
    
class BreakSignal(Exception):    
    pass    
    
class ContinueSignal(Exception):    
    pass    
    
class ReturnSignal(Exception):    
    def __init__(self, value):    
        self.value = value    
    
    
# ============================================================    
#   TEST — DEMO DASTUR    
# ============================================================    
    
DEMO = """\    
boshlash    
    
# O'zgaruvchilar    
son = 5    
matn = "Salom Dunyo"    
ro'yxat = [1, 2, 3, 4, 5]    
    
# chiqar    
chiqar matn    
chiqar son    
    
# agar / aks_holda / bo'lmasa    
agar son > 3 bo'lsa    
    chiqar "son 3 dan katta"    
aks_holda son == 3 bo'lsa    
    chiqar "son 3 ga teng"    
bo'lmasa    
    chiqar "son 3 dan kichik"    
tugat_agar    
    
# takror (while)    
hisoblagich = 0    
takror hisoblagich < 3 bo'lguncha    
    chiqar hisoblagich    
    hisoblagich += 1    
tugat_takror    
    
# har (for)    
har x ro'yxat da    
    chiqar x    
tugat_har    
    
# qadamda (range for)    
qadamda i 0 5 2    
    chiqar i    
tugat_har    
    
# funktsiya    
funktsiya qo'sh(a, b)    
    natija = a + b    
    qaytar natija    
tugat_funktsiya    
    
javob = qo'sh(10, 20)    
chiqar javob    
    
# tekshir (assert)    
tekshir son > 0    
    
# usla / tut / nihoyat    
usla    
    xato "Sinov xatosi"    
tut    
    chiqar "Xato ushlandi!"    
nihoyat    
    chiqar "Nihoyat bloki ishladi"    
tugat_usla    
    
# o'chir (del)    
vaqtinchalik = 99    
o'chir vaqtinchalik    
    
# yozuvchi (yield-like)    
yozuvchi 10    
yozuvchi 20    
yozuvchi 30    
chiqar __generator_list    
    
tugat    
"""    
    
if __name__ == "__main__":    
    import tempfile, os    
    with tempfile.NamedTemporaryFile("w", suffix=".uz", delete=False,    
                                     encoding="utf-8") as tmp:    
        tmp.write(DEMO)    
        tmp_path = tmp.name    
    
    try:    
        run_file(tmp_path)    
    finally:    
        os.unlink(tmp_path)    
