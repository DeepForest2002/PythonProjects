import random
#game variables
run=True
mine= False
numCount=0
mainlist=[] #Main board for the game
minelist=[] #Mine list of the game
print('''It is a board, so enter your board size in a single number like,
    3 for 3*3 = 9 box board
    4 for 4*4= 16 box board''')
board_size= int(input("Enter your board size:"))
#n= number of mines
n=int((board_size**2)*(0.25))
#Creating the list of mines
a1= random.sample(range(board_size),n)
a2=random.sample(range(board_size),n)
for i in range(n):
    minelist.append((a1[i], a2[i]))
#Creating mainlist for the game
mainlist=[['_' for i in range(board_size)]for j in range(board_size)]
print(minelist) #This is for the location of the mines present in the board
#Now we are gonna create the function that keeeps track the current status of the board
def CurrentStatus(board_size, mainlist):
    print("Current status of the board is: \n")
    for i in range(-1,board_size):
        if i==-1:
            print(" ", end=" ") #if there is nothing on the board
        else:
            print(i, end=" ") #If there is a number on the board
            continue
    
    #Checking if there is a mine on the list or not??
    for i in range(board_size):
        print(i, end=" ")
        for j in range(board_size):
            print(mainlist[i][j], end=" ")
        print("\n")
#Now lets create the main function of the gamne
print('''Here starts your minseepper game ''')
while(run): 
    CurrentStatus(board_size, mainlist)#Calling the function
    #user input for selection of row and columns 
    row=int(input("Enter the row number"))
    col=int(input("Enter the col number"))
    #If users choice is out of the index it will throw error
    if (row>board_size-1 or row<0 or col>board_size-1 or col<0):
        print("Error,Choose again")
        run=False
    print("\n")
    #Checking if the user select mine or not
    if ((row,col)in minelist):
        print("You loose")
        run=False
        for i in minelist:
            a=i[0]
            b=i[1]
            mainlist[a][b]='*' #This will show all the positions of mines in the list after loosing the game
    else:
        if(mainlist[row][col]=="_"):
            mainlist[row][col]= random.randint(0,9) #Putting a random number if there is no mine
            numCount+=1
        else:
            pass
#Check the user winner or not
if numCount==board_size**2-n:
    print("You win")
    run=False
else:
    pass
#Printing the final status of the board
CurrentStatus(board_size, mainlist)





