#Displays a summary onto the screen describing what the program does.
print("Welcome to the Tic-Tac-Toe game. You will play as Player X against the computer Player O and compete to get three in a row on the board first. I warn you that it is almost impossible to win against the bot. Thanks to the MINMAX function, this gives Player O (the bot) an advantage making it almost unbeatable. Can you beat the bot? Lets find out.")

#Initializing boardspaces that will be in the layout board
#with numbers, showing the user where they can make moves.
boardspaces = {1: '1', 2: '2', 3: '3',
         4: '4', 5: '5', 6: '6',
         7: '7', 8: '8', 9: '9'}

#Function definition Layout with parameter boardspaces that will
#display a board with numbers in them, showing where the user can make moves.
def Layout(boardspaces):
    print('------- ' + '\n|' + boardspaces[1] + '|' + boardspaces[2] + '|' + boardspaces[3] + '|' + '\n--+-+--')
    print('|' + boardspaces[4] + '|' + boardspaces[5] + '|' + boardspaces[6] + '|' + '\n--+-+--') 
    print('|' + boardspaces[7] + '|' + boardspaces[8] + '|' + boardspaces[9] + '|' + '\n------- ')

#Function call to display board 
#with numbers in each space
Layout(boardspaces)

#Initializing the actual gameboard with all
#the spaces (1-9) left initially blank.
board = {1: ' ', 2: ' ', 3: ' ',
         4: ' ', 5: ' ', 6: ' ',
         7: ' ', 8: ' ', 9: ' '}

#Function definition displayBoard with parameter board
def displayBoard(board):
    print('------- ' + '\n|' + board[1] + '|' + board[2] + '|' + board[3] + '|' + '\n--+-+--')
    print('|' + board[4] + '|' + board[5] + '|' + board[6] + '|' + '\n--+-+--') 
    print('|' + board[7] + '|' + board[8] + '|' + board[9] + '|' + '\n------- ')

#Displays a blank gameboard 
#onto the screen.
displayBoard(board)

#Function Definition availableSpace 
#with parameter spacet to check and see
#if the space is taken.
def availableSpace(space):
    
    #When the space is blank.
    if(board[space]== ' '):
        
        #Return True.
        return True
    
    #Otherwise...    
    else:

        #Returns False.
        return False

#Function Definition tie to 
#determine if there is a tie.
def Tie():

    #Counting loop going through every key in board.
    for key in board.keys():
        
        #When the key space is blank.
        if board[key] == ' ':
            
            #Returns False.
            return False 
    #Return True.
    return True

#Function Definition win to check
#if there are any winning scenarios.
def win():
    
    #All the scenarios of how 3 in a row win can happen.
    
    #When the player makes three in a row with board spaces 1, 2, and 3.
    if(board[1] == board[2] and board[1] == board[3] and board[1] != ' '):
        
        #Return True.
        return True
    
    #When the player makes three in a row with board spaces 4, 5, and 6.
    elif(board[4] == board[5] and board[4] == board[6] and board[4] != ' '):
        
        #Return True.
        return True
    
    #When the player makes three in a row with board spaces 7, 8, and 9.
    elif(board[7] == board[8] and board[7] == board[9] and board[7] != ' '):
        
        #Return True.
        return True
    
    #When the player makes three in a row with board spaces 1, 4, and 7.
    elif(board[1] == board[4] and board[1] == board[7] and board[1] != ' '):
        
        #Return True.
        return True
    
    #When the player makes three in a row with board spaces 2, 5, and 8.
    elif(board[2] == board[5] and board[2] == board[8] and board[2] != ' '):
        
        #Return True.
        return True
    
    #When the player makes three in a row with board spaces 3, 6, and 9.
    elif(board[3] == board[6] and board[3] == board[9] and board[3] != ' '):
        
        #Return True.
        return True
    
    #When the player makes three in a row with board spaces 1, 5, and 9.
    elif(board[1] == board[5] and board[1] == board[9] and board[1] != ' '):
        
        #Return True.
        return True
    
    #When the player makes three in a row with board spaces 3, 5, and 7.
    elif(board[7] == board[5] and board[7] == board[3] and board[7] != ' '):
        
        #Return True.
        return True
    
    #Otherwise...
    else:
        
        #Return False.
        return False

