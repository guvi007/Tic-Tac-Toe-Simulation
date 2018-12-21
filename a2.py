# GAURAV AGGARWAL
# 2017288 - A3


#Assignment-2, Game Tic-tac-toe

#State: Tiles are numbered 1 to 9

"""
Tick-Tac-Toe game state is defined as follows: 

tile1 |  tile2  | tile3
______|_________|______
tile4 |  tile5  | tile6
______|_________|______
tile7 |  tile8  | tile9
______|_________|______

A player can belong to one of the following two categories:
1. Naive: Player checks a tile randomly.
2. Intelligent: Player follows some strategy to win a game. You shall define a strategy that an intelligent player can take.

We will estimate probability of winning for a player for different scenarios.
 
Game1: A number of games are played between two naive players. Estimate probability of winning for player1. Assume player1 starts the game.

Game2: A number of games are played between a naive and intelligent player. Estimate probability of winning for player1. Assume player1 is naive and starts the game.

Game3: A number of games are played between two intelligent players. Estimate probability of winning for player1. Assume player1 starts the game.  
"""

import random as rn
import globals																		# globals module containing all the global variables

def set_variables():																
	"""
		resets all the tiles to initials values and turn to player 1
	"""
	globals.tile1 = globals.tile2 = globals.tile3 = globals.tile4 = globals.tile5 = globals.tile6 = globals.tile7 = globals.tile8 = globals.tile9 = 0
	globals.turn = globals.player1

def validmove(move):
	""" Checks whether a move played by a player is valid or invalid.
		Return True if move is valid. 
		
		A move is valid if the corresponding tile for the move is not ticked.
	"""
	assert 1<=move<=9,'move taken is not valid'
	if (globals.turn == globals.player1):
		if (move == 1 and globals.tile1 == 0):
			globals.tile1 = 1
			return True
		elif (move == 2 and globals.tile2 == 0):
			globals.tile2 = 1
			return True
		elif (move == 3 and globals.tile3 == 0):
			globals.tile3 = 1
			return True
		elif (move == 4 and globals.tile4 == 0):
			globals.tile4 = 1
			return True
		elif (move == 5 and globals.tile5== 0):
			globals.tile5 = 1
			return True
		elif (move == 6 and globals.tile6 == 0):
			globals.tile6 = 1
			return True
		elif (move == 7 and globals.tile7 == 0):
			globals.tile7 = 1
			return True
		elif (move == 8 and globals.tile8 == 0):
			globals.tile8 = 1
			return True
		elif (move == 9 and globals.tile9 == 0):
			globals.tile9 = 1
			return True
		else:
			return False
	else:
		if (move == 1 and globals.tile1 == 0):
			globals.tile1 = 2
			return True
		elif (move == 2 and globals.tile2 == 0):
			globals.tile2 = 2
			return True
		elif (move == 3 and globals.tile3 == 0):
			globals.tile3 = 2
			return True
		elif (move == 4 and globals.tile4 == 0):
			globals.tile4 = 2
			return True
		elif (move == 5 and globals.tile5== 0):
			globals.tile5 = 2
			return True
		elif (move == 6 and globals.tile6 == 0):
			globals.tile6 = 2
			return True
		elif (move == 7 and globals.tile7 == 0):
			globals.tile7 = 2
			return True
		elif (move == 8 and globals.tile8 == 0):
			globals.tile8 = 2
			return True
		elif (move == 9 and globals.tile9 == 0):
			globals.tile9 = 2
			return True
		else:
			return False

