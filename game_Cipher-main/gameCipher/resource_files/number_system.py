def xForTen(num, x1 = 2): #Перевод из двоичной СС в десятитичную.
	number = num
	step = 0
	sum_elem =0
	len_num = len(str(number)) - 1
	while step <= len_num:
		elem = number % 10
		oper = elem * (x1 ** step)
		sum_elem += oper
		step += 1
		elem1 = number // 10
		number = elem1
	return sum_elem


def tenForY(num, x2 = 2): #Перевод из десятичной СС в двоичную СС.
	a = num
	b = 0
	sum_elem = 0
	while a >= x2:
		elem = a % x2	
		elem1 = elem * (10 ** b)
		sum_elem += elem1
		b += 1
		a = a // x2
	elem3 = a * (10 ** b)
	sum_elem += elem3
	return str(sum_elem)

def binaryFloat(n): #Перевод вещественной части числа в двоичную СС.
	number = n / 100  
	step = 7
	binary_number_array = ''
	num_float = number % 1
	while num_float != 0 and step != 0:
		num_int = number // 1
		num_int = int(num_int)
		binary_number_array += str(num_int)
		num_float = number % 1
		num_float = round(num_float, 2)
		number = num_float * 2
		step -= 1
	new_word_bin = binary_number_array[1:]
	return new_word_bin


def numberToFibanachi(number): #Перевод числа в Фибоначчиеву СС.
	numberFibanachi = [55,34,21,13,8,5,3,2,1]
	numForFib = number
	fibNumber = ''
	for i in numberFibanachi:
		if i <= numForFib:
			numForFib -= i
			fibNumber += '1'
		else:
			fibNumber += '0'
	return fibNumber