#   _____ _           _
#  /  ___| |         | |
#  \ `--.| |__   __ _| | _____  ___ _ __   ___  __ _ _ __ ___
#   `--. \ '_ \ / _` | |/ / _ \/ __| '_ \ / _ \/ _` | '__/ _ \
#  /\__/ / | | | (_| |   <  __/\__ \ |_) |  __/ (_| | | |  __/
#  \____/|_| |_|\__,_|_|\_\___||___/ .__/ \___|\__,_|_|  \___|
#   _____       __                 | |      __________
#  | ___ \     | |                 | |     ()_________)
#  | |_/ / ___ | |_                |_|      \ ~~~~~~~~ \
#  | ___ \/ _ \| __|                         \ ~~~~~~   \
#  | |_/ / (_) | |_                           \ ~~~      \
#  \____/ \___/ \__|                          ()__________)
# by Ryan

# import "regular expressions" to help split input
import re
# import os, sys, and sleep function from time to help with animations
import os, sys
from time import sleep

# import colorText function from termcolor to improve UX/UI
from termcolor import colored as colorText

# create a dictionary of key:value pairs assigned in 
# original:shakespearian format
shakespeare_words = {
     'you'      : 'thou',      'your'     : 'thine',      'do'       : 'dost',
     'have'     : 'hast',      'does'     : 'doth',       'are'      : 'art',
     'anything' : 'aught',     'no'       : 'nay',        'why'      : 'wherefore',
     'before'   : '\'ere',     'legs'     : 'forks',      'knees'    : 'hams',
     'perhaps'  : 'haply',     'hurry'    : 'hie',        'soon'     : 'lief',      
     'more'     : 'moe',       'hey'      : 'hark',       'my'       : 'mine own',
     'here'     : 'h\'re',      'good'     : 'valorous',  'You'      : 'Thou',
     'it\'s'    : '\'tis',     'even'     : 'yea',        'often'    : 'oft',
     'there'    : 'younder',   'therefore': 'argal',      'necessary': 'behoveful',
     'what\'s'  : 'what be',   'is'       : 'be',         'guys'     : 'gents',
     'how\'s'   : 'how be',    'boy'      : 'lad',        'yo'       : 'hark',
     'hello'    : 'hallo',     'boys'     : 'lads',       'guy'      : 'gent',
     'where'     : 'whence',   'no'       : 'nay',        'hate'     : 'loath'
}

# function with one paramater taking an array, and
# iterating through the array 
def translate(textArray):

     # get length of array of text
     terms = len(textArray)

     # create empty string to store new text
     translated_text = ""

     # iterate through the textArray values
     for i in range(terms):

          # selection - checking if the string is in the 
          # dictionary of shakespearian words, and if it is
          # then change the word to it's shakespearian value
          if textArray[i] in shakespeare_words:
               textArray[i] = shakespeare_words[textArray[i]]
               translated_text += colorText(textArray[i], 'green')

          # otherwise, concatenate (or add) the string on to
          # the translated text variable as is with no changes
          else:
               translated_text += textArray[i]
     
     # at the end of the function, return the full translated text back
     # to be displayed
     return translated_text



# helper function for text animations
def animateText(text, time):

     # another example of iteration
     for char in text:
          sys.stdout.write(char)
          sys.stdout.flush()
          sleep(time)

# store variable for ascii art display, as referencing one variable 
# multiple times is more efficient than making the logo line by line 
# every time
logo = """
     _____ _           _
    /  ___| |         | |
    \ `--.| |__   __ _| | _____  ___ _ __   ___  __ _ _ __ ___
     `--. \ '_ \ / _` | |/ / _ \/ __| '_ \ / _ \/ _` | '__/ _ \ 
    /\__/ / | | | (_| |   <  __/\__ \ |_) |  __/ (_| | | |  __/
    \____/|_| |_|\__,_|_|\_\___||___/ .__/ \___|\__,_|_|  \___|
     _____       __                 | |      __________
    | ___ \     | |                 | |     ()_________)
    | |_/ / ___ | |_                |_|      \ ~~~~~~~~ \ 
    | ___ \/ _ \| __|                         \ ~~~~~~   \ 
    | |_/ / (_) | |_                           \ ~~~      \ 
    \____/ \___/ \__|                          ()__________)
"""

# calling animate text function, and giving some more room underneath 
# to help add to UX/UI before getting input
animateText(logo, 0.0025)
for i in range(3):
     sleep(0.25)
     print("-")

# the program's main loop: will run until told to stop with a break statement
while True:

     # instructions for user
     animateText(colorText("Enter the text you want translated: ","green"), 0.01)
     # get user input for text to translate
     text = input("")

     # use a nested loop to only allow text that is at least one character in length
     while len(text) < 1:
          animateText(colorText("Please enter a piece of text to translate: ", "green"), 0.01)
          text = input("")
          
     # bring the input to all lower case
     text = text.lower()

     # split into a list of each word and punctuation mark
     # ex: "hi guys!" --> ["hi", " ", "guys" "!", ""]
     text_list = re.split("([^a-zA-Z0-9'])", text)

     # call the translate function and store it in a variable to display
     translated_text = translate(text_list)

     # use ascii art and text animations to display the results of calling
     # the translate function on the string that the user entered
     animateText(colorText("    |---------------------------------------------|","magenta"), 0.005)
     animateText("""

      __________________________________________
     ()_________________________________________)
      \ 
       \ """ + translated_text + """
        \ 
        ()_________________________________________)

     """, 0.005)
     animateText(colorText("  |------------------------------------------------|\n\n","magenta"), 0.005)
     
     # ask user if they want to continue running the program
     animateText("Would you like to translate another piece of text? \n\n", 0.005)
     answer = input("y/n: ")

     # check if the user entered the letter n for no, and if they did then break the loop
     if answer == "n":
          animateText("I bid thou a fair morrow.\n", 0.05)
          break

     # otherwise clear the screen to reduce clutter and run the loop again
     else:
          os.system("clear")
          print("\n\n")
          print(logo)

          for i in range(3):
               sleep(0.25)
               print("-")