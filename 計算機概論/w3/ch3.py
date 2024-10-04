epsilon = 0.01
num_guesses, low = 0.0, 0.0
x = int(input("some number: "))
if x <= 0:
    print("error message")
    exit()
high = max(1, x)
ans = (high + low) / 2
while abs(ans**2 - x) >= epsilon:
    print("low", low, "high", high, "ans = ", ans)
    num_guesses += 1
    if ans**2 < x:
        low = ans
    else:
        high = ans
    ans = (high + low) / 2
print("number of guesses =", num_guesses)
print(ans, "is close to square root of", x)
