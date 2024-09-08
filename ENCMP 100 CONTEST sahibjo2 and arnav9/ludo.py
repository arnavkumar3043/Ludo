# LUDO GAME
#
# This is an Entry for ENCMP 100 's Optional Coding Contest for Winter 2024.
# This is a ludo game which is inspired by the board game Ludo
#
# It was developed by:
#    
# Sahibjot Singh: sahibjo2
# Arnav Kumar: arnav9
#
# Everything that was used to develop this program is limited to the course content.
    
import matplotlib.pyplot as plt
import random

img = plt.imread("images/board.jpg")
diceImg1 = plt.imread("images/dice5.png")
colors = ["Blue", "Red", "Green", "Yellow"]
winnerCrown =  plt.imread("images/1.png")
runnerCrown =  plt.imread("images/2.png")

# Welcome Screen
fig, ax = plt.subplots()
ax.imshow(img, extent=[0, 90, 0, 90])
plt.title("Welcome To Ludo")
plt.xticks([])
plt.yticks([])
plt.show()

#Coordinate Data
xCoordRed = [24,13.5,24,13.5]
yCoordRed = [76,76,66.5,66.5]
xCoordGreen = [65.6,76,65.6,76]
yCoordGreen = [76,76,66.5,66.5]
xCoordBlue = [24,13.5,24,13.5]
yCoordBlue = [15,15,24,24]
xCoordYellow = [65.6,76,65.6,76]
yCoordYellow = [15,15,24,24]
#Gives the "default" x and y coordinates for the markers/peices seen above
baseX = [xCoordBlue, xCoordRed, xCoordGreen, xCoordYellow]
baseY = [yCoordBlue, yCoordRed, yCoordGreen, yCoordYellow]
titleCoordinates = [[12,12,65,65],[3,55,55,3]]
#coordinates for the title
legalX = [39,39,39,39,39,39,33.3,27.6,21.9,16.2,10.5,4.5,4.5,4.5,10.5,16.2,21.9,27.6,33.3,39,39,39,39,39,39,44.7,50.4,50.4,50.4,50.4,50.4,50.4,56.1,61.8,67.5,73.2,78.9,84.6,84.6,84.6,78.9,73.2,67.5,61.8,56.1,50.4,50.4,50.4,50.4,50.4,50.4,44.7,39]
legalY = [4.5,10.2,15.9,21.6,27.3,33,39.3,39.3,39.3,39.3,39.3,39.3,45,50.7,50.7,50.7,50.7,50.7,50.7,56.8,62.1,67.8,73.5,79.2,85.5,85.5,85.5,79.2,73.5,67.8,62.1,56.8,50.7,50.7,50.7,50.7,50.7,50.7,45,39.3,39.3,39.3,39.3,39.3,39.3,33,27.3,21.6,15.9,10.2,4.5,4.5,4.5]
#Gives us the legal positionaing for the peices (white spaces)
allLegalX = [legalX[1:52],legalX[14:53] + legalX[1:13], legalX[27:53] + legalX[1:26], legalX[40:53] + legalX[1:39]]
allLegalY = [legalY[1:52],legalY[14:53] + legalY[1:13], legalY[27:53] + legalY[1:26], legalY[40:53] + legalY[1:39]]
#Gives the legal coordinates for each specific player (player 1,2, etc) These are so that
# the color tiles outside of the home are not allowed to be crossed by the other colors(i.e the ones leading to the center)
#Gives
redHomeX = [10.5,16.2,21.9,27.6,33.3,39,39,39,39]
redHomeY = [45,45,45,45,45,48,46,44,42]
yellowHomeX = [78.9,73.2,67.5,61.8,56.1,50.4,50.4,50.4,50.4]
yellowHomeY = [45,45,45,45,45,48,46,44,42]
greenHomeX = [44.7,44.7,44.7,44.7,44.7,42,44,46,48]
greenHomeY = [79.2,73.5,67.8,62.1,56.8,50.7,50.7,50.7,50.7]
blueHomeX = [44.7,44.7,44.7,44.7,44.7,42,44,46,48]
blueHomeY = [10.2,15.9,21.6,27.3,33,39.3,39.3,39.3,39.3]
homeRowX = [blueHomeX, redHomeX, greenHomeX, yellowHomeX]
homeRowY = [blueHomeY, redHomeY, greenHomeY, yellowHomeY]
#Gives the home column (i.e the part leading to the center and the center)
crownCoordinates = [[8, 32, 8, 32], [8, 32, 58, 82], [60, 84, 58, 82], [60, 84, 8, 32]]
#Where the crown is going to be put if there is a winner there
safeX = blueHomeX + redHomeX + greenHomeX + yellowHomeX + [legalX[1],legalX[9],legalX[14],legalX[22],legalX[27],legalX[35],legalX[40],legalX[48]]
safeY = blueHomeY + redHomeY + greenHomeY + yellowHomeY + [legalY[1],legalY[9],legalY[14],legalY[22],legalY[27],legalY[35],legalY[40],legalY[48]]
#Spots where the peice cannot be captured
#Gives coordinates where pieces cannot be captured
def getSafeCoordinates(safeX, safeY):
    safe_coordinates = []

    for x, y in zip(safeX, safeY):
        safe_coordinates.append((x, y))
    #creates a list of tuples with 44 total pairs giving the total safe coordinates
    return safe_coordinates
