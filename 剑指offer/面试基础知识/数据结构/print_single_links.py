#coding=utf-8

'''
题目：从尾到头打印单链表
'''

#方法一：使用栈,可以使用列表模拟
def print_links(links):
    stack = []
    while links:
        stack.append(links.val)
        links = links.next
    while stack:
        print(stack.pop())

#方法2: 直接递归
def print_link_recursion(links):
    if links:
        print(print_link_recursion(links.next))
        print(links.val)
