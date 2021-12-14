import random
from tkinter import *
from PIL import ImageTk, Image
from resource_files.number_system import *
from resource_files.text import *
from resource_files.cipher import *
from resource_files.game_logic import *

# Function to exit the program
def quitProgramm():
	root.destroy()


# Function to exit the program tab to the main menu
def quitMenu(root): 
	global STEP_GAME, STEP_ROUS
	# Resetting global variables
	STEP_ROUS = 0
	STEP_GAME = 1
	mainWindow(root)

'''
The function that forms the hour, 
minutes, day, month for the game
'''
def gameData():
	hour = random.randint(0, 23)
	minute = random.randint(0, 59)
	day = random.randint(1, 29)
	month = random.randint(1, 12)
	ldata_game = [hour, minute, day, month]
	return ldata_game


'''
Function that handles pressing 
buttons in the "Error" window
'''
def error(root, result_bool):
	global SCORE, STEP_GAME
	STEP_GAME = 1
	if result_bool == 0:
		SCORE = 1
		mainWindow(root)
	if result_bool == 1:
		SCORE += 1
		gameWindow(root, step = STEP_GAME, score = SCORE)


''' 
The function to be called when an error 
is made by the user. Renders the "Error" window
'''
def errorGame(root): 
	global LDESTROY_OBJECT
	# Destroying all objects on the screen
	for objectD in LDESTROY_OBJECT:
		objectD.destroy()
	LDESTROY_OBJECT = []
	error_frame = Frame(root, bg = 'white')
	LDESTROY_OBJECT.append(error_frame)
	error_text = Label(
		error_frame, 
		text = "Вы ошиблись!\nХотите попробовать ещё раз?", 
		font = "Times 30"
		)
	LDESTROY_OBJECT.append(error_text)
	button_yes = Button(
		error_frame, text = "Да", bg = '#32CD32', 
		fg = "white", font = "Times 20", 
		command = lambda: error(root , 1)
		)
	LDESTROY_OBJECT.append(button_yes)
	button_no = Button(
		error_frame, text = "Нет", bg = '#B22222', 
		fg = "white", font = "Times 20", 
		command = lambda: error(root, 0)
		)
	LDESTROY_OBJECT.append(button_no)
	error_frame.place(width = 700, height = 400, x = 150, y = 100)
	error_text.place(width = 700, height = 200, x = 0, y = 50)
	button_yes.place(width = 250, height = 40 ,x = 375 , y = 300)
	button_no.place(width = 250, height = 40 ,x = 75 , y = 300)

'''
Function that processes 
the user's response in the game.
'''
def passGame(root, pass_value, step): 
	global LOUT, STEP_GAME
	value = pass_value.get()
	value = value.strip(' ').upper()
	if value == LOUT[step-1]:
		STEP_GAME += 1
		if STEP_GAME == 7: # With the correct answer in the last step
			winGame(root)
		else:
			gameWindow(root, step=STEP_GAME) # With the correct answer in a step
	else:
		errorGame(root) # If the user makes a mistake, then he is thrown to the "Error" window

'''
The function to be called 
when the user responds 
correctly at the last step. 
Renders the "Victory" window
'''
def winGame(root): 
	global LDESTROY_OBJECT, SCORE, STEP_GAME
	SCORE = 1
	STEP_GAME = 1
	for objectD in LDESTROY_OBJECT:
		objectD.destroy()
	LDESTROY_OBJECT = []
	win_frame = Frame(root, bg = 'white')
	LDESTROY_OBJECT.append(win_frame)
	win_text = Label(
		win_frame, 
		text = "Поздравляю! Вы спасли мир!\nХотите попробовать ещё раз?", 
		font = 'Times 30'
		)
	LDESTROY_OBJECT.append(win_text)
	button_yes = Button(
		win_frame, text = "Да", bg = '#32CD32', 
		fg = "white", font = "Times 20", 
		command = lambda: gameWindow(root, step=STEP_GAME, score=SCORE)
		)
	LDESTROY_OBJECT.append(button_yes)
	button_no = Button(
		win_frame, text = "Нет", bg = '#B22222', 
		fg= "white", font = "Times 20", 
		command = lambda: mainWindow(root)
		)
	LDESTROY_OBJECT.append(button_no)
	win_frame.place(width = 700, height = 400, x = 150, y = 100)
	win_text.place(width = 700, height = 200, x = 0, y = 50)
	button_yes.place(width = 250, height = 40 ,x = 75 , y = 300)
	button_no.place(width = 250, height = 40 ,x = 375 , y = 300)

