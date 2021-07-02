import random
from tkinter import *
from PIL import ImageTk, Image


def xForTen(num, x1 = 2): #Перевод из двоичной СС в десятитичную.
	number = num
	step = 0
	sum_elem =0
	len_num = len(str(number)) - 1
	while step <= len_num:
		elem = number % 10
		oper = elem*(x1**step)
		sum_elem += oper
		step += 1
		elem1 = number // 10
		number = elem1
	return sum_elem


def phono(x): #Перевод слова в код по словорю.
	newWord = ''
	value_in_phono={
		'A':'00000','B':'00001','C':'00010','D':'00011',
		'E':'00100','F':'00101','G':'00110','H':'00111',
		'I':'01000','J':'01001','K':'01010','L':'01011',
		'M':'01100','N':'01101','O':'01110','P':'01111',
		'Q':'10000','R':'10001','S':'10010','T':'10011',
		'U':'1010','V':'1011','W':'1100','X':'1101',
		'Y':'1110','Z':'1111',
	}
	for i in x:
		newWord += value_in_phono[i]
	newWord = int(newWord)
	return newWord


def tenForY(num, x2 = 2): #Перевод из десятичной СС в двоичную СС.
	a = num
	b = 0
	sum_elem = 0
	while a >= x2:
		elem = a % x2	
		elem1 = elem * (10**b)
		sum_elem += elem1
		b += 1
		a = a // x2
	elem3 = a*(10**b)
	sum_elem += elem3
	return sum_elem


def binaryFloat(n): #Перевод вещественной части числа в двоичную СС.
	number = n/100  
	step = 7
	binaryNumberArray = ''
	numFloat = number % 1
	while numFloat != 0 and step != 0:
		numInt = number // 1
		numInt = int(numInt)
		binaryNumberArray += str(numInt)
		numFloat = number % 1
		numFloat = round(numFloat, 2)
		number = numFloat * 2
		step -= 1
	newWordBin = binaryNumberArray[1:]
	return newWordBin


def numberFibanachi(number): #Перевод числа в Фибоначчиеву СС.
	numberFibanachi = [55,34,21,13,8,5,3,2,1]
	numForFib = number
	fibNumber = ''
	for i in numberFibanachi:
		if i <= numForFib:
			numForFib -= i
			fibNumber += '1'
		else:
			fibNumber += '0'
	return int(fibNumber)


def ceasarCipher(word, values): #Зашифровка слова по шифру Цезаря.
	eanglishA = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
	word = word.upper()
	len_alpha = len(eanglishA)
	new_word = ''
	for i in range(len(word)):
		index = eanglishA.index(word[i])
		indexFC = index+values
		if indexFC > (len_alpha-1):
			step = indexFC // (len_alpha-1)
			if indexFC / (len_alpha-1) == 0:
				step -= 1
			indexFC = indexFC - (len_alpha-1)*step
		new_word += eanglishA[indexFC]
	return new_word


def gameLogic(hour, minute, day, month): #Логика игры. Возвращает массив с готовыми ответами на каждый шаг.
	word = 'HELP'
	#1
	contNum = str(numberFibanachi(hour)) + str(numberFibanachi(minute))
	#3
	sumCountNum = 0
	for i in contNum:
		if i == '1':
			sumCountNum += 1
	ceCi = ceasarCipher(word, sumCountNum)
	#2
	date = str(tenForY(day,2)) + binaryFloat(month)
	date = int(date)
	#4
	phonoOut = phono(ceCi)
	#5
	date_ten = xForTen(date); phonoOut_ten = xForTen(phonoOut);
	difOut1 = phonoOut_ten - date_ten
	difOut2 = tenForY(difOut1, 2)
	#6
	sumOut = str(difOut1)
	sim = len(list(sumOut))
	while sim < 8:
		sim += 1
		sumOut += '0'

	sumCountNum = str(sumCountNum)
	date = str(date)
	difOut2 = str(difOut2)
	phonoOut = str(phonoOut)
	sumOut = str(sumOut)
	answers = [sumCountNum,ceCi,date,phonoOut,difOut2,sumOut]
	return answers


def quitProgramm(): #Функция для выхода из программы.
	root.destroy()


def quitMenu(root): #Функция для выхода из вкладки программы в главное меню.
	global stepGame, stepRous
	stepRous = 0
	stepGame = 1
	main(root)


