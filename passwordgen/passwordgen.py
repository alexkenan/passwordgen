#!/usr/bin/env python3.5
"""
Random password generator inspired by Gfycat
"""
#####################################
#    LAST UPDATED     15 APR 2020   #
#####################################
import secrets
import os
import sys
from appJar import gui


def load_adjectives() -> list:
    """
    Load list of all adjectives
    :return: List of adjectives
    """
    path = os.path.join(os.path.abspath(os.path.dirname(__file__)), 'adjectives.txt')
    with open(path) as files:
        list_adjectives = files.read().splitlines()

    return list_adjectives


def load_nouns() -> list:
    """
    Load list of all nouns
    :return:
    """
    path = os.path.join(os.path.abspath(os.path.dirname(__file__)), 'nouns.txt')
    with open(path) as files:
        list_nouns = files.read().splitlines()

    return list_nouns


def numbers(adjective1: str, noun1: str, adjective2: str, noun2: str, num: int) -> str:
    """
    Insert 1 number between each word (insert 3 numbers total)
    :param adjective1: First adjective
    :param noun1: First noun
    :param adjective2: Second adjective
    :param noun2: Second noun
    :param num: number of numbers in the password
    :return: String
    """
    list_nums = []
    for __ in range(num):
        list_nums.append(str(secrets.randbelow(10)))

    if len(list_nums) == 1:
        return ''.join((adjective1, noun1, list_nums[0], adjective2, noun2))
    elif len(list_nums) == 2:
        return ''.join((adjective1, noun1, list_nums[0], adjective2, noun2, list_nums[1]))
    else:
        return ''.join((adjective1, list_nums[0], noun1, list_nums[1], adjective2, list_nums[2], noun2))


def symbols(adjective1: str, noun1: str, adjective2: str, noun2: str, num: int) -> str:
    """
    Insert "num" punctuation symbols between each word
    :param adjective1: First adjective
    :param noun1: First noun
    :param adjective2: Second adjective
    :param noun2: Second noun
    :param num: number of symbols in the password (max 3)
    :return: String
    """
    list_nums = []
    syms = '!@#$%^&*,.;:'
    for __ in range(num):
        list_nums.append(secrets.choice(syms))

    if len(list_nums) == 1:
        return ''.join((adjective1, noun1, list_nums[0], adjective2, noun2))
    elif len(list_nums) == 2:
        return ''.join((adjective1, list_nums[0], noun1, adjective2, list_nums[1], noun2))
    else:
        return ''.join((adjective1, list_nums[0], noun1, list_nums[1], adjective2, list_nums[2], noun2))


def do_everything(adjective1: str, noun1: str, adjective2: str, noun2: str, num_num: int, num_sym: int) -> str:
    """
    Insert "num" punctuation symbols between each word
    :param adjective1: First adjective
    :param noun1: First noun
    :param adjective2: Second adjective
    :param noun2: Second noun
    :param num_num: number of numbers in the password (max 3)
    :param num_sym: number of symbols in the password (max 3)
    :return: String
    """
    list_nums = []
    list_syms = []
    syms = '!@#$%^&*,.;:'
    for __ in range(num_sym):
        list_syms.append(secrets.choice(syms))
    for __ in range(num_num):
        list_nums.append(str(secrets.randbelow(10)))

    if len(list_nums) == 1 and len(list_syms) == 1:
        return ''.join((adjective1, noun1, list_nums[0], list_syms[0], adjective2, noun2))
    elif len(list_nums) == 2 and len(list_syms) == 1:
        return ''.join((adjective1, list_nums[0], noun1, list_syms[0], adjective2, list_nums[1], noun2))
    elif len(list_nums) == 2 and len(list_syms) == 2:
        return ''.join((adjective1, list_nums[0], list_syms[0], noun1, adjective2, list_nums[1], list_syms[1], noun2))
    elif len(list_nums) == 1 and len(list_syms) == 2:
        return ''.join((adjective1, list_syms[0], noun1, list_nums[0], adjective2, list_syms[1], noun2))
    elif len(list_nums) == 3 and len(list_syms) == 1:
        return ''.join((adjective1, list_nums[0], noun1, list_nums[1], list_syms[0], adjective2, list_nums[2], noun2))
    elif len(list_nums) == 3 and len(list_syms) == 2:
        return ''.join((adjective1, list_nums[0], list_syms[0], noun1, list_nums[1], adjective2, list_nums[2],
                        list_syms[1], noun2))
    elif len(list_nums) == 2 and len(list_syms) == 3:
        return ''.join((adjective1, list_nums[0], list_syms[0], noun1,list_syms[1], adjective2,
                        list_nums[1], list_syms[2], noun2))
    elif len(list_nums) == 1 and len(list_syms) == 3:
        return ''.join((adjective1, list_syms[0], noun1, list_syms[1], list_nums[0], adjective2,
                        list_syms[2], noun2))
    elif len(list_nums) == 3 and len(list_syms) == 3:
        return ''.join((adjective1, list_nums[0], list_syms[0], noun1, list_nums[1], list_syms[1], adjective2,
                        list_nums[2], list_syms[2], noun2))
    else:
        return 'Error'


