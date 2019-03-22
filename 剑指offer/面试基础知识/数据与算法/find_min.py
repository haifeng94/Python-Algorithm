#coding = utf-8
'''
题目：把递增数组的前面部分数字移到队尾，求数组中的最小值，例如[3,4,5,6,1,2]
思路：使用二分法，但要考虑[1, 0, 0, 1]这种数据，只能顺序查找
'''

def find_min(nums):
    length = len(nums)
    if length == 0:
        return 0
    left, right = 0, length-1
    while nums[left] >= nums[right]:
        if right - left == 1:
            return nums[right]
        mid = (left + right) // 2
        if nums[left] == nums[mid] == nums[right]:
            return min(nums)
        if nums[left] <= nums[mid]:
            left = mid
        if nums[right] >= nums[mid]:
            right = mid
    return nums[0]

nums = [1,0,1,1,1,1,1]
res = find_min(nums)
print(res)