def gameData(): #Функция, которая формирует час, минуты, день, месяц для игры. Возвращает массив с этими значениями.
	hour = random.randint(0,23)
	minute = random.randint(0,59)
	day = random.randint(1,29)
	month = random.randint(1,12)
	dataGameData = [hour, minute, day, month]
	return dataGameData



def error(root, rez): #Функция обрабатывающая нажатие кнопок в окне "Ошибка"
	global score, stepGame
	stepGame = 1
	if rez == 0:
		score = 1
		main(root)
	if rez == 1:
		score += 1
		game(root,step=stepGame,score=score)


def errorGame(root): #Функция вызываемая, при допущении ошибки пользователем. Отрисовывает окно "Ошибка"
	global destroy_object
	for objectD in destroy_object:
		objectD.destroy()
	destroy_object = []
	errorFrame = Frame(root,bg='white')
	destroy_object.append(errorFrame)
	errorText = Label(
		errorFrame, 
		text="Вы ошиблись!\nХотите попробовать ещё раз?", 
		font='Times 30'
		)
	destroy_object.append(errorText)
	buttonYes = Button(
		errorFrame, text="Да", bg='#32CD32', 
		fg="white", font="Times 20", 
		command = lambda: error(root, 1)
		)
	destroy_object.append(buttonYes)
	buttonNo = Button(
		errorFrame, text="Нет", bg='#B22222', 
		fg="white", font="Times 20", 
		command = lambda: error(root, 0)
		)
	destroy_object.append(buttonNo)
	errorFrame.place(width=700, height=400, x=150, y=100)
	errorText.place(width=700, height=200, x=0, y=50)
	buttonYes.place(width=250, height=40 ,x=375 , y=300)
	buttonNo.place(width=250, height=40 ,x=75 , y=300)


def passGame(root, passValue, step): #Функция обрабатывающая ответ пользователя в игре.
	global out, stepGame
	value = passValue.get()
	value = value.strip(' ').upper()
	if value == out[step-1]:
		stepGame += 1
		if stepGame == 7: # При правильном ответе в последнем шаге.
			winGame(root)
		else:
			game(root, step=stepGame) #При правильном ответе в шаге.
	else:
		errorGame(root) #Если пользователь допустил ошибку, то его перекидывает на окно "Ошибка"


def winGame(root): #Функция вызываемая, при правильном ответе пользователя на последнем шаге. Отрисовывает окно "Победа"
	global destroy_object, score, stepGame
	score = 1
	stepGame = 1
	for objectD in destroy_object:
		objectD.destroy()
	destroy_object = []
	winFrame = Frame(root,bg='white')
	destroy_object.append(winFrame)
	winText = Label(
		winFrame, 
		text="Поздравляю! Вы спасли мир!\nХотите попробовать ещё раз?", 
		font='Times 30'
		)
	destroy_object.append(winText)
	buttonYes = Button(
		winFrame, text="Да", bg='#32CD32', 
		fg="white", font="Times 20", 
		command = lambda: game(root,step=stepGame,score=score)
		)
	destroy_object.append(buttonYes)
	buttonNo = Button(
		winFrame, text="Нет", bg='#B22222', 
		fg="white", font="Times 20", 
		command = lambda: main(root)
		)
	destroy_object.append(buttonNo)
	winFrame.place(width=700, height=400, x=150, y=100)
	winText.place(width=700, height=200, x=0, y=50)
	buttonYes.place(width=250, height=40 ,x=75 , y=300)
	buttonNo.place(width=250, height=40 ,x=375 , y=300)


