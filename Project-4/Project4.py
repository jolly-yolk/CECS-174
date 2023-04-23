import string

WORD_LENGTH = 5

alphabet_string = string.ascii_lowercase
remaining_alphabet = list(alphabet_string)
in_secret_word_correct_spot = []
in_secret_word_somewhere = []
not_in_secret_word =[]

def read_dictionary (file_name): #opens word list
  file = open(file_name)
  new_dictionary_list = file.readlines()
  for i in range(len(new_dictionary_list)): #makes wordlist lowercase
    new_dictionary_list[i] = new_dictionary_list[i].replace('\n', '')
    new_dictionary_list[i] = new_dictionary_list[i].lower()
  file.close()
  return new_dictionary_list

def enter_a_word (word_type, num_letters): #enters player and secret word
    a_word = input(f'Enter the {num_letters}-letter {word_type} word: ')
    a_word = a_word.lower()
    return a_word

def is_it_a_word (input_word, dictionary_list): #checks if word is real
    if input_word not in dictionary_list:
        is_word = False
    else:
        is_word = True
    return is_word

def enter_and_check (word_type, dictionary_list): #checks if word is real/in list
    global WORD_LENGTH
    in_word = enter_a_word(word_type, WORD_LENGTH)
    is_real = is_it_a_word(in_word, word_list)
    length = len(in_word)
    while (length != WORD_LENGTH) or (is_real == False):
        is_real = is_it_a_word(in_word, word_list)
        length = len(in_word)
        if (length != WORD_LENGTH) and (is_real == False):
            print(f'You entered a {length}-letter word that is not in the dictionary. Please try again!')
            in_word = enter_a_word(word_type, WORD_LENGTH)
        elif (length != WORD_LENGTH) and (is_real == True):
            print(f'You entered a {length}-letter word that is in the dictionary. Please try again!')
            in_word = enter_a_word(word_type, WORD_LENGTH)
        elif (length == WORD_LENGTH) and (is_real == False):
            print(f'You entered a {length}-letter word that is not in the dictionary. Please try again!')
            in_word = enter_a_word(word_type, WORD_LENGTH)
    return in_word

def compare_words (player, secret): #compares player and secret word
  global remaining_alphabet
  global in_secret_word_correct_spot
  global in_secret_word_somewhere
  global not_in_secret_word

  letter_in_right_spot = 0
  lists = ['', '', '', '', '']
  player_list = list(player)

  for i in range(len(player)):
    for j in range(len(secret)):
      if (player[i] == secret[j]):
        if (i != j) and (player[i] not in in_secret_word_somewhere) and (player[i] not in in_secret_word_correct_spot): #Correct Letter and Wrong Spot
          lists[i] = f'({player[i]})'
          in_secret_word_somewhere.append(secret[i])
        elif (i == j) or (player[i] in in_secret_word_correct_spot): #Correct Letter and Correct Spot
          if i == 0:
            lists[0] = player[0]
            if player[i] not in in_secret_word_correct_spot:
              in_secret_word_correct_spot.append(player[i])
            letter_in_right_spot += 1
            break
          elif i == 1:
            lists[1] = player[1]
            if player[i] not in in_secret_word_correct_spot:
              in_secret_word_correct_spot.append(player[i])
            letter_in_right_spot += 1
            break
          elif i == 2:
            lists[2] = player[2]
            if player[i] not in in_secret_word_correct_spot:
              in_secret_word_correct_spot.append(player[i])
            letter_in_right_spot += 1
            break
          elif i == 3:
            lists[3] = player[3]
            if player[i] not in in_secret_word_correct_spot:
              in_secret_word_correct_spot.append(player[i])
            letter_in_right_spot += 1
            break
          elif i == 4:
            lists[4] = player[4]
            if player[i] not in in_secret_word_correct_spot:
              in_secret_word_correct_spot.append(player[i])
            letter_in_right_spot += 1
            break
      else: #Not in word
          continue

  for i in range(len(player)): #adds letters to not secret word list
    for j in range(len(secret)):
      if (player[i] not in secret) and (player[i] not in not_in_secret_word):
        not_in_secret_word.append(player[i])
        break

  for i in range(len(remaining_alphabet)): #removes already used letters
    for j in range(len(player_list)):
      if (player[j] in remaining_alphabet):
        remaining_alphabet.remove(player[j])
        break

  for i in range(len(in_secret_word_correct_spot)): #removes l in double l words
    for j in range(len(in_secret_word_somewhere)):
      if (in_secret_word_somewhere[j] == 'l'):
        if in_secret_word_somewhere[j] in in_secret_word_correct_spot:
          in_secret_word_somewhere.remove(in_secret_word_somewhere[j])
          break
      else:
        break
    
  dup = [x for i, x in enumerate(in_secret_word_correct_spot) if i != in_secret_word_correct_spot.index(x)]
  dup2 = [x for i, x in enumerate(in_secret_word_somewhere) if i != in_secret_word_somewhere.index(x)]
  dup3 = [x for i, x in enumerate(not_in_secret_word) if i != not_in_secret_word.index(x)]

  for i in range(len(in_secret_word_correct_spot)): #removes dups in correct spot
      if in_secret_word_correct_spot[i] in dup:
        in_secret_word_correct_spot.remove(in_secret_word_correct_spot[i])
        break
  for i in range(len(in_secret_word_somewhere)): #removes dups in somewhere
      if in_secret_word_somewhere[i] in dup2:
        in_secret_word_somewhere.remove(in_secret_word_somewhere[i])
        break
  for i in range(len(not_in_secret_word)): #removes dups in not_in
      if not_in_secret_word[i] in dup3:
        not_in_secret_word.remove(not_in_secret_word[i])
        break

  for i in range(len(lists)): #places underscores in final
    if lists[i] == '':
      lists[i] = '_'
  
      
  final  = ''.join(lists) #makes final a string
  return final, letter_in_right_spot
    

word_list = read_dictionary('project4_dictionary.txt')

print('Welcome to new and improved Wordle - CECS 174 edition!')
secret_word = enter_and_check('secret', word_list) #enters secret word

N = int(input("Input allowed number of attempts: ")) #enters number of attempts
attempts = 1

while (attempts <= N): #outputs everything above
  print(f'Enter your attempt #{attempts}')
  player_word = enter_and_check('player', word_list) #enter secret_word
  final_word, letter_in_the_right_spot = compare_words(player_word, secret_word)
  print(f'letter in the right spot: {letter_in_the_right_spot}')
  print(f'You guessed letters of the secret_word: {final_word}')
  print('Previously attempted letters that are in the correct spot of secret_word:')
  print(in_secret_word_correct_spot)
  print('Previously attempted letters that are in some spot of secret_word:')
  print(in_secret_word_somewhere)
  print('Previously attempted letters that are not in the secret_word:')
  print(not_in_secret_word)
  print('Remaining letters of the alphabet that have not been tried:')
  print(remaining_alphabet)
  if secret_word == player_word:
    print(f'Congrats you won using {attempts} attempt(s)')
    break
  attempts += 1

if (N <= 0): #used all attempts
  player_word = 'No'
if secret_word != player_word:
  if (N <= 0):
    pass
  elif (N <= attempts):
    print(f'You already used #{attempts - 1} attempts. Better luck tomorrow!')