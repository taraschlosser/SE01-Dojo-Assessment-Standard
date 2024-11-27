## Completed Hint 1 and Hint 2 of Exercise 3
## Created gethints function to use within mastermind function

def gethints(guess, code):
  rightposition = 0
  rightnumber = 0
  
  for idx, number in enumerate(guess):
    if number == code[idx]:
      rightposition = rightposition +1
    if number in code:
      rightnumber = rightnumber +1
  rightnumber = rightnumber - rightposition
  return rightposition, rightnumber


def mastermind():

  allpossibleguesses = []
  for i in range (1111,6667):
    oneguess = str(i)
    if "7" not in oneguess and "8" not in oneguess and "9" not in oneguess and "0" not in oneguess:
      allpossibleguesses.append (oneguess)
  
  print(allpossibleguesses)
  
  tries = 12
  code = "4431"

  while tries > 0:
    guess = allpossibleguesses[0]
    print(guess)
    tries = tries-1

    if guess == code: 
      print ("You won the game")
      break
    
    allpossibleguesses.remove(guess)

    rightposition, rightnumber = gethints(guess, code)

    print (str(rightposition) + " right position(s) in code")
    print (str(rightnumber) + " right numbers in code")

    ## Idea/Approach for Hint 3 in Exercise 3: Loop through allpossibleguesses
    ## Use gethints function to compare originial guess with allpossibleguesses 
    ## Remove guesses out of allpossibleguesses that don't receive same hint as original guess
  
mastermind()