def game(root, step=1, score=1): #Основная функция игры.
	global destroy_object, data, out, stepGame
	for objectD in destroy_object:
		objectD.destroy()
	destroy_object = []
	if stepGame == 1:
		data = gameData()
		out = gameLogic(hour=data[0], minute=data[1], day=data[2], month=data[3])
		for i in out:
			print(i)
	if data[3] < 10:
		monthStr = '0' + str(data[3])
	else:
		monthStr = str(data[3])
	if data[0] < 10:
		hourStr = '0' + str(data[0])
	else:
		hourStr = str(data[0])
	if data[1] < 10:
		minuteStr = '0' + str(data[1])
	else:
		minuteStr = str(data[1])
	if data[2] < 10:
		dayStr = '0' + str(data[2])
	else:
		dayStr = str(data[2])
	footerFrameGame = Frame(root,bg='#9480AD')
	destroy_object.append(footerFrameGame)
	labelTimeGame = Label(
		footerFrameGame, 
		text=hourStr+':'+minuteStr+'     '+dayStr+'.'+monthStr, font="Times 16"
		)
	destroy_object.append(labelTimeGame) 
	labelStepGame = Label(
		footerFrameGame, 
		text="Шаг " + str(stepGame) + "/6",font="Times 16"
		)
	destroy_object.append(labelStepGame) 
	labelScoreGame = Label(
		footerFrameGame, 
		text="Попытка "+str(score),font="Times 16"
		)
	destroy_object.append(labelScoreGame)
	mainTextFrame = Frame(root, bg='#C4E3DD')
	destroy_object.append(mainTextFrame)
	mainStepFrame = Frame(root, bg='#C4E3DD')
	destroy_object.append(mainStepFrame)
	mainStepLable = Label(mainStepFrame, text='Ответы:', font="Times 30" )
	destroy_object.append(mainStepLable)
	mainButtonFrame = Frame(root, bg='black')
	destroy_object.append(mainButtonFrame)
	entryAnswer = Entry(mainTextFrame, bg='#fff', font='Times 18')
	destroy_object.append(entryAnswer)
	buttonNextGame = Button(
		root, text="Далее", bg='#9480AD' , 
		fg='#fff', font="Times 20",
		command = lambda: passGame(root, entryAnswer, stepGame)
		)
	destroy_object.append(buttonNextGame)
	buttonExitGame = Button(
		root, text="Выход", bg='#9480AD', 
		fg="#fff", font="Times 20", 
		command = lambda: quitMenu(root)
		)
	destroy_object.append(buttonExitGame)
	textStepGame = Label(
		mainTextFrame, text=textGame[stepGame-1], 
		font="Times 19", bg='#C4E3DD'
		)
	destroy_object.append(labelScoreGame)
	wordStepGame = Label(mainStepFrame,text="HELP", font="Times 30")
	destroy_object.append(wordStepGame)
	wordStepGame.place(width=270, height=75,x=0,y=375)
	mainStepLable.place(width=270, height=75,x=0,y=0)
	entryAnswer.place(width=300, height=40, x=195, y=400)
	textStepGame.place(width=650, height=410,x=0,y=0)
	labelTimeGame.place(width=200, height=30,x=10,y=10)
	labelStepGame.place(width=200, height=30,x=400,y=10)
	labelScoreGame.place(width=200, height=30,x=790,y=10)
	footerFrameGame.place(width=1000, height=50)
	mainTextFrame.place(width=690, height=450, x=300, y=60)
	mainStepFrame.place(width=270, height=450, x=10, y=60)
	mainButtonFrame.place(width=690, height=60, x=300, y=510)
	buttonNextGame.place(width=250, height=40 ,x=520 , y=520)
	buttonExitGame.place(width=200, height=40 ,x=35 , y=520)
	if stepGame > 1:
		mainStepOne = Label(mainStepFrame, text=out[0], font="Times 20")
		destroy_object.append(mainStepOne)
		mainStepOne.place(width=270, height=20, x=0, y=95)
	if stepGame > 2:
		mainStepTwo = Label(mainStepFrame, text=out[1], font="Times 20")
		destroy_object.append(mainStepTwo)
		mainStepTwo.place(width=270, height=20, x=0, y=125)
	if stepGame > 3:
		mainStepThree = Label(mainStepFrame, text=out[2], font="Times 20")
		destroy_object.append(mainStepThree)
		mainStepThree.place(width=270, height=20, x=0, y=155)
	if stepGame > 4:
		mainStepFour = Label(mainStepFrame, text=out[3], font="Times 15")
		destroy_object.append(mainStepFour)
		mainStepFour.place(width=270, height=20, x=0, y=185)
	if stepGame > 5:
		mainStepFive = Label(mainStepFrame, text=out[4], font="Times 15")
		destroy_object.append(mainStepFive)
		mainStepFive.place(width=270, height=20, x=0, y=215)


def downStepRous(root): #Переключает на предидущий слайд во вкладке "Предыстория"
	global stepRous
	stepRous -= 1
	rousMenu(root, stepRous)


