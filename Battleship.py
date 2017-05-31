from random import randint

turn_limit = 5		 	#Adjustable turn limit.
board_height = 5		#Adjustable row size.
board_width = 5			#Adjustable column size.
board = []


#Creating board layout.
for x in range(board_height):
	board.append(["O"] * board_width)


def print_board(board):
 	for row in board:
        	print " ".join(row)		#Removing commas and quotations.


print
print "Let's play Battleship!"
print "You have " + str(turn_limit) + " turns to sink my battleship!"
print


def random_row(board):
   	return randint(0, (board_height - 1))

def random_col(board):
    	return randint(0, (board_width - 1))

#Setting ship location.
ship_row = random_row(board)
ship_col = random_col(board)


#Cycling through player turns.
turn = 1
while turn <= 5:
	if turn == turn_limit:
		print 'Last turn!'
        else :
		print "Turn", str( (turn) )


	print_board(board)

	try:
     		guess_row = int(raw_input("Guess Row: ")) - 1
    	except:
		guess_row = ''
	try:
		guess_col = int(raw_input("Guess Column: ")) - 1
   	except: 
		guess_col = ''

    	if guess_row == ship_row and guess_col == ship_col:
        	print "CONGRATULATIONS! You sunk my battleship!"
 		print
		board[guess_row][guess_col] = '#'
		board[ship_row][ship_col] = '#'
	       	break
        elif guess_row == '' or guess_col == '':
            	print "Oops, didn't quite catch that.."
		print
		turn -= 1
    	elif (guess_row < 0 or guess_row > (board_height-1)) or (guess_col < 0 or guess_col > (board_width-1)):
        	print "Oops, that's not even in the ocean."
		print
		turn -= 1
   	elif(board[guess_row][guess_col] == "X"):
        	print "You guessed that one already."
  		print
		turn -= 1
	else:
        	print "You missed my battleship!"
		print
        	if turn == turn_limit-1:
			print 'Better luck next time!'
		board[guess_row][guess_col] = "X"
	
	turn += 1

print_board(board)
print 'My ship was located at Row ' + str(ship_row + 1) + " Column " + str(ship_col + 1l) + "!"

