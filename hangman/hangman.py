# Problem Set 2, hangman.py
# Name: 
# Collaborators:
# Time spent:

# Hangman Game
# -----------------------------------
# Helper code
# You don't need to understand this helper code,
# but you will have to know how to use the functions
# (so be sure to read the docstrings!)
import random
import string
import copy
WORDLIST_FILENAME = "words.txt"


def load_words():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print("Loading word list from file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = line.split()
    print("  ", len(wordlist), "words loaded.")
    return wordlist



def choose_word(wordlist):
    """
    wordlist (list): list of words (strings)
    
    Returns a word from wordlist at random
    """
    return random.choice(wordlist)

# end of helper code

# -----------------------------------

# Load the list of words into the variable wordlist
# so that it can be accessed from anywhere in the program
wordlist = load_words()


def is_word_guessed(secret_word, letters_guessed):
  secret_word=set(secret_word)
  letters_guessed=set(letters_guessed)
  count=0
  for el in letters_guessed:
    if el in secret_word:
      count+=1
  if count==len(secret_word):
    return True
  else:
    return False



def get_guessed_word(secret_word, letters_guessed):
  string=''

  secret_word=list(secret_word)

  for el in secret_word:
    string='_ '+string
  string=list(string)
    
  for i in range(len(letters_guessed)):
    for j in range(len(secret_word)):
      if letters_guessed[i]==secret_word[j]:
        string[2*j]=secret_word[j]
  string=''.join(string)
  return string



def get_available_letters(letters_guessed):
  all_available_letters=list(string.ascii_lowercase)
  available_letters=copy.deepcopy(all_available_letters)
  for i in range(len(letters_guessed)):
    for j in range(len(all_available_letters)):
      if letters_guessed[i]==all_available_letters[j]:
        available_letters.remove(letters_guessed[i])
  available_letters=''.join(available_letters)
  return available_letters


def fails_or_no(fails):
  if fails<=0:
    return 'no'
  else:
    return fails

def fail_string_apear(fails):
  if fails<=0:
    return ' so you lose one guess'
  else:
    return ''

def hangman(secret_word):
  vowels = ["a", "e", "i", "o", "u"]
  attempts = 6
  fails = 3
  fails_detect=False
  letters_guessed = list()
  secret_word_extra=list(secret_word)
  print("Welcome to the game Hangman!")
  print(f"I am thinking of a word that is {len(secret_word)} letters long.")
  print('You have 3 warnings left.')
  print("-" * 20)
  while attempts>0 and not is_word_guessed(secret_word,letters_guessed):
    if fails<=0 and fails_detect:
      attempts-=1
    fails_detect=False
    if attempts==0:
      break
    print(f"You have {attempts} guesses left.")
    string_guessed=get_guessed_word(secret_word, letters_guessed)
    print(f"Available letters: {get_available_letters(letters_guessed)}")
    letter=input("Please guess a letter: ")
    if letter.isalpha():
      if len(letter)==1:
        letter=letter.lower()
        if not (letter in letters_guessed):
          letters_guessed.append(letter)
          if (not (letter in secret_word_extra)) and not (letter in vowels):
            attempts-=1
            print(f'Oops! That letter is not in my word: {string_guessed}')
            print("-" * 20)
          elif (not (letter in secret_word_extra)) and (letter in vowels):
            attempts-=2
            print(f'Oops! That letter is not in my word: {string_guessed}')
            print("-" * 20)
          else:
            print(f'Good guess: {get_guessed_word(secret_word, letters_guessed)}')
            print("-" * 20)
        else:
          fails-=1
          fails_detect=True
          string3=(f"Oops! You have already guessed that letter. You now have {fails_or_no(fails)} warnings left{fail_string_apear(fails)}: {string_guessed}")
          print(string3)
          print("-" * 20)
      else:
        fails-=1
        fails_detect=True
        string2=(f'Oops! That is not a valid letter. You have {fails_or_no(fails)} warnings left{fail_string_apear(fails)}: {string_guessed}')
        print(string2)
        print("-" * 20)
    else:
      fails-=1
      fails_detect=True
      string1=(f'Oops! That is not a valid letter. You have {fails_or_no(fails)} warnings left{fail_string_apear(fails)}: {string_guessed}')
      print(string1)
      print("-" * 20)
  if is_word_guessed(secret_word,letters_guessed):
    total_score=attempts*len(set(secret_word))
    print("Congratulations, you won!")
    print(f"Your total score for this game is: {total_score}")
  else:
    print("Sorry, you ran out of guesses. ",end='')
    print(f"Secret word was {secret_word}")



# When you've completed your hangman function, scroll down to the bottom
# of the file and uncomment the first two lines to test
#(hint: you might want to pick your own
# secret_word while you're doing your own testing)


# -----------------------------------



def match_with_gaps(my_word: str, other_word: str) -> bool:
  my_word = my_word.replace(" ", "")
  if len(my_word) != len(other_word):
      return False
  for my_char, other_char in zip(my_word,other_word):
      if my_char != "_" and my_char != other_char:
          return False
  return True



def show_possible_matches(my_word):
  match = []
  for i in wordlist:
         if match_with_gaps(my_word, i):
               match.append(i)
  if len(match) == 0:
      print("No matches found")
  else:
      for i in match:
          print(i, end=" ")
  print("")




def hangman_with_hints(secret_word):
  vowels = ["a", "e", "i", "o", "u"]
  attempts = 6
  fails = 3
  fails_detect=False
  letters_guessed = list()
  secret_word_extra=list(secret_word)
  print("Welcome to the game Hangman!")
  print(f"I am thinking of a word that is {len(secret_word)} letters long.")
  print('You have 3 warnings left.')
  print("-" * 20)
  while attempts>0 and not is_word_guessed(secret_word,letters_guessed):
    if fails<=0 and fails_detect:
      attempts-=1
    fails_detect=False
    if attempts==0:
        break
    print(f"You have {attempts} guesses left.")
    string_guessed=get_guessed_word(secret_word, letters_guessed)
    print(f"Available letters: {get_available_letters(letters_guessed)}")
    letter=input("Please guess a letter: ")
    if letter=='*':
      print("-" * 20)
      print("Possible word matches are: ", end='')
      show_possible_matches(get_guessed_word(secret_word, letters_guessed))
      print("-" * 20)
    else:
      if letter.isalpha():
        if len(letter)==1:
          letter=letter.lower()
          if not (letter in letters_guessed):
            letters_guessed.append(letter)
            if (not (letter in secret_word_extra)) and not (letter in vowels):
              attempts-=1
              print(f'Oops! That letter is not in my word: {string_guessed}')
              print("-" * 20)
            elif (not (letter in secret_word_extra)) and (letter in vowels):
              attempts-=2
              print(f'Oops! That letter is not in my word: {string_guessed}')
              print("-" * 20)
            else:
              print(f'Good guess: {get_guessed_word(secret_word, letters_guessed)}')
              print("-" * 20)
          else:
            fails-=1
            fails_detect=True
            string3=(f"Oops! You have already guessed that letter. You now have {fails_or_no(fails)} warnings left{fail_string_apear(fails)}: {string_guessed}")
            print(string3)
            print("-" * 20)
        else:
          fails-=1
          fails_detect=True
          string2=(f'Oops! That is not a valid letter. You have {fails_or_no(fails)} warnings left{fail_string_apear(fails)}: {string_guessed}')
          print(string2)
          print("-" * 20)
      else:
        fails-=1
        fails_detect=True
        string1=(f'Oops! That is not a valid letter. You have {fails_or_no(fails)} warnings left{fail_string_apear(fails)}: {string_guessed}')
        print(string1)
        print("-" * 20)
  if is_word_guessed(secret_word,letters_guessed):
    total_score=attempts*len(set(secret_word))
    print("Congratulations, you won!")
    print(f"Your total score for this game is: {total_score}")
  else:
    print("Sorry, you ran out of guesses. ",end='')
    print(f"Secret word was {secret_word}")



# When you've completed your hangman_with_hint function, comment the two similar
# lines above that were used to run the hangman function, and then uncomment
# these two lines and run this file to test!
# Hint: You might want to pick your own secret_word while you're testing.


if __name__ == "__main__":
    # pass

    # To test part 2, comment out the pass line above and
    # uncomment the following two lines.
    
    #secret_word = choose_word(wordlist)
    #hangman(secret_word)

###############
    
    # To test part 3 re-comment out the above lines and 
    # uncomment the following two lines. 
    
    secret_word = choose_word(wordlist)
    hangman_with_hints(secret_word)
