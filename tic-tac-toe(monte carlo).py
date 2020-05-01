"""
Monte Carlo Tic-Tac-Toe Player
"""

import random
import poc_ttt_gui
import poc_ttt_provided as provided

# Constants for Monte Carlo simulator
# You may change the values of these constants as desired, but
#  do not change their names.
NTRIALS = 100         # Number of trials to run
SCORE_CURRENT = 2.0 # Score for squares played by the current player
SCORE_OTHER = 1.0   # Score for squares played by the other player

# Add your functions here.

def mc_trial(board, player):
	# game_board = board
	game_player = player
	while board.check_win() is None:
		square = random.choice(board.get_empty_squares())
		board.move(square[0], square[1], game_player)
		game_player = provided.switch_player(game_player)

	return board


def mc_update_scores(scores,board,player):
	winner = board.check_win()
	# score = []
	if winner == player:
		score = [SCORE_CURRENT, -1*SCORE_OTHER]
	elif winner == provided.switch_player(player):
		score = [-1*SCORE_CURRENT, SCORE_OTHER]
	else:
		return

	dim = range(board.get_dim())

	for row in dim:
		for col in dim:
			if board.square(row, col) == player:
				scores[row][col] += (score[0])
			else:
				scores[row][col] += (score[1])


def get_best_move(board,scores):
	empty_squares = board.get_empty_squares()
	if empty_squares == []:
		return

	max_score = scores[empty_squares[0][0]][empty_squares[0][1]]
	max_row = empty_squares[0][0]
	max_col = empty_squares[0][1]

	for square in empty_squares:
		row = square[0]
		col = square[1]
		if scores[row][col] >= max_score:
			max_score = scores[row][col]
			max_row = row
			max_col = col
		
	move_square = (max_row, max_col)
	return move_square

def mc_move(board,player,trials):
	dim = board.get_dim()
	scores = [[0 for _ in range(dim)] for _ in range(dim)]
	board_clone = board.clone()
	for trial in range(trials):
		mc_trial(board_clone, player)
		mc_update_scores(scores, board_clone, player)

	return get_best_move(board, scores)







# Test game with the console or the GUI.  Uncomment whichever 
# you prefer.  Both should be commented out when you submit 
# for testing to save time.

# provided.play_game(mc_move, NTRIALS, False)        
poc_ttt_gui.run_gui(3, provided.PLAYERX, mc_move, NTRIALS, False)
