# coding=utf-8

'''
题目：输入一个矩阵，按照从外向里以顺时针的顺序依次打印出每一个数字。例如：如果输入如下矩阵：

    1     2     3     4
    5     6     7     8
    9    10    11    12
   13    14    15    16
   则依次打印出数字1、2、3、4、8、12、16、15、14、13、9、5、6、7、11、10。
'''

'''
思路超神：
可以模拟魔方逆时针旋转的方法，一直做取出第一行的操作
例如
1 2 3
4 5 6
7 8 9
输出并删除第一行后，再进行一次逆时针旋转，就变成：
6 9
5 8
4 7
继续重复上述操作即可
'''

class Solution:
    def printMatrix(self, matrix):
        ret = []
        while matrix:
            ret += matrix.pop(0)
            if not matrix:
                break
            matrix = self.turn(matrix)
        return ret

    def turn(self, matrix):
        newMat = []
        row = len(matrix)
        col = len(matrix[0])
        for i in range(col):
            subMat = []
            for j in range(row):
                subMat.append(matrix[j][i])
            newMat.insert(0,subMat)

        return newMat

s = Solution()
res = s.printMatrix([[1,2,3],[4,5,6],[7,8,9]])
print(res)