''' Instructions:
   Work with a partner to complete these tasks. You may assume that all variables/lists are declared and initialized (unless you are specifically asked to create/initialize a list); you need only write the code using the variables/lists indicated in the description. Write your solution below the commented description.
'''

''' 1. 
   Create a list of ints, faveNums, that holds 3 integers.
'''

faveNums = [3,4,5]

''' 2. 
   Create a list of Strings, holidays, that holds 14 holidays.  
'''
holidays = ['President\'s Day','Easter','Christmas','Labor Day','Memorial Day','Hanukkah','Valentine\'s Day','New Year\'s Day','Children\'s Day', 'Martin Luther King\'s Day', 'Passover', 'Diwali','Boxing Day','Thanksgiving']


''' 3. 
   Create a list of characters, grades, that holds 5 letter grades.
'''

grades = ["A",""B,"C","D","F"]

''' 4. 
   Create a list of booleans, funny, the can keep track of whether 18 things are funny or not. 
'''

funny = [True,False,True,True,False,False,False,True,False,True,False,True,True,False,False,False,True,False,True,False,True,True,False,False,False,True,False]

''' 5. 
   Create a list of doubles, salaries, that holds the salaries of all the employees at a university. The number of employees is stored in the int numEmployees.
'''

salaries = [("John",75000)*numEmployees for i in range(numEmployees)]

''' 6. 
   A picture's dimensions are stored in integer variables x and y. Create a single list of integers that can store the grayscale value for each pixel in the list.
'''

pixels = [[0]*x for i in range(y)]

''' 7. 
   In a class, each student has 0, 1, 2 or 3 siblings. The numbers of students with no siblings is stored in the variable noSiblings, the number of students with one sibling is stored in the variable oneSibling, the number of students with two siblings is stored in the variable twoSiblings, and the number of students with three siblings is stored in the variable threeSiblings. Create a list that holds all the names of the students in the class, as well as the names of all their siblings.
'''

roster = []
total = noSiblings + oneSibling + twoSiblings + threeSibling
for i in range(noSiblings):
  roster.append([name])
for i in range(oneSiblings):                                                                                          
   roster.append([name,sibling1])
for i in range(twoSiblings):                                                                                          
   roster.append([name,sibling1,sibling2])
for i in range(threeSiblings):                                                                                          
   roster.append([name,sibling1,sibling2,sibling3])

''' 8. 
   Create a list that holds all the months in the year. (No loop.)
'''

months = ['January', 'February', 'March', 'April', 'May', 'June', 'July','August', 'September', 'October', 'November', 'December']


''' 9. 
   Create a list that holds all the days of the week. (No loop.)
'''

week = ["Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday"]

''' 10. 
   Create a list that holds all the possible values for boolean variables. (No loop.)
'''

boolean = [True,False]

''' 11. 
   Create a list that holds the names of all the 3rd form dorms on campus. (No loop.)
'''

freshmans = ["Memorial","Nichols","Pitman","Squire Stanley"]

''' 12.  
   Create a list that holds 3 random numbers with values between 0 and 1. (Loop optional.)
'''

import random
values = [random.randrange(2) for i in range(3)]

''' 13. 
   Create a list that will represent a deck of cards. Some example data for cards would be AS (ace of spaces), 5H (5 of hearts), JC (jack of clubs), 9D (9 diamonds). (Loop required.) 
'''

suits = ["S","H","C","D"]
values = ["A","2","3","4","5","6","7","8","9","10","J","Q","K"]
deck = [(v,s) for v in values for s in suits]

''' 14. 
   Write a Yahtzee program that simulates the rolling of five dice and prints "Yahtzee" if all five dice are the same; otherwise it should print "Try again."
'''

import random

def Yahtzee():
   dice = [random.randrange(1,7) for i in range(5)]
   match=0
   print(dice)
   for i in range(len(dice)):
      if i==0:
         pass
      elif dice[i]==dice[i-1]:
         match+=1
   if match == 4:
      return True
   else:
      return False

if Yahtzee():
   print("Yahtzee!")
else:
   print("Try again.")
      
''' 15. 
   In a list, specials are numbers in a list that have an even number before them, an odd number behind them, and they themselves are divisible by 3. Given a list of ints called numbers, print out the location in the list of the specials, as well as the value in front of them, their value, and the value behind them. For example:
   position 4: 14, 9, 25
'''

