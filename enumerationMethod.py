# 如果 a+b+c = 2000,且a^2+b^2=c^2(a,b,c为自然数)，如何求出a、b、c所有可能的组合

import time

#枚举法之方法一:时间复杂度为O(n^3)
def method1():
	startTime = time.time()
	for a in range(2001):
		for b in range(2001):
			for c in range(2001):
				if a+b+c == 2000 and a**2 + b**2 == c**2:
					print('a,b,c=%d,%d,%d'%(a,b,c))

	endTime = time.time()
	print("time=%d"%(endTime-startTime))
	print("ok")

#枚举法之方法二:时间复杂度为O(n^2)
def method2():
	startTime = time.time()
	for a in range(2001):
		for b in range(2001):
			c = 2000-a-b
			if a**2 + b**2 == c**2:
				print('a,b,c=%d,%d,%d'%(a,b,c))
	
	endTime = time.time()
	print("time=%d"%(endTime-startTime))
	print("ok")

s1=method1()
s2=method2()
