# time O(N)
# Space O(N)

def nthfib(n, memoize={1: 0, 2: 1}):
    if n in memoize:
        return memoize[n]
    else:
        memoize[n] = nthfib(n-1, memoize) + nthfib(n-2, memoize)
        return memoize[n]


print(nthfib(50))
