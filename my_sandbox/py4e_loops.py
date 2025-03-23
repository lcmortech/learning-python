#PY4E
def lg_val(nums):
	s_nums = sorted(nums)
	print(s_nums[-1])
	
def find_lg(nums):
	max_num = 0 # Dr.Chuck starts at -1
	
	for num in nums:
		if num > max_num:
			max_num = num
	
	print(max_num) 
	
lg_val([6,2,7,8,4,5])
lg_val([3,41,12,9,74,15])
find_lg([6,2,7,8,4,5])
find_lg([3,41,12,9,74,15])

# LOOP IDIOMS
# Counting in a Loop
counter = 0

for _ in [5,9,1,8,4,6,7]:
	counter += 1
	
print(counter)

# Summing in a Loop
total = 0
nums_list = [6,3,8,6,9,6]

for i in range(len(nums_list)):
	total = total + nums_list[i]
	
print(total)

c_total = 0
for i in [9, 41, 12, 3, 74, 15]:
	c_total = c_total + i
	
print(c_total)

	
# Avg in a Loop	
def find_avg(nums):
	nums_count = len(nums)
	num_sum = 0
	

	for num in nums: # get each value
		num_sum = num_sum + num
		print(num_sum)
		print(nums_count)
		avg_num = num_sum / nums_count
		
	print(avg_num)
	
find_avg([5,2,3,4])

count = 0
sum = 0
for num in [9, 41, 12, 3, 74, 15]:
	count += 1
	sum = sum + num
	avg = sum // count
	
print(avg)


def fizzbuzz(nums):
	
	for num in nums:
		match num % 2:
			case 0:
				print("fizz")
			case 1:
				print("buzz")
			case _:
				print("neither")
				
	print(num)
	
fizzbuzz([6,2,9,"fan"])
	
		
		
		

	
	
