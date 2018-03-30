# coding:utf-8

def shellSort(nums):
	"""希尔排序"""
	s = len(nums)
	step = s//2 #python3得到整数n//2,python2为n/2
	
	while step >= 1:
		#与普通的插入算法的区别就是step步长不同
		for i in range(step,s):
			j = i
			while j > 0:
				if nums[j] < nums[j-step]:
					nums[j],nums[j-step] = nums[j-step],nums[j]
					j -= step
				else:
					break
		#缩短step步长
		step //= 2

if __name__ == "__main__":
	nums = [45,12,89,33,39,84,26,78,43]
	print(nums)
	shellSort(nums)
	print(nums)