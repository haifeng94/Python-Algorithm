# coding=utf-8

'''
题目：有个游戏是这样的:首先,让小朋友们围成一个大圈。然后,他随机指定一个数m,让编号为0的小朋友开始报数。
每次喊到m-1的那个小朋友要出列唱首歌,然后可以在礼品箱中任意的挑选礼物,并且不再回到圈中,从他的下一个小朋友开始,
继续0...m-1报数....这样下去....直到剩下最后一个小朋友,可以不用表演,并且拿到牛客名贵的“名侦探柯南”典藏版(名额
有限哦!!^_^)。请你试着想下,哪个小朋友会得到这份礼品呢？(注：小朋友的编号是从0到n-1)
'''

'''
思路：约瑟夫环问题
     递推公式：f[i] = (f[i-1]+m)%i
     详细解释：http://blog.csdn.net/u012505432/article/details/51747181
'''

class Solution:
    def LastRemaining_Solution(self, n, m):
        if n < 1 or m < 1:
            return -1
        temp = 0
        for i in range(1, n+1):
            temp = (temp + m) % i

        return temp #从1开始编号的话，结果加1即可


s = Solution()
res = s.LastRemaining_Solution(4,3)
print(res)