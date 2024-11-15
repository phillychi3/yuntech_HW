def countWays(n, path=[]):
    if n == 0:
        print(path)
        return 1
    ways = 0
    if n >= 1:
        ways += countWays(n-1, path + [1])
    if n >= 2:
        ways += countWays(n-2, path + [2])
    return ways

n = 4
total_ways = countWays(n)
print("Total:", total_ways)