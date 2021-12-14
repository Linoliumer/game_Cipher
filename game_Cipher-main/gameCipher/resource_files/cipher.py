def likePhono(x): #Перевод слова в код по словорю.
	new_word = ''
	list_like_phono={
		'A':'00000','B':'00001','C':'00010','D':'00011',
		'E':'00100','F':'00101','G':'00110','H':'00111',
		'I':'01000','J':'01001','K':'01010','L':'01011',
		'M':'01100','N':'01101','O':'01110','P':'01111',
		'Q':'10000','R':'10001','S':'10010','T':'10011',
		'U':'1010','V':'1011','W':'1100','X':'1101',
		'Y':'1110','Z':'1111',
	}
	for i in x:
		new_word += list_like_phono[i]
	new_word = int(new_word)
	return new_word


def ceasarCipher(word, values): #Зашифровка слова по шифру Цезаря.
	eng_alph = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
	word = word.upper()
	len_alpha = len(eng_alph)
	new_word = ''
	for i in range(len(word)):
		index = eng_alph.index(word[i])
		index_FC = index + values
		if index_FC > (len_alpha - 1):
			step = index_FC // (len_alpha-1)
			if index_FC / (len_alpha-1) == 0:
				step -= 1
			index_FC = index_FC - (len_alpha - 1) * step
		new_word += eng_alph[index_FC]
	return new_word