def win():
	""" Returns True if the board state specifies a winning state for some player.
		
		A player wins if ticks made by the player are present either
		i) in a row
		ii) in a cloumn
		iii) in a diagonal
	"""
	'''
	if (globals.tile1==globals.tile2==globals.tile3!=0 or globals.tile4==globals.tile5==globals.tile6!=0 or globals.tile7==globals.tile8==globals.tile9!=0 or globals.tile1==globals.tile4==globals.tile7!=0 or globals.tile2==globals.tile5==globals.tile8!=0 or globals.tile3==globals.tile6==globals.tile9!=0 or globals.tile1==globals.tile5==globals.tile9!=0 or globals.tile3==globals.tile5==globals.tile7!=0):
		return True
	'''
	if (globals.tile1 == 1 and globals.tile2 == 1 and globals.tile3 == 1) or (globals.tile4 == 1 and globals.tile5 == 1 and globals.tile6 == 1) or (globals.tile7 == 1 and globals.tile8 == 1 and globals.tile9 == 1) or (globals.tile1 == 1 and globals.tile4 == 1 and globals.tile7 == 1) or (globals.tile2 == 1 and globals.tile5 == 1 and globals.tile8 == 1) or (globals.tile3 == 1 and globals.tile6 == 1 and globals.tile9 == 1) or (globals.tile1 ==1 and globals.tile5 == 1 and globals.tile9 == 1) or (globals.tile3 == 1 and globals.tile5 == 1 and globals.tile7 == 1):
		return True
	elif (globals.tile1 == 2 and globals.tile2 == 2 and globals.tile3 == 2) or (globals.tile4 == 2 and globals.tile5 == 2 and globals.tile6 == 2) or (globals.tile7 == 2 and globals.tile8 == 2 and globals.tile9 == 2) or (globals.tile1 == 2 and globals.tile4 == 2 and globals.tile7 == 2) or (globals.tile2 == 2 and globals.tile5 == 2 and globals.tile8 == 2) or (globals.tile3 == 2 and globals.tile6 == 2 and globals.tile9 == 2) or (globals.tile1 == 2 and globals.tile5 == 2 and globals.tile9 == 2) or (globals.tile3 == 2 and globals.tile5 == 2 and globals.tile7 == 2):
		return True
	else:
		return False
	
def takeNaiveMove():
	""" Returns a tile number randomly from the set of unchecked tiles with uniform probability distribution.    
	"""
	return rn.randint(1,9)

