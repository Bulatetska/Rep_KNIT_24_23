a = "a14b6fh"

# Дізнатися, чи всі символи унікальні, використовуючи множини та списки?
# Використовуючи множину
print("Всі символи унікальні" if len(set(a)) == len(a) else "Є повторювані символи")

# Використовуючи список
unique_chars = []
for char in a:
    if char not in unique_chars:
        unique_chars.append(char)

print("Всі символи унікальні" if len(unique_chars) == len(a) else "Є повторювані символи")