def upStepRous(root): #Переключает на слудеющий слайд во вкладке "Предыстория"
	global stepRous
	stepRous += 1
	rousMenu(root, stepRous)


def rousMenu(root,step=0): #Функция отрисовки окна "Предыстория"
	global destroy_object
	for objectD in destroy_object:
		objectD.destroy()
	destroy_object = []
	rousTextFrame = Frame(root, bg='#C4E3DD')
	destroy_object.append(rousTextFrame)
	rousText = Label(
		rousTextFrame, text=textHistory[step], 
		font="Times 19", bg='#C4E3DD'
		)
	destroy_object.append(rousText)
	if step < 5:
		rousNextButton = Button(
			root, text="Далее", bg='#C4E3DD', 
			fg="#000", font="Times 24", 
			command = lambda: upStepRous(root)
			)
		destroy_object.append(rousNextButton)
		rousNextButton.place(height=50,width=300,x=350,y=430)

	if step > 0:
		rousBackButton = Button(
			root, text="Назад", bg='#C4E3DD', 
			fg="#000", font="Times 24", 
			command = lambda: downStepRous(root)
			)
		destroy_object.append(rousBackButton)
		rousBackButton.place(height=50,width=300,x=350,y=485)

	rousTextFrame.place(height=400,width=800,x=125,y=20)
	rousText.place(height=400,width=730,x=0,y=0)
	buttonExitRous = Button(
		root, text="Выход", bg='#9480AD', 
		fg="#fff", font="Times 24", 
		command = lambda: quitMenu(root)
		)
	destroy_object.append(buttonExitRous)
	buttonExitRous.place(height=50,width=300,x=350,y=540)


def main(root): #Функция отрисовки главного меню программы.
	global destroy_object, stepRous, stepGame
	for objectD in destroy_object:
		objectD.destroy()
	destroy_object = []
	buttonPlay = Button(
		root, text="Играть", width=15, height=7, 
		bg='#C4E3DD', fg="#000", font="Times 24", 
		command = lambda: game(root)
		)
	destroy_object.append(buttonPlay)
	buttonPlay.place(height=70,width=300,x=350,y=380)
	buttonRous = Button(
		root, text="Предыстория", width=15, height=7, 
		bg='#C4E3DD', fg="#000", font="Times 24", 
		command = lambda: rousMenu(root)
		)
	destroy_object.append(buttonRous)
	buttonRous.place(height=70,width=300,x=350,y=280)
	buttonExit = Button(
		root, text="Выход", width=15, height=2, 
		bg='#9480AD', fg="#fff", font="Times 24", 
		command = quitProgramm
		)
	destroy_object.append(buttonExit)
	buttonExit.place(height=70,width=300,x=350,y=480)


def textStepGames(): #Текст для описания задания в игре.

	stepOne = '''
	(Время и Дата отображены в левом верхнем улгу.)
	Хм... На листе записаны время и дата... 
	Может это и есть кодовые числа? 
	Переведем часы и минуты в Фибоначчиевую 
	систему счисления.
	СС состоит из 0 и 1, а базис её числа
	Фибаначи [55,34,21,13,8,5,3,2,1].
	Запишем эти два числа вместе, без пробелов.
	В полученном числе посчитаем количество едениц'''
	
	stepTwo = '''
	Теперь с помощью рассчитанного шага, 
	нужно зашифровать HELP по шифру Цезаря 
	Шифр Цезаря — это вид шифра подстановки, 
	в котором каждый символ в открытом тексте 
	заменяется символом, находящимся на 
	некотором постоянном числе позиций правее 
	него в алфавите.. Например: 
	шаг = 3, значит буква A зашифруется в D

	Английский алфавит
	A  B  C  D  E  F  G  H  I  J  K  L  M 
	N  O  P  Q  R  S  T  U  V  W  X  Y  Z'''
	
	stepThree = '''
	Профессор перевёл дату и месяц в двочную систему,
	подразумивая, что месяц - дробная часть числа(
	18.01 = 18,01). Переведем это число в двоичную систему.
	И убрав запятую запишем число без пробелов.
	Условно назовем полученное число - ДАТА'''
	
	stepFour = '''
	Переведи зашифрованное слово в двоичный код 
	по принципу Фоно.

	A=00000 B=00001 C=00010 D=00011 E=00100 
	F=00101 G=00110 H=00111 I=01000 J=01001 
	K=01010 L=01011 M=01100 N=01101 O=01110 
	P=01111 Q=10000 R=10001 S=10010 T=10011 
	U=1010 V=1011 W=1100 X=1101 Y=1110 Z=1111'''

	stepFive = '''
	Теперь осталось отнять из полученного 
	двоичного числа(из предидущего шага) 
	число ДАТА.
	(оставить результат в двоичной СС)'''
	
	stepSix = '''
	Переводим получившееся число 
	в десятичную систему счисления.
	Если в коде меньше восьми символов, 
	значит приписываем в конце нули,
	пока длина итогового кода не станет равна 8'''

	
	stepArray = [stepOne, stepTwo, stepThree, stepFour, stepFive, stepSix]
	return stepArray


