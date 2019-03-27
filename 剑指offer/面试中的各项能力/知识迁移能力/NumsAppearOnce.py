# coding=utf-8

'''
题目：一个整型数组里除了两个数字之外，其他的数字都出现了两次。请写程序找出这两个只出现一次的数字。
'''

#思路一：利用python自带的counter库
class Solution:
    def FindNumsAppearOnce(self, array):
        from collections import Counter
        mc = Counter(array).most_common()        #[(1, 2), (2, 2), (3, 2), (4, 1), (5, 1)]
        return list(map(lambda c:c[0], mc[-2:]))      #[4,5]

s = Solution()
res = s.FindNumsAppearOnce([1,2,3,4,1,2,3,5])
print(res)


#思路二：异或运算  按位异或，在得到的值中找到二进制最后一个1，然后把数组按照该位是0还是1分为两组
def get_only_one_number(nums):
    if not nums:
        return None
    tmp_ret = 0
    for n in nums:  # 获取两个值的异或结果
        tmp_ret ^= n
    last_one = get_bin(tmp_ret)
    a_ret, b_ret = 0, 0
    for n in nums:
        if is_one(n, last_one):
            a_ret ^= n
        else:
            b_ret ^= n
    return [a_ret, b_ret]


def get_bin(num):  # 得到第一个1
    ret = 0
    while num & 1 == 0 and ret < 32:
        num = num >> 1
        ret += 1
    return ret


def is_one(num, t):  # 验证t位是不是1
    num = num >> t
    return num & 0x01