def takeStrategicMove():
	""" Returns a tile number from the set of unchecked tiles
	using some rules.
	"""
	if globals.tile1==0 and (globals.tile2==globals.tile3==2 or globals.tile4==globals.tile7==2 or globals.tile5==globals.tile9==2): 
		return 1
	elif globals.tile2==0 and (globals.tile1==globals.tile3==2 or globals.tile5==globals.tile8==2):
		return 2
	elif globals.tile3==0 and (globals.tile1==globals.tile2==2 or globals.tile6==globals.tile9==2 or globals.tile5==globals.tile7==2):
		return 3
	elif globals.tile4==0 and (globals.tile5==globals.tile6==2 or globals.tile1==globals.tile7==2):
		return 4
	elif globals.tile5==0 and (globals.tile4==globals.tile6==2 or globals.tile2==globals.tile8==2 or globals.tile1==globals.tile9==2 or globals.tile3==globals.tile7==2):
		return 5
	elif globals.tile6==0 and (globals.tile4==globals.tile5==2 or globals.tile3==globals.tile9==2):
		return 6
	elif globals.tile7==0 and (globals.tile8==globals.tile9==2 or globals.tile1==globals.tile4==2 or globals.tile3==globals.tile5==2):
		return 7
	elif globals.tile8==0 and (globals.tile7==globals.tile9==2 or globals.tile2==globals.tile5==2):
		return 8
	elif globals.tile9==0 and (globals.tile7==globals.tile8==2 or globals.tile3==globals.tile6==2 or globals.tile1==globals.tile5==2):
		return 9

	elif globals.tile1==0 and (globals.tile2==globals.tile3==1 or globals.tile4==globals.tile7==1 or globals.tile5==globals.tile9==1): 
		return 1
	elif globals.tile2==0 and (globals.tile1==globals.tile3==1 or globals.tile5==globals.tile8==1):
		return 2
	elif globals.tile3==0 and (globals.tile1==globals.tile2==1 or globals.tile6==globals.tile9==1 or globals.tile5==globals.tile7==1):
		return 3
	elif globals.tile4==0 and (globals.tile5==globals.tile6==1 or globals.tile1==globals.tile7==1):
		return 4
	elif globals.tile5==0 and (globals.tile4==globals.tile6==1 or globals.tile2==globals.tile8==1 or globals.tile1==globals.tile9==1 or globals.tile3==globals.tile7==1):
		return 5
	elif globals.tile6==0 and (globals.tile4==globals.tile5==1 or globals.tile3==globals.tile9==1):
		return 6
	elif globals.tile7==0 and (globals.tile8==globals.tile9==1 or globals.tile1==globals.tile4==1 or globals.tile3==globals.tile5==1):
		return 7
	elif globals.tile8==0 and (globals.tile7==globals.tile9==1 or globals.tile2==globals.tile5==1):
		return 8
	elif globals.tile9==0 and (globals.tile7==globals.tile8==1 or globals.tile3==globals.tile6==1 or globals.tile1==globals.tile5==1):
		return 9

	elif (globals.tile5 == 0):
		return 5
	elif (globals.tile5 != 0 and globals.tile1==globals.tile3==globals.tile7==globals.tile9==0):
		move = rn.randint(1,4)
		if (move == 1):
			return 1
		elif (move ==2):
			return 3
		elif (move ==3):
			return 7
		else:
			return 9

	elif (globals.tile3==globals.tile8==1 or globals.tile7==globals.tile6==1) and globals.tile9==0:
		return 9
	elif (globals.tile1==globals.tile8==1 or globals.tile9==globals.tile4==1) and globals.tile7==0:
		return 7
	elif (globals.tile3==globals.tile4==1 or globals.tile7==globals.tile2==1) and globals.tile1==0:
		return 1
	elif (globals.tile9==globals.tile2==1 or globals.tile1==globals.tile6==1) and globals.tile3==0:
		return 3

	elif (globals.tile1 == globals.tile9 == 0):
		move = rn.randint(1,2)
		if (move == 1):
			return 1
		else:
			return 9
	elif (globals.tile3 == globals.tile7 == 0):
		move = rn.randint(1,2)
		if (move == 1):
			return 3
		else:
			return 7
	elif (globals.tile2 == globals.tile8 == 0):
		move = rn.randint(1,2)
		if (move == 1):
			return 2
		else:
			return 8
	
	elif (globals.tile4 == globals.tile6 == 0):
		move = rn.randint(1,2)
		if (move == 1):
			return 4
		else:
			return 6
	
	elif (globals.tile1==0 and globals.tile2==0):
		move = rn.randint(1,2)
		if (move == 1):
			return 1
		else:
			return 2
	elif (globals.tile2==0 and globals.tile3==0):
		move = rn.randint(1,2)
		if (move == 1):
			return 2
		else:
			return 3
	elif (globals.tile3==0 and globals.tile6==0):
		move = rn.randint(1,2)
		if (move == 1):
			return 3
		else:
			return 6
	elif (globals.tile6==0 and globals.tile9==0):
		move = rn.randint(1,2)
		if (move == 1):
			return 6
		else:
			return 9
	elif (globals.tile9==0 and globals.tile8==0):
		move = rn.randint(1,2)
		if (move == 1):
			return 9
		else:
			return 8
	elif (globals.tile8==0 and globals.tile7==0):
		move = rn.randint(1,2)
		if (move == 1):
			return 8
		else:
			return 7
	elif (globals.tile7==0 and globals.tile4==0):
		move = rn.randint(1,2)
		if (move == 1):
			return 7
		else:
			return 4
	elif (globals.tile1==0 and globals.tile4==0):
		move = rn.randint(1,2)
		if (move == 1):
			return 1
		else:
			return 4

def validBoard():
	""" Return True if board state is valid.
		
		A board state is valid if number of ticks by player1 is always either equal to or one more than the ticks by player2.
	"""
	count_player1 = 0 					# counting number of turns of player 1
	count_player2 = 0					# counting number of turns of player 2
	if globals.tile1 == 1:
		count_player1 += 1
	elif globals.tile1 ==2 :
		count_player2 += 1

	if globals.tile2 == 1:
		count_player1 += 1
	elif globals.tile2 ==2 :
		count_player2 += 1

	if globals.tile3 == 1:
		count_player1 += 1
	elif globals.tile3 ==2 :
		count_player2 += 1

	if globals.tile4 == 1:
		count_player1 += 1
	elif globals.tile4 ==2 :
		count_player2 += 1

	if globals.tile5 == 1:
		count_player1 += 1
	elif globals.tile5 ==2 :
		count_player2 += 1

	if globals.tile6 == 1:
		count_player1 += 1
	elif globals.tile6 ==2 :
		count_player2 += 1

	if globals.tile7 == 1:
		count_player1 += 1
	elif globals.tile7 ==2 :
		count_player2 += 1

	if globals.tile8 == 1:
		count_player1 += 1
	elif globals.tile8 ==2 :
		count_player2 += 1

	if globals.tile9 == 1:
		count_player1 += 1
	elif globals.tile9 ==2 :
		count_player2 += 1

	if count_player1==count_player2 or count_player1==count_player2 + 1:
		return True
	else:
		return False

