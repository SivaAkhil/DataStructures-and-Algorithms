# Solution 2
# O(n) time
# O(n) space

def twoNumberSum(array, targetSum):
    nums = {}
    for num in array:
        potentialMatch = targetSum - num
        if potentialMatch in nums:
            return [targetSum - num, num]
        else:
            nums[num] = True
    return []



ar = [3, 5, -4, 8, 11, 1, -1, 6]


print(twoNumberSum(ar, 10))