safeCoordinates = getSafeCoordinates(safeX, safeY)

#Checks if Given coordinate is a safe house
def checkSafeHouse(x, y): #Function to check if the peice is safe
    if (x, y) in safeCoordinates:
        return True
    return False


winners = []

# A function that presents the menu an returns the response
def menu():
    print()
    print("MAIN MENU")
    print("Choose from Menu")
    print("1. About Game")
    print("2. Instructions")
    print("3. Play Game")
    print("4. Exit")
    print()
    Proper_Response=False 
    while Proper_Response==False: #Forces User to give a proper response 
        try:
            choice = int(input("Choice (1-4)? "))
            while not (1 <= choice <= 4):
                choice = int(input("Choice (1-4)? "))
            return choice
        except:
            print("Give one of the following Values: (1,2,3,4).")
            continue
    

#This function does the initial setup of the game, it creates pieces as dictionaries, assignes them path and other properties.
def initiateBoard(players):
    newPlayers = []
    currPlayer = 0
    for player in players:
        newPlayer = []
        newPlayer.append(player[0])
        currPiece = 0
        for j in ['A', 'B', 'C', 'D']:
            piece = {
                "name": j,
                "xPath": [baseX[currPlayer][currPiece]] + allLegalX[currPlayer] + homeRowX[currPlayer][0:5]  + [homeRowX[currPlayer][currPiece+5]],
                "yPath": [baseY[currPlayer][currPiece]] + allLegalY[currPlayer] + homeRowY[currPlayer][0:5]  + [homeRowY[currPlayer][currPiece+5]],
                #Gives the path for the peice based on the player number and the peice number(peice 
                #number's only difference is initial position, and final position(i.e left and right wise))
                "currPos": 0, 
                "x": baseX[currPlayer][currPiece],
                "y": baseY[currPlayer][currPiece],
                "isSafe": True,
                "isAtBase": True,
                "isAtHome": False,
                "color": colors[currPlayer]
                }#initializes all the varialbes for the code
            newPlayer.append(piece)
            currPiece = currPiece + 1
        newPlayers.append(newPlayer)
        currPlayer = currPlayer + 1 
    return newPlayers #Returns all dict values in one in a list(players) of list(peice) of form [name, dict1,dict2, etc]