'''
Function with the logic of 
displaying GUI, etc. in the game window
'''
def gameWindow(root, step=1, score=1): 
	global LDESTROY_OBJECT, LDATA, LOUT, STEP_GAME
	# Destroying all objects on the screen
	for objectD in LDESTROY_OBJECT:
		objectD.destroy()
	LDESTROY_OBJECT = []
	if STEP_GAME == 1:
		LDATA = gameData()
		LOUT = creatingResponses(hours=LDATA[0], minutes=LDATA[1], day=LDATA[2], month=LDATA[3])
		for i in LOUT:
			print(i)
	if LDATA[3] < 10:
		month_str = '0' + str(LDATA[3])
	else:
		month_str = str(LDATA[3])
	if LDATA[0] < 10:
		hour_str = '0' + str(LDATA[0])
	else:
		hour_str = str(LDATA[0])
	if LDATA[1] < 10:
		minute_str = '0' + str(LDATA[1])
	else:
		minute_str = str(LDATA[1])
	if LDATA[2] < 10:
		day_str = '0' + str(LDATA[2])
	else:
		day_str = str(LDATA[2])
	footer_frame_game = Frame(root, bg = '#9480AD')
	LDESTROY_OBJECT.append(footer_frame_game)
	label_time_game = Label(
		footer_frame_game, 
		text = hour_str + ':' + minute_str + '     ' + day_str + '.' + month_str, font = "Times 16"
		)
	LDESTROY_OBJECT.append(label_time_game) 
	label_step_game = Label(
		footer_frame_game, 
		text = "Шаг " + str(STEP_GAME) + "/6", font = "Times 16"
		)
	LDESTROY_OBJECT.append(label_step_game) 
	label_score_game = Label(
		footer_frame_game, 
		text = "Попытка " + str(score), font = "Times 16"
		)
	LDESTROY_OBJECT.append(label_score_game)
	main_text_frame = Frame(root, bg = '#C4E3DD')
	LDESTROY_OBJECT.append(main_text_frame)
	main_step_frame = Frame(root, bg = '#C4E3DD')
	LDESTROY_OBJECT.append(main_step_frame)
	main_step_lable = Label(main_step_frame, text = 'Ответы:', font = "Times 30" )
	LDESTROY_OBJECT.append(main_step_lable)
	main_button_frame = Frame(root, bg = 'black')
	LDESTROY_OBJECT.append(main_button_frame)
	entry_answer = Entry(main_text_frame, bg = '#fff', font = 'Times 18')
	LDESTROY_OBJECT.append(entry_answer)
	button_next_game = Button(
		root, text = "Далее", bg = '#9480AD' , 
		fg = '#fff', font = "Times 20",
		command = lambda: passGame(root, entry_answer, STEP_GAME)
		)
	LDESTROY_OBJECT.append(button_next_game)
	button_exit_game = Button(
		root, text = "Выход", bg = '#9480AD', 
		fg = "#fff", font = "Times 20", 
		command = lambda: quitMenu(root)
		)
	LDESTROY_OBJECT.append(button_exit_game)
	text_step_game = Label(
		main_text_frame, text = text_game[STEP_GAME-1], 
		font = "Times 19", bg = '#C4E3DD'
		)
	LDESTROY_OBJECT.append(label_score_game)
	word_step_game = Label(main_step_frame, text = "HELP", font = "Times 30")
	LDESTROY_OBJECT.append(word_step_game)
	word_step_game.place(width = 270, height = 75, x = 0, y = 375)
	main_step_lable.place(width = 270, height = 75, x = 0, y = 0)
	entry_answer.place(width = 300, height = 40, x = 195, y = 400)
	text_step_game.place(width = 650, height = 410, x = 0, y = 0)
	label_time_game.place(width = 200, height = 30, x = 10, y = 10)
	label_step_game.place(width = 200, height = 30, x = 400, y = 10)
	label_score_game.place(width = 200, height = 30, x = 790, y = 10)
	footer_frame_game.place(width = 1000, height = 50)
	main_text_frame.place(width = 690, height = 450, x = 300, y = 60)
	main_step_frame.place(width = 270, height = 450, x = 10, y = 60)
	main_button_frame.place(width = 690, height = 60, x = 300, y = 510)
	button_next_game.place(width = 250, height = 40 ,x = 520 , y = 520)
	button_exit_game.place(width = 200, height = 40 ,x = 35 , y = 520)
	if STEP_GAME > 1:
		main_step_one = Label(main_step_frame, text = LOUT[0], font = "Times 20")
		LDESTROY_OBJECT.append(main_step_one)
		main_step_one.place(width = 270, height = 20, x = 0, y = 95)
	if STEP_GAME > 2:
		main_step_two = Label(main_step_frame, text = LOUT[1], font = "Times 20")
		LDESTROY_OBJECT.append(main_step_two)
		main_step_two.place(width = 270, height = 20, x = 0, y = 125)
	if STEP_GAME > 3:
		main_step_three = Label(main_step_frame, text = LOUT[2], font = "Times 20")
		LDESTROY_OBJECT.append(main_step_three)
		main_step_three.place(width = 270, height = 20, x = 0, y = 155)
	if STEP_GAME > 4:
		main_step_four = Label(main_step_frame, text = LOUT[3], font = "Times 15")
		LDESTROY_OBJECT.append(main_step_four)
		main_step_four.place(width = 270, height = 20, x = 0, y = 185)
	if STEP_GAME > 5:
		main_step_five = Label(main_step_frame, text = LOUT[4], font = "Times 15")
		LDESTROY_OBJECT.append(main_step_five)
		main_step_five.place(width = 270, height = 20, x = 0, y = 215)


