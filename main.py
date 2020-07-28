import random
def ninGame(x): 
  #while loop will loop until someone counts to 20
  count = 0
  while count < 20:
   #player 1
   if x == 1:
    n = int(input("Player 1: How many times would you like to count? "))
    #count once
    if n == 1:
      count += 1
      print("Current count: " + str(count))
      x = 2 #switch to other player's turn
    #count twice
    elif n == 2:
      count += 2
      print("Current count: " + str(count))
      x = 2 #switch to other player's turn
    else:
      print("Invalid input")
   #player 2
   elif x == 2: #You want them acting on diffrent intervuls 
     #the computer will win in one turn if it can, meaning if count is 18 or 19
     if count == 18:
       count += 2
       print("The computer counts twice.")
       print("Current count: " + str(count))
     elif count == 19:
       count += 1
       print("The computer counts once.")
       print("Current count: " + str(count))
     #regular turn
     else:
       n = random.choice([1, 2]) #randomly chooses to count one or two times
       if n == 1:
        count += 1
        print("The computer counted once.")
        print("Current count: " + str(count))
        x = 1 #switch to other player's turn
       #count twice
       elif n == 2:
        count += 2
        print("The computer counted twice.")
        print("Current count: " + str(count))
        x = 1 #switch to other player's turn
  if x == 1:
    print("Player 2 wins!")
  else:
    print("Player 2 wins!")


player = int(input("Which player should go first? "))
if player < 3 and player > 0: #if it is a number between 1 and 2
  ninGame(player)

