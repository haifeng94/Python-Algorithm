# coding=utf-8

class Solution:
    def maxNumber(self, nums1, nums2, k):
        for i in range(k+1):
            if i <= len(nums1) and k-i <= len(nums2): #nums1从小到大遍历，nums2从大到小遍历
                p1 = self.prep(nums1, i)
                p2 = self.prep(nums2, k-i)
                self.merge(p1, p2)

    def prep(self, nums, k): #获取一共含有k个数的两个新列表
        drop = len(nums) - k
        out = []
        for num in nums:
            while drop and out and out[-1] < num:
                out.pop() #pop()函数用于移除列表中的一个元素（默认最后一个元素），并且返回该元素的值
                drop -= 1
            out.append(num)
            #print(out)
        #print(out)
        print(out[:k])
        return out[:k]

    def merge(self, a, b): #根据得到的a,b新列表按照题目规则排列成新列表
        r = [max(a, b).pop(0) for _ in a+b] #a->list, b->list, max(a,b) equals to max(a[0], b[0])
        print('r====', r)

if __name__ == "__main__":
    nums1 = [3, 4, 6, 5]
    nums2 = [9, 1, 2, 5, 8, 3]
    #nums1 = [3,4]
    #nums2 = [5,2,6]
    k = 5
    s = Solution()
    s.maxNumber(nums1,nums2,k)

    for _ in nums1+nums2:
        print(max(nums1, nums2))
        print(max(nums1, nums2).pop(0))