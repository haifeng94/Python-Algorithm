# coding=utf-8

'''
题目：输入一个字符串,按字典序打印出该字符串中字符的所有排列。
例如输入字符串abc,则打印出由字符a,b,c所能排列出来的所有字符串abc,acb,bac,bca,cab和cba。
'''

'''
思路：依次取一个元素，然后依次和之前递归形成的所有子串组合，形成新的字符串。
'''

def my_permutation(s):
    str_set = []
    ret = []

    def permutation(string):
        print('string; ',string)
        for i in string:
            str_tem = string.replace(i, '')
            str_set.append(i)
            if len(str_tem) > 0:
                permutation(str_tem)
            else:
                ret.append(''.join(str_set))
            str_set.pop()

    permutation(s)
    return ret