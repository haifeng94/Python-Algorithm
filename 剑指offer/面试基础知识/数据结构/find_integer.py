#coding=utf-8
'''
题目：二维数组中，每行从左到右递增，每列从上到下递增，给出一个数，判断它是否在数组中
思路：从左下角或者右上角开始比较
'''

def find_integer(matrix, num):
    """
    param matrix: [[]]
    param num: int
    return: bool
    """
    
    if not matrix:
        return False
    rows, cols = len(matrix), len(matrix[0])
    row, col = rows-1, 0
    while row >= 0 and col <= cols-1:
        if matrix[row][col] == num:
            return True
        elif matrix[row][col] > num:
            row -= 1
        else:
            col += 1
    return False

if __name__ == "__main__":
    matrix = [
        [1,   4,  7, 11, 15],
        [2,   5,  8, 12, 19],
        [3,   6,  9, 16, 22],
        [10, 13, 14, 17, 24],
        [18, 21, 23, 26, 30]
    ]
    num = 666
    res = find_integer(matrix, num)
    print(res)
