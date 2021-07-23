# this is iterative solution

# time O(N)
# space O(1)

def ntfib(n):
    lastTwo = [0, 1]
    counter = 3
    while counter <= n:
        nextfib = lastTwo[0] + lastTwo[1]
        lastTwo[0] = lastTwo[1]
        lastTwo[1] = nextfib
        counter += 1
    if n > 1:
        return lastTwo[1]
    else:
        lastTwo[0]


print(ntfib(50))
