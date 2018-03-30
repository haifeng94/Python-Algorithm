# coding=utf-8

def bubbleSort(nums):
	"""冒泡排序"""
	for i in range(len(nums)-1):
		for j in range(0, len(nums)-1-i):
			if nums[j] > nums[j+1]:
				nums[j],nums[j+1] = nums[j+1],nums[j]
			
	return nums

if __name__ == "__main__":
	li = [23,56,12,99,34,78,23,13,47]
	print(li)
	print(bubbleSort(li))

