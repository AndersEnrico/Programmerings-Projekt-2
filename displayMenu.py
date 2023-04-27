import numpy as np
from inputNumber import inputNumber
from colorama import init as colorama_init
from colorama import Fore
from colorama import Style

colorama_init()

def displayMenu(options):
# DISPLAYMENU Displays a menu of options, ask the user to choose an item
# and returns the number of the menu item chosen.
#
# Usage: choice = displayMenu(options)
#
# Input options Menu options (array of strings)
# Output choice Chosen option (integer)
#
# Author: Mikkel N. Schmidt, mnsc@dtu.dk, 2015
# Display menu options
    for i in range(len(options)):
        print("{:d}. {:s}".format(i+1, options[i]))
# Get a valid menu choice
    choice = 0
    while not(np.any(choice == np.arange(len(options))+1)):
        choice = inputNumber('\x1b[;30;47m' + 'Vælg en af følgende muligheder fra menuen: ' + '\x1b[0m')
    return choice
