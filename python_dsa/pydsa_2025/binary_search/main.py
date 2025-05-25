def binary_search(nums, targ):
	low = 0
	high = len(nums)
	
	while low < high:
		mid = int(len(low + high)//2)
		if targ == nums[mid]:
			return mid
		elif targ < nums[mid]:
			high = mid - 1
		else:
			low = mid + 1
			
	return -1
	
	
	if "__name__" == "__main__":
		pass
		
