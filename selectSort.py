# coding:utf-8

def selectSort(nums):
	"""选择排序"""
	for i in range(len(nums)-1): 
		min_index = i
		for j in range(i+1,len(nums)):
			if nums[min_index] > nums[j]:
				min_index = j
		nums[i],nums[min_index] = nums[min_index],nums[i]

if __name__ == "__main__":
	li = [45,12,89,33,39,84,26,78,43]
	print(li)
	selectSort(li)
	print(li)
