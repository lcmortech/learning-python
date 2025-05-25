def merge_sort(nums):
	if len(nums) < 1:
		return nums
		
	mid = int(len(nums)//2)
	first_half = nums[:mid]
	second_half = nums[mid:]
	
	nums_a = merge_sort(first_half)
	numms_b = merge_sort(second_half)
	
	return merge(nums_a, nums_b)
	
	def merge(sublist_1, sublist2)
		i = j = 0 #initiate both i and j pointers at 0
		
		merged_list = [] #where the merged list will go
		
		while i < len(sublist_1) and j < len(sublist_2):
			
			if sublist_1[i] < sublist_2[j]:
				merged_list.append(sublist_1[i])
				i += 1
			else:  
				merged_list.append(sublist_2[j])
				j += 1
			
			while i < len(sublist_1):
				merged_list.append(sublist_1[i])
				i += 1
				
			while j < sublist_2[j]:
				merged_list.append(sublist_2[j])
				j += 1
				
			return merged_list