#This function prints a new matplotlib ludo plot based on current state of game. 
def updateBoardState(players, currentPlayer, dice, legalMoves):
    fig, ax = plt.subplots()
    ax.imshow(img, extent=[0, 90, 0, 90])
    if not dice:
        #If dice is None
        plt.title("It's %s 's Turn" %players[currentPlayer][0])
    else:
        url = "images/dice"+str(dice)+".png"
        diceImg = plt.imread(url)
        ax.imshow(diceImg, extent=[0, 6, 0, 6])
        plt.title("It's a "+str(dice))
        
    
    for i in range(len(winners)): #Gives the crown for the winner
        if i == 0:
            ax.imshow(winnerCrown, extent=crownCoordinates[winners[i]])
        if i == 1:
            ax.imshow(runnerCrown, extent=crownCoordinates[winners[i]])
    numPlayer = 0
    for player in players:
        for piece in player[1:]: #Ignores first one as that is the name
            plt.scatter(piece["x"], piece["y"], marker='o', color=piece["color"], edgecolor='black', s=60)
            if dice and numPlayer == currentPlayer and piece["name"] in legalMoves:
                #Checks if dice has a value and checks if the num_player=current_player
                #and if the move is in legal moves where legal moves is the list of peices that can move
                plt.text(piece["x"], piece["y"], piece["name"], fontsize=10)
        plt.text(titleCoordinates[0][numPlayer], titleCoordinates[1][numPlayer], player[0], fontsize=10)
        numPlayer = numPlayer + 1
    plt.xticks([])
    plt.yticks([])
    
    plt.show()
    plt.close()
    #overall just displays the graph/board

#This function represents rolling the dice. It returns a random value between 1 and 6
def roll_dice(playerName):
    print("It's %s 's Turn" %playerName )
    keyPress = input("Press anything to roll dice")
    dice = random.randint(1, 6)
    print()
    print("It's a ",dice)
    return dice

#This function prompts the user to select a move based on possible moves.
def get_move(legalMoves):
    move = ""
    while move not in legalMoves:
        print("Choose one of the following:",legalMoves)
        move = input("Select Piece to Move ").upper()
    return move

#This function is heart of our program. It updates the state of board (players variable) based on current state, current player his move and number on dice. It updates the state while checking for rules, eliminations and checking if game is towards ending.
def move_piece(players, move, currentPlayer, dice):
    newPlayers = players
    for i in range(0,len(players)):
        numIn = 0
        if currentPlayer == i: #checks if we are moving the right peice
            for j in range(1,5): #Checks for each peice
                if newPlayers[i][j]["name"] == move: #Note move is the name of the peice A,B, etc
                    if newPlayers[i][j]["isAtBase"] :
                        newPlayers[i][j]["isAtBase"] = False
                        #Updates the value as the value of a peice that is moving cannout be at base(i.e only in the case of a six)
                        newPlayers[i][j]["currPos"] += 1 #Moves it outside
                    else:
                        newPlayers[i][j]["currPos"] +=  dice #Else it moves it the value of the dice i.e if it is not at base
                    newPlayers[i][j]["x"] = newPlayers[i][j]["xPath"][newPlayers[i][j]["currPos"]]
                    newPlayers[i][j]["y"] = newPlayers[i][j]["yPath"][newPlayers[i][j]["currPos"]]
                    #updates the value as the list[position]
                    
                    if(not checkSafeHouse(newPlayers[i][j]["x"], newPlayers[i][j]["y"])):
                        
                        numOccupied =  0 
                        
                        occupied = []
                        currX = newPlayers[i][j]["x"]
                        currY = newPlayers[i][j]["y"]
                        
                        for n in range(0,len(players)):
                            for o in range(1,5):
                                name = players[n][o]["name"]
                                x = players[n][o]["x"] 
                                y = players[n][o]["y"]
                                #x and y position
                                
                                if currX == x and currY == y: 
                                    if currentPlayer == n:
                                        # checks if there is a peice already 
                                        #occupying it by iterating through every one
                                        break
                                    else :
                                        numOccupied += 1
                                        occupied.append([n,o,name])
                                             
                        if numOccupied == 1:
                            for occupants in occupied:
                                newPlayers[occupants[0]][occupants[1]]["isAtBase"] = True
                                newPlayers[occupants[0]][occupants[1]]["currPos"] = 0
                                newPlayers[occupants[0]][occupants[1]]["x"] =  newPlayers[occupants[0]][occupants[1]]["xPath"][0]
                                newPlayers[occupants[0]][occupants[1]]["y"] =  newPlayers[occupants[0]][occupants[1]]["yPath"][0]
                                #Moves the peice to the 0 spot if it has been "taken"
                    if newPlayers[i][j]["currPos"] >= 57: #checks if the peice has completed its run
                        newPlayers[i][j]["isAtHome"] = True
                if newPlayers[i][j]["isAtHome"]:
                    numIn += 1
        if numIn == 4 and i not in winners:
            winners.append(i)
    return newPlayers

