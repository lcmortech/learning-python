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
				
		
		
#+++++++++++++++++++++++++++++++++++++++++++++++++

def merge_sort(list):
	if len(list) < 1:
		return list
		
	mid = int(len(list)//2)
	low = list[:mid]
	high = list[mid:]
	
	part_a = merge_sort(low)
	part_b = merge_sort(high)
	
	return merged(part_a, part_b)
				
				
	def merged(sublist_1, sublist_2):
		i = j = 0 #initiate both to zero
		
		merged_list = []
		
		while i < len(sublist_1) and j < len(sublist_2): #regular loop for both sublists
			
			if sublist_1[i] < sublist_2[j]:
				merged_list.append(sublist_1[i])
				i += 1
				
			else:
				merged_list.append(sublist_2[j])
				j += 1
				
		while i < len(sublist_1):
			merged_list.append(sublist_1[i])
			i += 1
			
		while j < len(sublist_2):
			merged_list.append(sublist_2[j])
			j += 1
			
		return merged_list
		
		
#+++++++++++++++++++++++++++++++++++++++++++++++++
# What do we need to input?
# for merge_sort() -> unsorted list
# for merged() -> the split sections
# What do we need to return?
# for merge_sort() -> merged(sec1, sec2)
# for merged() -> merged_list

def merge_sort(u_list):
	if len(u_list) < 2:
		return u_list
		
	midpoint = int(len(u_list)//2)
	low = u_list[:mid]
	high = u_list[mid:]
	
	sec1 = merge_sort(low)
	sec2 = merge_sort(high)
	
	return merged(sec1, sec2)
	
def merged(p1, p2):
	i = j = 0
	mergelist = []
	
	while i < len(p1) and j < len(p2):
		
			if p1[i] > p2[j]:
				mergelist.append(p1[i])
				i += 1
			else:
				mergelist.append(p2[j])
				j += 1
				
			while i < len(p1):
				mergelist.append(p1[i])
				i += 1
			
			while j < len(p2):
				mergelist.append(p2[j])
				
			return mergelist
			
#++++++++++++++++++++++++++++++++++++++++++++

def mergesort(u_list):
	if len(u_list) < 2:
		return u_list
		
	mid = int(len(u_list)//2)
	low = u_list[:mid]
	high = u_list[mid:]
	
	sec_1 = mergesort(low)
	sec_2 = mergesort(high)
	
	return mergelist(sec_1, sec_2)
	
	
def merge(part1, part2):
	i = j = 0
	
	merge_list = []
	
	while i < len(part1) and j < len(part2):
		
		if part1[i] < part2[j]:
			merge_list.append(part1[i])
			i += 1
		else:
			merge_list.append(part2[j])
			j += 1
			
			
	while i < len(part1):
		merge_list.append(part1[i])
		i += 1
		
	while j < len(part2):
		merge_list.append(part[j])
		j += 1
		
	return merge_list
			
				
					

			
