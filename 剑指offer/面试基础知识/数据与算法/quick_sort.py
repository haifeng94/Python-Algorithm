#coding = utf-8

'''
快速排序
'''

class Solution:
    def quick_sort(self, list):
        if len(list) < 2:
            return list
        else:
            mid = list[0]
            lessmid = [i for i in list[1:] if i <= mid]
            biggermid = [j for j in list[1:] if j > mid]
            finalylist = self.quick_sort(lessmid) + [mid] + self.quick_sort(biggermid)
            return finalylist

print(Solution().quick_sort([2,4,6,7,1,2,5]))