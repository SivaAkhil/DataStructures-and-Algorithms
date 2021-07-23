#  time complexity O(2^N)
#  Space Complexicity O(N)

# this is very slow

def nthfib(n):
    memo = {}
    if n in memo:
        return n
    if n == 1:
        return 0
    if n == 2:
        return 1
    return nthfib(n - 1) + nthfib(n - 2)


print(nthfib(50))