def random_uppercase(password: str) -> str:
    """
    Randomly capitalize some letters in the password
    :param password: Password returned by mainprogram
    :return: String of the password with stuff randomly capitalized
    """
    def randomupper(c):
        if secrets.randbelow(int(1E99)) > secrets.randbelow(int(1E99)):
            return c.upper()
        return c.lower()

    return ''.join(map(randomupper, password))


def runstuff():
    """
    Run the backend of the gui
    :return: None
    """
    number_nums = int(app.getRadioButton("numnum"))
    number_syms = int(app.getRadioButton("numsym"))
    word = mainprogram(number_nums, number_syms)
    if app.getCheckBox("Random capitalization?"):
        word = random_uppercase(word)
    app.clearTextArea("swe")
    app.setTextAreaState('swe', "normal")
    app.setTextArea('swe', 'Password to copy:\n\n{}'.format(word))
    app.setLabel('pass3', word)
    app.setLabelRelief('pass3', "sunken")


def mainprogram(num_nums: int=0, num_syms: int=0) -> str:
    """
    Join two adjectives and two nouns
    :param num_nums: Number of numbers
    :param num_syms: number of symbols
    :return: Randomly generated password phrase
    """
    adjectives = load_adjectives()
    nouns = load_nouns()
    adj1 = secrets.choice(adjectives)
    adj2 = secrets.choice(adjectives)
    noun1 = secrets.choice(nouns)
    noun2 = secrets.choice(nouns)

    if num_nums > 0:
        numbersgen = True
    else:
        numbersgen = False

    if num_syms > 0:
        symbolsgen = True
    else:
        symbolsgen = False

    if numbersgen and symbolsgen:
        return do_everything(adj1, noun1, adj2, noun2, num_nums, num_syms)
    elif numbersgen and not symbolsgen:
        return numbers(adj1, noun1, adj2, noun2, num_nums)
    elif not numbersgen and symbolsgen:
        return symbols(adj1, noun1, adj2, noun2, num_syms)
    else:
        return ' '.join((adj1, noun1, adj2, noun2))


#      GUI Stuff here
def press(btn: str) -> None:
    if btn == "Cancel":
        app.stop()
    else:
        runstuff()


if __name__ == '__main__':
    if len(sys.argv) == 3:
        try:
            one = int(sys.argv[1])
            two = int(sys.argv[2])
            print(mainprogram(one, two))
        except ValueError:
            print('Pass two integers as the arguments!')
    else:
        app = gui("Password Generator", "450x581")
        app.setFont(16)
        app.addLabel("title", "Random Password Generator", 0, 0, 3)  # Row 0,Column 0,Span 2
        app.addLabel("numbers", "Numbers:", 1, 0)              # Row 1,Column 0
        app.addRadioButton("numnum", '0', 1, 1)
        app.addRadioButton("numnum", '1', 2, 1)                             # Row 1,Column 1
        app.addRadioButton("numnum", '2', 3, 1)
        app.addRadioButton("numnum", '3', 4, 1)
        app.addLabel("symbs", "Symbols: ", 5, 0)
        app.addRadioButton("numsym", '0', 5, 1)
        app.addRadioButton("numsym", '1', 6, 1)                             # Row 1,Column 1
        app.addRadioButton("numsym", '2', 7, 1)
        app.addRadioButton("numsym", '3', 8, 1)
        app.addCheckBox("Random capitalization?", 9, 1)
        app.addButtons(["Submit", "Cancel"], press, 10, 0, 2)   # Row 3,Column 0,Span 2
        app.addLabel('pass3', '', 11, 1, 2)
        app.addTextArea('swe', 12, 0, 3)
        app.setTextAreaState('swe', 'disabled')

        app.go()
