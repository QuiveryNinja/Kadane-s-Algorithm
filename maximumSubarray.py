#Kadane's Algorithm
nums=[-1,3,2,-1]
def maxSubArray(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    max_current = max_global = nums[0]
    for i in range(1, len(nums)-1):
        max_current=max(nums[i], max_current+nums[i])
    if max_current > max_global:
        max_global = max_current
    return max_global