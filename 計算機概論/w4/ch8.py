def find_last(s, sub):
    last = -1
    while True:
        next = s.find(sub, last + 1)
        if next == -1:
            return last
        last = next

print(find_last('asdfagg', 'a'))