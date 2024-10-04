ascii_base = 65
null = "- "

def get_ascii( base, count) -> str:
    print(base, count)
    return " ".join(chr(base + i) for i in range(count)) + " "

for i in range(1, 11):
    print(null * (10 - i) + get_ascii(ascii_base, i))
    ascii_base += i

