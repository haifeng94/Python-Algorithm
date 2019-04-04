#coding = utf -8

'''
题目：把只包含因子2、3和5的数称作丑数（Ugly Number）。例如6、8都是丑数，但14不是，因为它包含因子7。
习惯上我们把1当做是第一个丑数。求按从小到大的顺序的第N个丑数。
'''

'''
res用来存放排好序的丑数。每一个丑数 n 都是从小于 n 的丑数 乘以 2，3，5 中得来的。
所以每次只需要考虑 <= n的丑数中，没有加入res的值，例如为(n-1)*5，那么只需要比较(n-1)*5，n*2，n*3的值，取最小存入res
'''

class Solution:
    def GetUglyNumber_Solution1(self, index):
        if index <= 0:
            return 0
        index2, index3, index5 = 0, 0, 0
        res = [1]
        while len(res) < index:
            temp = min(res[index2]*2, res[index3]*3, res[index5]*5)
            if not temp in res:
                res.append(temp)
            if temp % 2 == 0:
                index2 += 1
            if temp % 3 == 0:
                index3 += 1
            if temp % 5 == 0:
                index5 += 1
        return res[index - 1]

s = Solution()
res = s.GetUglyNumber_Solution1(20)
print(res)