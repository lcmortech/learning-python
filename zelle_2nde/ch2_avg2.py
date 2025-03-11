# Find the average of 3 exam scores
import math
# Method 1 (hardcoded)
def avg_score():
	score1 = int(input("Please enter the first score: \n"))
	score2 = int(input("Please enter the second score: \n"))
	score3 = int(input("Please enter the third score: \n"))
	
	avg = math.ceil((score1 + score2 + score3)/3)
	print(f"Your average score is {avg}")
	
#avg_score()

# Method 2 (Variable Scores)
def avg_scores():
	score_input = int(input("Please enter the amount of scores: "))
	
	for score in range(score_input):
		score_sum = 0
		score_sum += score
		result = score_sum / score_input
		
	print(result)

#avg_scores()
