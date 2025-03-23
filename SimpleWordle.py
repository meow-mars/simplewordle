from termcolor import colored
from random import randint


def correct(letter):
    return colored(letter, 'white', 'on_green', attrs=['bold'])
def present(letter):
    return colored(letter, 'white', 'on_yellow', attrs=['bold'])
def absent(letter):
    return colored(letter, 'white', 'on_grey', attrs=['bold'])

#You can modify/add more words into the wordlist
word_list = ["hello","trees","trash","stump","spine","ocean","fishy","treck","plead"]

secret_list = []
guess = ""
randnum = randint(0,8)

secret = word_list[randnum]
for char in secret:
    secret_list.append(char)


while (guess!=secret):
    guess=""
    guess_list = []
    while len(guess)!=5:
        guess = input("Enter your guess: ")
    for char in guess:
        guess_list.append(char)

    for i in range (len(guess)):
        if (guess_list[i] in secret_list) and (guess_list[i] == secret_list[i]):
            print(correct(guess_list[i]),end="")
        elif (guess_list[i] in secret_list):
            print(present(guess_list[i]),end="")
        else:
            print(absent(guess_list[i]),end="")
    print()
print("Correct! Well done!")