for i,x in enumerate(numbers):
  if i != 0:
    if x % 3 == 0:
      if numbers[i-1] % 2 == 0:
        if numbers[i+1] % 2 != 0:
          print("position",i,":",numbers[i-1],numbers[i],numbers[i+1])

''' 16. 
   Write a program to search for the "saddle points" in a 5 by 5 list of integers. A saddle point is a cell whose value is greater than or equal to any in its row, and less than or equal to any in its column. There may be more than one saddle point in the list. Print out the coordinates of any saddle points your program finds. Print out "No saddle points" if there are none.
'''

integers=[[1,1,1,1,1],[1,1,1,1,1],[1,1,1,1,1],[1,1,1,1,1],[1,1,1,1,1]]

def saddleFind(saddles):
   saddlepoints = []
   for y in range(len(saddles)):
      for x in range(len(saddles[y])):
         largerThan = 0
         smallerThan = 0
         for i in range(4):
            if saddles[y][x]>=saddles[y][x-(i+1)]:
               largerThan+=1
            if saddles[y][x]<=saddles[y-(i+1)][x]:
               smallerThan+=1
         if largerThan == 4 and smallerThan == 4:
            saddlepoints.append([x+1,y+1])
   return saddlepoints

saddlepoints = saddleFind(integers)
if saddlepoints == []:
   print("No saddle points")
else:
   print("Saddlepoints (in the form [column#,row#]): \n" + str(saddleFind(integers)))

''' 17. 
   In the game of chess, a queen can attack pieces which are on the same row, column, or diagonal. A chessboard can be represented by an 8 by 8 list. A 1 in the list represents a queen on the corresponding square, and a O in the list represents an unoccupied square. Given the two locations for queens (row1, col1, row2, col2), place the queens in the 2D list, chessboard. Then process the board and indicate whether or not the two queens are positioned so that they attack each other. 
'''
chessboard = [[0]*8 for x in range(8)]
chessboard[0][0]=1
chessboard[1][1]=1
validMove=False
moveType = ""

for y in range(8):
   queenCount=0
   for x in range(8):
      if chessboard[y][x]==1:
         queenCount+=1
   if queenCount>=2:
      validMove=True
      moveType="horizontally."

for x in range(8):
   queenCount=0
   for y in range(8):
      if chessboard[y][x]==1:
         queenCount+=1
   if queenCount>=2:
      validMove=True
      moveType="vertically."

for x in range(8):
   for y in range(8):
      queenCount=0
      for i in range(8):
         for j in range(8):
            if chessboard[x-i][y-j]==1:
               queenCount+=1
      if queenCount>=2:
         validMove=True
         moveType="diagonally."

if validMove:
   print("The two queens can attack each other "+moveType)

''' 18. 
   Given a list, write code that will reverse the order of the elements in the list. For example, dog, cat, bunny should become bunny, cat, dog.
'''
elements.reverse()
print(elements)

''' 19. 
   Given a list, doorknobs, that holds strings, swap the elements at positions 1 and 3, if possible.
'''

doorknobs[1], doorknobs[3] = doorknobs[3], doorknobs[1]

''' 20. 
   In a list of ints called numbers, find the largest number in the list and place it at the end of the list.
'''

maxnum=numbers[0]
position = 0
for i in range(len(numbers)):
   if numbers[i]>maxnum:
      maxnum = numbers[i]
      position = i
numbers.append(numbers.pop(position))

''' 21. 
   In a 2D list with dimensions w by h, filled with random numbers from from 1 to 100, replace every odd number with either 2 or 22; 2 if the number was a single digit number, 22 if the number was a 2-digit number. 
'''

import random
var = [[random.randrange(1,101) for x in range(w)] for y in range(h)]

for y in range(h):
   for x in range(w):
      if var[y][x]%2!=0:
         if len(str(var[y][x]))==2:
            var[y][x]=22
         elif len(str(var[y][x]))==1:
            var[y][x]=2

print(var)

''' 22. 
   In a 2D list with dimensions w by h, holding grayscale values for an image, adjust the colors so the image is inverted. All light portions should be dark, all dark portions should be light. A value of 200 should be 5, a value of 100 should be 155, etc. Remember, there are 256 levels for color, including 0.
'''

for y in range(h):
   for x in range(w):
      image[y][x] = 255-image[y][x]

