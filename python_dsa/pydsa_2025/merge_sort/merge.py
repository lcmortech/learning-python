def merge_sort(nums):
	if len(nums) < 1:
		return nums
	
	mid = int(len(nums)//2)
	first_half = nums[:mid]
	second_half = nums[mid:]
	
	nums_a = merge_sort(first_half)
	nums_b = merge_sort(second_half)
	
	return merged(nums_a, nums_b)
	
	def merged(nums1, nums2):
		i = j = 0
		merged_list = []
		
		while i < len(nums1) and j < len(nums2):
			
			if i < nums1[i] and j < nums2[j]:
				merged_list.append(nums1[i])
				i += 1
			else:
				merged_list.append(nums2[j])
				j += 1
				
			while i < len(nums1):
				merged_list.append(nums1[i])
				i += 1
			while j < len(nums2):
				merged_list.append(nums[j])
				j += 1
				
			return merged_list
				
		
				
	
