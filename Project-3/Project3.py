import nltk
nltk.download('words')
from nltk.corpus import words

print("Welcome to Wordle - CECS 174 edition!")
secret_word = input('Enter the secret 5-letter word: ')
count = len(secret_word)
is_word = False


while (count != 5) or (is_word == False):
  if secret_word in words.words():
    is_word = True
    
  else:
    is_word = False
  if (count != 5) or (is_word == False):
    print('Not a valid word, try again!')
    secret_word = input('Enter the secret 5-letter word: ')
    count = len(secret_word)
    
N = int(input("Input allowed number of attempts: "))
attempts = 1

while(attempts - 1 < N):
  
  print(f'Enter your attempt # {attempts}')
  player_word = input()
  count2 = len(player_word)
  is_word2 = False
  while (count2 != 5) or (is_word2 == False):
    if player_word in words.words():
      is_word2 = True
    
    else:
      is_word2 = False
    
    if (count2 != 5) or (is_word2 == False):
      if (is_word2 == False):
        print('Not a valid word try again!')
      elif (count2 != 5):
        print(f'You entered a {len(player_word)}-letter word, but a 5-letter word is needed. Try Again.')
      print(f'Enter your attempts # {attempts + 1}')
      player_word = input()
      count2 = len(player_word)
  print('You entered a 5-letter word')
  
  letter_in_the_right_spot = 0
  for i in range(0, len(player_word)):
    for j in range(0, len(secret_word)):
      if (player_word[i] == secret_word[j]):
        if (i == j):
          print(f'{player_word[i]} is in the secret_word and in the correct spot # {i + 1}')
          letter_in_the_right_spot += 1
          print(f'Correct letters in the correct spot: {letter_in_the_right_spot}')
        
        elif (i != j):
          print(f'{player_word[i]} is in the secret_word but not in the correct spot')
      
      else:
        continue
  
  if secret_word == player_word:
    print(f'Congrats you won using {attempts} attempt(s)')
    break
  attempts += 1
  tries = attempts

if (N == 0):
  player_word = 'No'
if secret_word != player_word:
  if (N == 0):
    pass
  elif (N <= attempts):
    print(f'You already used #{tries - 1} attempts. Better luck tomorrow!')