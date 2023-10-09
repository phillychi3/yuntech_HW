import sys
str = sys.stdin.readlines()
str = [s.strip('\n') for s in str]
data = str[0].replace('-', '')

def luhn(card_no):
    digits = [int(x) for x in reversed(card_no)]
    even_digits = [d * 2 for d in digits[1::2]]
    even_digits = [d // 10 + d % 10 for d in even_digits]
    even_sum = sum(even_digits)
    odd_sum = sum(digits[::2])
    if (odd_sum + even_sum) % 10 == 0:
        return True
    else:
        return False

dd = luhn(data)
if dd:
    if data[0] == '4':
        print('VISA')
    elif data[0] == '5':
        print('MASTER_CARD ')
    
else:
    print('INVALID')
