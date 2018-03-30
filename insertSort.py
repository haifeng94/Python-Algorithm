# coding:utf-8

def insertSort(nums):
	"""插入排序"""
	for i in range(1, len(nums)):
		j = i
		while j>0:
			if nums[j] < nums[j-1]:
				nums[j], nums[j-1] = nums[j-1], nums[j]
				j -= 1
			else:
				break

if __name__ == "__main__":
	li = [45,12,89,33,39,84,26,78,43]
	print(li)
	insertSort(li)
	print(li)