''' 23.
   In a list, shifters, holding ints, shift all elements forward 1 position. For example, position 2 should move to position 1, position 1 to position 0, and position 0 to the end of the list (etc.)
'''

shiftList.append(shiftList.pop(0))

''' 24. 
   Given an N-by-N grid of elevation values (in meters), a peak is a grid point for which all four neighboring cells are strictly lower. Write a code fragment that counts the number of peaks in a given N-by-N grid.
'''

def calcPeaks(grid):
   totalPeaks = 0
   for y in range(len(grid)):
      for x in range(len(grid[y])):
         walls = 0
         count = 0
         if x!=len(grid[y])-1:
            if grid[y][x]>grid[y][x+1]:
               count+=1
         else:
            walls+=1
         if x!=0:
            if grid[y][x]>grid[y][x-1]:
               count+=1
         else:
            walls+=1
         if y!=len(grid)-1:
            if grid[y][x]>grid[y+1][x]:
               count+=1
         else:
            walls+=1
         if y!=0:
            if grid[y][x]>grid[y-1][x]:
               count+=1
         else:
            walls+=1
         if walls+count==4:
            totalPeaks+=1
   return totalPeaks

print(str(calcPeaks(elevations))+" peaks in the grid")

''' 25. 
   90% of incoming college students rate themselves as above average. Write some code that, given a list of student rankings (stored in integer list rankings), prints the fraction of values that are strictly above the average value.
'''

rankingTotal = 0
for i in range(len(rankings)):
   rankingTotal+=rankings[i]
avgRank=rankingTotal/len(rankings)

numAbove = 0
for i in range(len(rankings)):
   if rankings[i]>avgRank:
      numAbove+=1

print(numAbove)

''' 26. 
   Given a 9-by-9 list of integers between 1 and 9, check if it is a valid solution to a Sudoku puzzle: each row, column, and block should contain the 9 integers exactly once.
'''
soduku=[[1,2,3,4,5,6,7,8,9],[2,3,4,5,6,7,8,9,1],[3,4,5,6,7,8,9,1,2],[4,5,6,7,8,9,1,2,3],[5,6,7,8,9,1,2,3,4],[6,7,8,9,1,2,3,4,5],[7,8,9,1,2,3,4,5,6],[8,9,1,2,3,4,5,6,7],[9,1,2,3,4,5,6,7,8]]

def sodukuCheck(soduku):
   validrows=0
   validcolumns = 0
   for y in range(len(soduku)):
      numbers = [i+1 for i in range(9)]
      valid=0
      for x in range(len(soduku[y])):
         if soduku[y][x] in numbers:
            numbers.remove(soduku[y][x])
            valid+=1
      if valid==9:
         validrows+=1
   for x in range(len(soduku[y])):
      numbers = [i+1 for i in range(9)]
      valid=0
      for y in range(len(soduku)):
         if soduku[y][x] in numbers:
            numbers.remove(soduku[y][x])
            valid+=1
      if valid==9:
         validcolumns +=1
   if validrows==9 and validcolumns==9:
      return True
   else:
      return False

if sodukuCheck(soduku):
   print("Soduku board is valid!")
else:
   print("Soduku is invalid.")

'''
   27. Create a list of 100 numbers between 1 and 10 (inclusive), create a new list whose first value is the number of 1s in the original list, whose 2nd value is the number of 2s in the original list, and so on. Average the number of occurences of each number in the list over 100 repetitions. Average the averages. Print the result to the screen.
'''

import random
avglist = [0 for t in range(100)]
occlist = []
for i in range(100):
   occ = [0 for i in range(10)]
   numbers = [random.randrange(1,11) for x in range(100)]
   for j in range(len(numbers)):
      occ[numbers[j]-1]+=1
   occlist.append(occ)
totalOccs = [0 for i in range(10)]
for j in range(10):
   for i in range(100):
      totalOccs[j]+=occlist[i][j]
print("total over 100 repetitions: " + str(totalOccs))
for j in range(10):
   totalOccs[j]=totalOccs[j]/100
print("average over 100 repititions: " + str(totalOccs))
totalAvg=0
for i in range(10):
   totalAvg+=totalOccs[i]
print("average occurances: " + str(totalAvg/10))

''' Sources
   http://users.csc.calpoly.edu/~jdalbey/103/Projects/ProgrammingPractice.html
   http://introcs.cs.princeton.edu/java/14array/
'''