def game(gametype=1):
	""" Returns 1 if player1 wins and 2 if player2 wins
		and 0 if it is a draw.
	
		gametype defines three types of games discussed above.
		i.e., game1, game2, game3
	"""
	while True:
		if (globals.turn == globals.player1):
			if (gametype == 1 or gametype == 2):
				valid_move = validmove(takeNaiveMove())
			elif (gametype == 3):
				valid_move = validmove(takeStrategicMove())

			while valid_move == False:
				if(gametype == 1 or gametype == 2):
					valid_move=validmove(takeNaiveMove())
				elif (gametype == 3):
					valid_move = validmove(takeStrategicMove())
			assert validBoard(),'the game is not honest. someone cheated'
			globals.turn = globals.player2
			game_result = win()
			if (game_result == True):
				return 1
			elif (not globals.tile1 == 0) and (not globals.tile2 == 0) and (not globals.tile3 == 0) and (not globals.tile4 == 0) and (not globals.tile5 == 0) and (not globals.tile6 == 0) and (not globals.tile7 == 0) and (not globals.tile8 == 0) and (not globals.tile9 == 0):
				return 0
		else:
			if (gametype == 3 or gametype == 2):
				valid_move = validmove(takeStrategicMove())
			elif (gametype == 1):
				valid_move = validmove(takeNaiveMove())

			while valid_move == False:
				if(gametype == 3 or gametype == 2):
					valid_move=validmove(takeStrategicMove())
				elif (gametype == 1):
					valid_move = validmove(takeNaiveMove())
			assert validBoard(),'the game is not honest. someone cheated'
			globals.turn = globals.player1
			game_result = win()
			if (game_result == True):
				return 2
			elif (not globals.tile1 == 0) and (not globals.tile2 == 0) and (not globals.tile3 == 0) and (not globals.tile4 == 0) and (not globals.tile5 == 0) and (not globals.tile6 == 0) and (not globals.tile7 == 0) and (not globals.tile8 == 0) and (not globals.tile9 == 0):
				return 0


def game1(n):
	""" Returns the winning probability for player1. 
	
	n games are played between two naive players. Estimate probability of winning for player1. Assume player1 starts the game.
	"""
	isinstance(n,int),"argument 'n' is an integer. please enter valid input"
	assert n>=0,"input should not be negative"
	win_player1 = 0
	win_player2 = 0
	draw = 0
	for i in range(n):
		game_result = game(1)
		if (game_result == 1):
			win_player1 += 1
		set_variables()
	prob = win_player1/n
	return prob

def game2(n):
	"""Returns the winning probability for player1.
	
	n games are played between a naive and intelligent player. Estimate probability of winning for player1. Assume player1 is naive and starts the game.
	"""
	isinstance(n,int),"argument 'n' is an integer. please enter valid input"
	assert n>=0,"input should not be negative"
	win_player1 = 0
	win_player2 = 0
	draw = 0
	for i in range(n):
		game_result = game(2)
		if (game_result == 1):
			win_player1 += 1
		set_variables()
	prob = win_player1/n
	return prob

def game3(n):
	"""Returns the winning probability for player1. 
	
	n games are played between two intelligent players. Estimate probability of winning for player1. Assume player1 starts the game.
	"""
	isinstance(n,int),"argument 'n' is an integer. please enter valid input"
	assert n>=0,"input should not be negative"
	win_player1 = 0
	win_player2 = 0
	draw = 0
	for i in range(n):
		game_result = game(3)
		if (game_result == 1):
			win_player1 += 1
		set_variables()
	prob = win_player1/n
	return prob