#This function checks if current player can make any legal move using the number given on dice.
def getLegalMoves(players,dice, currentPlayer):
    currPlayerObj = players[currentPlayer]
    legalMoves = []
    
    for piece in currPlayerObj[1:]:
        #Check if at Base and Unlocked
        if(piece["isAtBase"] and dice != 6):
            continue
        #Check if at Home 
        if(piece["isAtHome"]):
            continue
        #Check if dice will exceed Home
        if(piece["currPos"] + dice >= len(piece["xPath"])):
            continue
        legalMoves.append(piece["name"])
    return legalMoves


#This function uses all of the above defined functions to lay a general setup of the program.
def main():
    global winners
    print("Welcome To Ludo")
    choice = menu()
    
    while choice != 4:
        if choice == 1:
            about = open('text/about.txt','r')
            print(about.read())
            #prints the file about the game
        elif choice == 2:
            rules = open('text/rules.txt','r')
            print(rules.read())
            #prints the rules of the game
        elif choice == 3:
            numPlayers = 0
            winners = []
            while not (2 <= numPlayers <= 4):
                try:
                    numPlayers = int(input("Number of Players (2-4)? "))
                except:
                    print("Give one of the following (2.3, or 4")
                    continue
            players = []
            
            for i in range(0,numPlayers):
                tempName = ""
                while not (len(tempName) > 0):
                    tempName = input("Enter %s Player's Name " % colors[i])
                    players.append([tempName])
                    #Gives a name for each player saved as temp name
            players = initiateBoard(players) #Gives all the initial information about the players
            
            
            currentPlayer = 0 # 0: Blue, 1: Red, 2: Green, 3: Yellow
            updateBoardState(players, currentPlayer, None, None)#Gives the initial board
            
            everyoneGotIn = False #sets it so that it chekcs if the game is over
            
            while not (everyoneGotIn):
                if currentPlayer==winners:
                    currentPlayer = 0 if currentPlayer == numPlayers - 1 else currentPlayer + 1
                    continue
                dice = roll_dice(players[currentPlayer][0]) #argument is player name
                legalMoves = getLegalMoves(players, dice, currentPlayer)#gets the peices that can move [A,B,C etc]
                if not legalMoves:
                    print("No Possible Move for You")
                    if dice != 6:
                        currentPlayer = 0 if currentPlayer == numPlayers - 1 else currentPlayer + 1
                    updateBoardState(players, currentPlayer, None, None)
                    continue
                
                updateBoardState(players, currentPlayer, dice, legalMoves)
                move = get_move(legalMoves)
                players = move_piece(players, move, currentPlayer, dice)
                if dice !=6:
                    currentPlayer = 0 if currentPlayer == numPlayers - 1 else currentPlayer + 1
                updateBoardState(players, currentPlayer, None, None)
                
                everyoneGotIn = sum(all(piece["isAtHome"] for piece in player[1:]) for player in players) == len(players) - 1

                
                if everyoneGotIn:
                    print()
                    print("GAME OVER")
                    print("Results")                    
                    for i in range(len(players) - 1 ):
                        if i == 0:
                            print(players[winners[i]][0],"won the Game")
                        if i == 1:
                            print(players[winners[i]][0],"was the runner up")
                        if i == 2:
                            print(players[winners[i]][0],"came third")
        choice = menu()
    
main()