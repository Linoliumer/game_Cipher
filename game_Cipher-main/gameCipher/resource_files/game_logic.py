from resource_files.number_system import *
from resource_files.text import *
from resource_files.cipher import *


# Generating responses
def creatingResponses(hours, minutes, day, month):
	lanswers = [] 
	word_for_encryption = 'HELP' # The base word for the cipher (Modify)
	
	# Step 1 / Concatenation of two numbers in Fibonacci SS
	concate_fib_num = numberToFibanachi(hours) + numberToFibanachi(minutes)
	# Counting units in concate_fib_num
	sum_of_units = 0
	for i in concate_fib_num: 
		sum_of_units += int(i)
	
	# Step 2 / Calling the "Caesar Cipher" function for word with step sum_of_units
	word_caesar = ceasarCipher(word_for_encryption, sum_of_units)
	
	''' 
	Step 3 / Chill to binary SS.
	Converting the month to double SS as a 
	fractional part of a number,
	concatenate the two numbers obtained.
	'''
	concate_num = tenForY(day,2) + binaryFloat(month)
	
	# Step 4 / Translation of the encrypted word into like a.k.a phono
	like_phono_out = likePhono(word_caesar)
	
	# Step 5 and 6 / Subtracting concate_num from like_phono_out 
	concate_num_ten = xForTen(int(concate_num)); 
	like_phono_out_ten = xForTen(like_phono_out);
	ans_step_five1 = like_phono_out_ten - concate_num_ten
	ans_step_five2 = int(tenForY(ans_step_five1, 2))
	'''
	 If the code contains less than eight characters,
	we attribute zeros at the end, while the length
	the final code will not equal 8
	'''
	sum_out = str(ans_step_five1)
	size_sum_out = len(sum_out)
	while size_sum_out < 8:
		size_sum_out += 1
		sum_out += '0'

	# Writing the answers to the answers array
	lanswers.append(str(sum_of_units))
	lanswers.append(word_caesar)
	lanswers.append(str(concate_num))
	lanswers.append(str(like_phono_out))
	lanswers.append(str(ans_step_five2))
	lanswers.append(str(sum_out))
	
	return lanswers