# coding:utf-8

def quickSort(nums,first,end):
	"""快速排序"""
	if first >= end: 
		return
	
	mid_value = nums[first]
	left_pointer = first
	right_pointer = end

	while left_pointer < right_pointer:
		#right_pointer 左移
		while left_pointer < right_pointer and nums[right_pointer] >= mid_value:
			right_pointer -= 1

		nums[left_pointer] = nums[right_pointer]

		while left_pointer < right_pointer and nums[left_pointer] < mid_value:
			left_pointer += 1
		nums[right_pointer] = nums[left_pointer]

	#从循环退出时，left_pointer等于right_pointer
	nums[left_pointer] = mid_value

	#对mid_value左边的列表递归
	quickSort(nums,first,left_pointer-1)
	#对mid_value右边的列表递归
	quickSort(nums,left_pointer+1,end) 

if __name__ == "__main__":
	nums = [45,12,89,33,39,84,26,78,43]
	print(nums)
	quickSort(nums,0,len(nums)-1)
	print(nums)