def downStepRous(root): #Переключает на предидущий слайд во вкладке "Предыстория"
	global STEP_ROUS
	STEP_ROUS -= 1
	rousMenu(root, STEP_ROUS)


def upStepRous(root): #Переключает на слудеющий слайд во вкладке "Предыстория"
	global STEP_ROUS
	STEP_ROUS += 1
	rousMenu(root, STEP_ROUS)


def rousMenu(root,step=0): #Функция отрисовки окна "Предыстория"
	global LDESTROY_OBJECT
	for objectD in LDESTROY_OBJECT:
		objectD.destroy()
	LDESTROY_OBJECT = []
	rous_text_frame = Frame(root, bg = '#C4E3DD')
	LDESTROY_OBJECT.append(rous_text_frame)
	rous_text = Label(
		rous_text_frame, text = text_history[step], 
		font = "Times 19", bg = '#C4E3DD'
		)
	LDESTROY_OBJECT.append(rous_text)
	if step < 5:
		rous_next_button = Button(
			root, text = "Далее", bg = '#C4E3DD', 
			fg = "#000", font = "Times 24", 
			command = lambda: upStepRous(root)
			)
		LDESTROY_OBJECT.append(rous_next_button)
		rous_next_button.place(height = 50, width = 300, x = 350, y = 430)

	if step > 0:
		rous_back_button = Button(
			root, text = "Назад", bg = '#C4E3DD', 
			fg = "#000", font = "Times 24", 
			command = lambda: downStepRous(root)
			)
		LDESTROY_OBJECT.append(rous_back_button)
		rous_back_button.place(height = 50, width = 300, x = 350, y = 485)

	rous_text_frame.place(height = 400, width = 800, x = 125, y = 20)
	rous_text.place(height = 400, width = 730, x = 0, y = 0)
	button_exit_rous = Button(
		root, text = "Выход", bg = '#9480AD', 
		fg = "#fff", font = "Times 24", 
		command = lambda: quitMenu(root)
		)
	LDESTROY_OBJECT.append(button_exit_rous)
	button_exit_rous.place(height = 50, width = 300, x = 350, y = 540)


def mainWindow(root): #Функция отрисовки главного меню программы.
	global LDESTROY_OBJECT, STEP_ROUS, STEP_GAME
	for objectD in LDESTROY_OBJECT:
		objectD.destroy()
	LDESTROY_OBJECT = []
	button_play = Button(
		root, text = "Играть", width = 15, height = 7, 
		bg = '#C4E3DD', fg = "#000", font = "Times 24", 
		command = lambda: gameWindow(root)
		)
	LDESTROY_OBJECT.append(button_play)
	button_play.place(height = 70, width = 300, x = 350, y = 380)
	button_rous = Button(
		root, text = "Предыстория", width = 15, height = 7, 
		bg = '#C4E3DD', fg = "#000", font = "Times 24", 
		command = lambda: rousMenu(root)
		)
	LDESTROY_OBJECT.append(button_rous)
	button_rous.place(height = 70, width = 300, x = 350, y = 280)
	button_exit = Button(
		root, text = "Выход", width = 15, height = 2, 
		bg = '#9480AD', fg = "#fff", font = "Times 24", 
		command = quitProgramm
		)
	LDESTROY_OBJECT.append(button_exit)
	button_exit.place(height = 70, width = 300, x = 350, y = 480)


text_game = textStepGames()
text_history = textRousHistory()
LDATA = []
LOUT = []
STEP_ROUS = 0
STEP_GAME = 1
LDESTROY_OBJECT = []
root = Tk()
root.title("Открой Сейф")
root.iconbitmap('templates/icon.ico')
root.geometry('1000x600')
root.resizable(width = False, height=  False)
image = ImageTk.PhotoImage(Image.open("templates/main.jpg"))
mainImage = Label(image=image)
mainImage.place(height = 600, width = 1000, x = 0, y = 0)
mainWindow(root)
root.mainloop()
