# coding:utf-8

def binarySearch(clist,item):
	"""二分查找--非递归"""
	s = len(clist)
	first = 0
	end = s-1
	while first <= end:
		mid = (first+end)//2 #python2为s/2
		if clist[mid] == item:
			return True
		elif item < clist[mid]:
			end = mid - 1
		else:
			first = mid + 1
	return False

def binarySearch2(clist,item):
	"""二分查找--递归法"""
	s = len(clist)
	if s > 0:
		mid = s//2 
		if clist[mid] == item:
			return True
		elif item < clist[mid]:
			return binarySearch2(clist[:mid],item)
		else:
			return binarySearch2(clist[mid+1:],item)
	return False

if __name__ == "__main__":
	li = [23,24,36,51,14,54,100,77,98]
	print(binarySearch(li,30))
	print(binarySearch(li,100))

	li = [23,24,36,51,14,54,100,77,98]
	print(binarySearch2(li,77))
	print(binarySearch2(li,50))
