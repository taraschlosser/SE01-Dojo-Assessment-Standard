def mastermind():
  
  tries = 12
  code = "4431"

  while tries > 0:
    guess = input("Guess the code: ")
    tries = tries-1

    if guess == code: 
      print ("You won the game")
      break
    
    rightposition = 0
    
    for idx, number in enumerate(guess):
      if number == code[idx]:
        rightposition = rightposition +1
    print (str(rightposition) + " right position(s) in code")

  
mastermind()