# coding:utf-8

def mergeSort(nums):
	"""归并排序"""
	if len(nums) <= 1:
		return nums

	mid = len(nums)//2

	#left
	left_nums = mergeSort(nums[:mid])
	#right
	right_nums = mergeSort(nums[mid:])
	print(left_nums)
	print(right_nums)

	left_pointer,right_pointer = 0,0
	result = []

	while left_pointer < len(left_nums) and right_pointer < len(right_nums):
		if left_nums[left_pointer] <= right_nums[right_pointer]:
			result.append(left_nums[left_pointer])
			left_pointer += 1
		else:
			result.append(right_nums[right_pointer])
			right_pointer += 1

	result += left_nums[left_pointer:]
	result += right_nums[right_pointer:]
	return result

if __name__ == "__main__":
	li = [45,12,89,33,39,84,26,78,43]
	print(li)
	sorted_nums = mergeSort(li)
	print(sorted_nums)