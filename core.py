def run_file(path):
    with open(path, "r", encoding="utf-8") as f:
        for line in f:
            line = line.strip()

            if not line:
                continue

            if line.startswith("boshlash"):
                print("🚀 START")

            elif line.startswith("chiqar"):
                print(line.replace("chiqar", "").strip().strip('"'))

            elif line.startswith("agar"):
                print("IF:", line)

            elif line.startswith("bo‘lsa"):
                print("ELSE:", line)

            else:
                print("UNKNOWN:", line)
