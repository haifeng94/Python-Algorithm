# coding=utf-8

'''
题目：统计一个数字在排序数组中出现的次数。
'''

'''
思路一：count函数是顺序查找，最坏时间复杂度是O(n)
'''

class Solution:
    def GetNumberOfK(self, data, k):
        return data.count(k)

'''
思路二：看见有序就要想起使用二分法查找,最坏时间复杂度是O(logn)
对于一个有序数组，要考虑 1,2,2,2,3,4这种情况，计算k=2在数组中出现的次数，用二分法去找这个数，一个找最前面
出现的2的下标，一个找最后面2出现的小标，这样前后相减+1即可的到结果。
'''

class Solution2:
    def GetNumberOfK(self, nums, k):
        if not data:
            return 0
        first = self.get_first_k(nums, k)
        last = self.get_last_k(nums, k)
        if first < 0 and last < 0:
            return 0
        #if first < 0 or last < 0:
        #    return 1
        return last - first + 1

    def get_first_k(self, nums, k):
        left, right = 0, len(nums) - 1
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] < k:
                if mid + 1 < len(nums) and nums[mid+1]==k:
                    return mid + 1
                left = mid + 1
            elif nums[mid] == k:
                if mid - 1 < 0 or (mid - 1 >= 0 and nums[mid-1] < k):
                    return mid
                right = mid - 1
            else:
                right = mid - 1

        return -1

    def get_last_k(self, nums, k):
        left, right = 0, len(nums) - 1
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] < k:
                left = mid + 1
            elif nums[mid] == k:
                if mid + 1 == len(nums) or (mid + 1 < len(nums) and nums[mid+1] > k):
                    return mid
                left = mid + 1
            else:
                if mid - 1 >= 0 and nums[mid-1] == k:
                    return mid - 1
                right = mid - 1

        return -1

s = Solution2()
data = [1,2,3,4,5,7]
k = 1
res = s.GetNumberOfK(data, k)
print(res)