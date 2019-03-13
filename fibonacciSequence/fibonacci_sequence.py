# coding=utf-8

'''
斐波那契数列:
F = 0                            -->  n = 0
F = 1                            -->  n = 1
F(n) = F(n-1) + F(n-2)           -->  n >= 2                 
'''

#问题应用https://github.com/taizilongxu/interview_python#1-selectpoll%E5%92%8Cepoll

class Fibonacci(object):
    def fibonacci_recursion_tool(self, n):
        '''递归实现'''
        if n <= 0:
            return 0
        elif n == 1:
            return 1
        else:
            return self.fibonacci_recursion_tool(n-1) + self.fibonacci_recursion_tool(n-2)

    def fibonacci_recursion(self, n):
        res = []
        for i in range(1, n+1):
            res.append(self.fibonacci_recursion_tool(i))
        print(res)
        return res

    def fibonacci_loop_tool(self, n):
        '''循环实现'''
        a, b = 0, 1
        while n > 0:
            a, b = b, a+b
            n -= 1

    def fibonacci_loop(self, n):
        res = []
        a, b = 0, 1
        while n > 0:
            res.append(b)
            a, b = b, a+b
            n -= 1
        print(res)
        return res

    def fibonacci_yield_tool(self, n):
        '''通过关键字yield优化循环实现'''
        a, b = 0, 1
        while n > 0:
            yield b
            a, b = b, a+b
            n -= 1

    def fibonacci_yield(self, n):
        return list(self.fibonacci_yield_tool(n))

if __name__ == "__main__":
    f = Fibonacci()
    f.fibonacci_recursion(10)
    f.fibonacci_loop(12)
    y = f.fibonacci_yield(15)
    print(y)
