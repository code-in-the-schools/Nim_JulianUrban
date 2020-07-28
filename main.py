def ninGame(x): 
  #while loop will loop until someone counts to 20
  count = 0
  while count <= 20:
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
   if x == 2: 
     n = int(input("Player 2: How many times would you like to count? "))
     #count once
     if n == 1:
       count += 1
       print("Current count: " + str(count))
       x = 1 #switch to other player's turn
     #count twice
     elif n == 2:
       count += 2
       print("Current count: " + str(count))
       x = 1 #switch to other player's turn
     else:
       print("Invalid input")
  if x == 1:
    print("Player 2 wins!")
  else:
    print("Player 2 wins!")


player = int(input("Which player should go first? "))
if player < 3 and player > 0: #if it is a number between 1 and 2
  ninGame(player)