def textRousHistory(): #Текст для вкладки "Предыстория".
	stepHistoryOne = '''
	Шёл 2020 год. Мир охватила пандемия. Смертельный 
	вирус распространился по всей планете. Каждый день 
	люди умирали тысячами. Известный доктор биологических 
	наук - профессор Провалов потерял свою жену. Он взял 
	её биологический материал для исследований. Чтобы не 
	заразиться от людей, он решил спустится в бункер для 
	проведения экспериментов по разработке вакцины 
	      от нового опаснейшего вируса…'''
	stepHistoryTwo = '''
	Через какое-то время. Ресурсы профессора заканчивались. 
	У него практически не осталось воды, еда была на 
	исходе. Все эти месяцы доктор упорно работал над 
	созданием вакцины, но все попытки были тщетны… 
	Сегодня он опробовал очередную разработку 
	на последней крысе, но опять – провал. 
	Всю ночь профессор не спал. 
	Он вспоминал свою жену, вспоминал жизнь до эпидемии… '''
	stepHistoryThree = '''
	Вдруг раздался грохот! Упала клетка. Вместе с ней 
	разбилось несколько пробирок.  Профессор подошёл, 
	чтобы поставить клетку обратно на стол. Он взял клетку,
	но сразу же уронил на пол. Его укусила крыса!
	От потрясения, что крыса жива и вакцина работает, 
	у профессора закружилась голова и он облокотился на стол.
	И не заметил, что разлитый яд попал ему в рану. '''
	stepHistoryFour = '''
	Доктор сразу же отправил сообщение своему лучшему 
	студенту, о том, что он разработал вакцину от вируса. 
	И сказал, чтобы завтра он пришел к нему. 
	Профессор подумал, что нужно положить все разработки 
	в надежное место.'''
	stepHistoryFive = '''
	На следующий день студент Ваня Недоспасов, 
	подойдя к дому, увидел, что дверь открыта. 
	Он вошёл. Все вещи были вытащены их шкафов и 
	разбросаны по полу. Ваня спустился в бункер. 
	Там дверь была закрыта. Он знал код, профессор 
	всегда придумывал шифр для кодового числа или слова. 
	Ваня вошёл в бункер и увидел, что профессор 
	сидит в кресле. Он его окликнул,
	но доктор не отвечал. Молодой студент решил, 
	что профессор спит. Но когда он к нему подошел, 
	то понял, что доктор мёртв.'''
	stepHistorySix = '''
	Ваня начал осматриваться, но не мог найти ни вакцины, ни 
	документов по разработке. И тут он увидел на столе листок. 
	Он понял, что это лист с алгоритмом для какого-то замка. 
	Ваня оглянулся и увидел сейф. Осталось лишь разгадать шифр… 
	Теперь только от Вани зависит судьба человечества…'''
	stepHistoryArray = [
	stepHistoryOne, stepHistoryTwo, 
	stepHistoryThree, stepHistoryFour, 
	stepHistoryFive, stepHistorySix
	]
	return stepHistoryArray


textGame = textStepGames()
textHistory = textRousHistory()
data = []
out = []
stepRous = 0
stepGame = 1
destroy_object = []
root = Tk()
root.title("Открой Сейф")
root.iconbitmap('icon.ico')
root.geometry('1000x600')
root.resizable(width=False, height=False)
image = ImageTk.PhotoImage(Image.open("main.jpg"))
mainImage = Label(image=image)
mainImage.place(height=600,width=1000,x=0,y=0)
main(root)
root.mainloop()