#Function Definition whoWon to check
#if there are any winning scenarios with 
#the most recent mark a player entered.
def whoWon(mark):

    #When the player or bot places a mark to make three in a row with board spaces 1, 2, and 3.
    if(board[1] == board[2] and board[1] == board[3] and board[1] == mark):
        
        #Return True.
        return True
    
    #When the player or bot places a mark to make three in a row with board spaces 4, 5, and 6.
    elif(board[4] == board[5] and board[4] == board[6] and board[4] == mark):
        
        #Return True.
        return True
    
    #When the player or bot places a mark to make three in a row with board spaces 7, 8, and 9.
    elif(board[7] == board[8] and board[7] == board[9] and board[7] == mark):
        
        #Return True.
        return True
    
    #When the player or bot places a mark to make three in a row with board spaces 1, 4, and 7.
    elif(board[1] == board[4] and board[1] == board[7] and board[1] == mark):
        
        #Return True.
        return True
    
    #When the player or bot places a mark to make three in a row with board spaces 2, 5, and 8.
    elif(board[2] == board[5] and board[2] == board[8] and board[2] == mark):
        
        #Return True.
        return True
    
    #When the player or bot places a mark to make three in a row with board spaces 3, 6, and 9.
    elif(board[3] == board[6] and board[3] == board[9] and board[3] == mark):
        
        #Return True.
        return True
    
    #When the player or bot places a mark to make three in a row with board spaces 1, 5, and 9.
    elif(board[1] == board[5] and board[1] == board[9] and board[1] == mark):
        
        #Return True.
        return True
    
    #When the player or bot places a mark to make three in a row with board spaces 3, 5, and 7.
    elif(board[7] == board[5] and board[7] == board[3] and board[7] == mark):
        
        #Return True.
        return True
    
    #Otherwise...
    else:

        #Return False.
        return False  

#Function Definition for makeMove
#so that either the player or bot
#can make and set their space.
def makeMove(letter, space):
    
    #When there is a space available.
    if availableSpace(space):

        #Sets a space with the players or bots letter.
        board[space] = letter

        #Displays an updated gameboard with the most
        #recent move made by either the player or the bot.
        displayBoard(board)

        #When there is a tie.
        if(Tie()):

            #Displays a message onto the screen 
            #saying no one won and the game is
            #a tied.
            print("It's a tie!")

            #Displays a message onto the screen asking the user if they want to play another round.
            response = input("Would you like to play another round?: ")

            #A while loop for when there is a tie.
            while Tie():

                #When the user wants to keep playing.
                if response == "yes":

                    #Displays a board with the numbers showing
                    #where players can make moves.
                    Layout(boardspaces)

                    #Clears the entire board for another round.
                    board[1] = board[2] =board[3] = board[4] =  board[5] = board[6] = board[7] = board[8] = board[9] = ' '
                    
                    #Displays a new blank board for the new round.
                    displayBoard(board)
                
                #When the user is done playing.   
                elif response == "no":

                    #Displays a message onto the screen telling the user thanks for playing
                    #and hopes they come back to play some more.
                    print("Thanks for playing. Hope you play again soon.")

                    #Ending the app.
                    exit()
                
                #Otherwise...
                else:

                    #Telling the user that they need to enter a yes to continue playing or no to quit.
                    response = input("Enter either yes to play another round or no to quit: ")

        #When there is a winner.
        if win():

            #When the computer wins.
            if letter == 'O':
                
                #Displays a message onto the screen telling
                #the human player the opponent, the bot won.
                print("Bot wins!")

                #Displays a message onto the screen asking the user if they want to play another round.
                response = input("Would you like to play another round?: ")

                #A while loop for when there is a winner.
                while win():

                    #When the user wants to keep playing.
                    if response == "yes":

                        #Displays a board with the numbers showing
                        #where players can make moves.
                        Layout(boardspaces)

                        #Clears the entire board for another round.
                        board[1] = board[2] =board[3] = board[4] =  board[5] = board[6] = board[7] = board[8] = board[9] = ' '
                        
                        #Displays a new blank board for the new round.
                        displayBoard(board)
                    
                    #When the user is done playing.
                    elif response == "no":

                        #Displays a message onto the screen telling the user thanks for playing
                        #and hopes they come back to play some more.
                        print("Thanks for playing. Hope you play again soon.")
                        
                        #Ending the app.
                        exit()

                    #Otherwise...
                    else:
                        
                        #Telling the user that they need to enter a yes to continue playing or no to quit.
                        response = input("Enter either yes to play another round or no to quit: ")
            
            #Otherwise...
            else:

                #Displays a message onto the screen 
                #telling the user they won.
                print("Player wins!")

                #Displays a message onto the screen asking the user if they want to play another round.
                response = input("Would you like to play another round?: ")

                #A while loop for when there is a winner.
                while win():
                    
                    #When the user wants to keep playing.
                    if response == "yes":
                        
                        #Displays a board with the numbers showing
                        #where players can make moves.
                        Layout(boardspaces)

                        #Clears the entire board for another round.
                        board[1] = board[2] =board[3] = board[4] =  board[5] = board[6] = board[7] = board[8] = board[9] = ' '
                        
                        #Displays a new blank board for the new round.
                        displayBoard(board)

                    #When the user is done playing.    
                    elif response == "no":
                        
                        #Displays a message onto the screen telling the user thanks for playing
                        #and hopes they come back to play some more.
                        print("Thanks for playing. Hope you play again soon.")
                        
                        #Ending the app.
                        exit()
                    
                    #Otherwise...
                    else:

                        #Telling the user that they need to enter a yes to continue playing or no to quit.
                        response = input("Enter either yes to play another round or no to quit: ")
        #Return
        return
    
    #Otherwise...
    else:

        #Displays a message onto the screen telling the
        #user the space has already been marked.
        print("The space has already been marked!")

        #Allows the user to pick another space.
        space = int(input("Pick another space:"))
        
        #So the player can make and set 
        #their move on the board.
        makeMove(letter, space)
        
        #Returns the move.
        return

#Initializing player (the human player) with 
#their letter being X.
player = 'X'

#Initializing the computer player (the opponent) 
#with their letting being O.
computer = 'O'

#Function Definition for the player
#to make their move in the game.
def playersChoice():
    
    #Allows the human player to make a move, by entering a number 1-9.
    space = int(input("It's your turn Player X. Enter a space (1-9): "))

    #Sets the players move.
    makeMove(player, space)

    #Returns players choice.
    return

#Function Definition for the computer
#player to make its own move in the game.
def computersChoice():

    #bestScore is -1000.
    bestScore = -1000

    #bestMove is 0.
    bestMove = 0

    #Counting loop going through every key in board.
    for key in board.keys():

        #When board[key] space is blank.
        if(board[key]== ' '):

            #Initializing board[key] to computer.
            board[key] = computer

            #Initializing score to MINMAX function call
            #with parameters board, 0 and False.
            score = MINMAX(board, 0, False)

            #Initializing board[key] to blank space.
            board[key] = ' '

            #When score is greater than the bestScore.
            if(score > bestScore):

                #Initializing bestScore to score.
                bestScore = score

                #Initializing bestMove to key.
                bestMove = key
    
    #Calling makeMove function with 
    #parameters computer and bestMove,
    makeMove(computer, bestMove)
    
    #Returns
    return

#Function Definition MINMAX with parameters board, depth
#and isMaximizing, which will make the computer player 
#unbeatable or extremely hard to beat and rarely win against.
def MINMAX(board, depth, isMaximizing):
    
    #If the computer player wins...
    if whoWon(computer):
        return 100
    
    #If the human player wins...
    elif whoWon(player):
        return -100
    
    #Otherwise if it's a tie...
    elif Tie():
        return 0
    
    #When isMaximizing...
    if isMaximizing:

        #bestScore is -1000.
        bestScore = -1000

        #Counting loop going through every key in board.
        for key in board.keys():

            #When board[key] space is blank.
            if(board[key]== ' '):

                #Initializing board[key] to computer.
                board[key] = computer
                
                #Initializing score to MINMAX function call
                #with parameters board, 0 and False.
                score = MINMAX(board, 0, False)
                
                #Initializing board[key] to blank space.
                board[key] = ' '
                
                #When score is greater than the bestScore.
                if(score > bestScore):
                    
                    #Initializing bestScore to score.
                    bestScore = score

        #Returns the bestScore
        return bestScore
    
    #Otherwise...
    else:
        
        #bestScore is 800.
        bestScore = 800
        
        #Counting loop going through 
        #every key in board.
        for key in board.keys():

            #When board[key] space is blank.
            if(board[key]== ' '):

                #Initializing board[key] to player.
                board[key] = player

                #Initializing score to MINMAX function call
                #with parameters board, 0 and True.
                score = MINMAX(board, 0, True)

                #Initializing board[key] to blank space.
                board[key] = ' '

                #When score is less than the bestScore.
                if(score < bestScore):

                    #Initializing bestScore to score.
                    bestScore = score

        #Returns bestScore            
        return bestScore

#Creating a while loop 
#with no winner yet and
#the game is still going.
while not win():
    
    #Having the human player make the next move.
    playersChoice()
    
    #Having the computer player make a move 
    #after the human player.
    computersChoice()

