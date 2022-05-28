#!/usr/bin/env python

import pyautogui
import argparse
import time
import glob
import os


# Default values
INTERVAL_TIME = 3
WAIT_TIME = 10
CURRENT_DIRECTORY = os.getcwd()



# Countdown before spamming begins
def countdown(wait_time):
    for i in range(wait_time):
        print('Spam Bot Initializing in', wait_time - i, 'seconds')
        time.sleep(1)


# Main spammer
def spammer(word, interval):
    pyautogui.typewrite(word)
    pyautogui.press('enter')
    time.sleep(interval)


# Handles Spamming Files
def file_spammer(filename, interval, count):
    with open(filename, 'r') as file:
        # Loops 'count' times unless count is '-1'
        # If 'count' is '-1' then loops forever
        while count > 0 or count <= -1:
            for word in file:
                spammer(word, interval)
            file.seek(0,0)
            count -= 1


# Handles Spamming Strings
def string_spammer(word, interval, count):
    # Loops 'count' times unless count is '-1'
    # If 'count' is '-1' then loops forever
    while count > 0 or count <= -1:
        spammer(word, interval)
        count -= 1


# Clears screen
def clear():
    if os.name == 'posix':
        os.system('clear')
    elif os.name == 'nt':
        os.system('cls')


# Takes input only if it is valid 
# Otherwise repeats menu
def take_input(choices, text, input_prompt="Choose File to Spam: "):
    choice = ''
    while choice not in choices:
        clear()
        print("Detected Text Files in Directory:-\n")
        print(text)
        try:
            choice = int(input(input_prompt))
        except ValueError:
            continue
    return choice


# Shows a menu to choose text files
def get_file(directory):
    files = glob.glob("*.txt", root_dir=directory)
    if files == []:
        print(f"No text files found in {directory} or {directory} is not a directory\n" \
              + "Make sure that the path specified after '-d' or '--directory' is an absolute one")
        exit()
        
    menu = ""
    choices = []
    for index, file in enumerate(files):
        menu += f"[{index + 1}] {file}\n"
        choices.append(index+1)
    chosen = take_input(choices, menu)
    
    # Checking for trailing slashes in file path
    if directory[-1] in ("/", "\\"):
        file = f"{directory}{files[chosen - 1]}"
    else:
        file = f"{directory}/{files[chosen - 1]}"

    return file


# Argparse

# Checks if the count entered is below -1
def run_count(arg):
    try:
        count = int(arg)
    except ValueError:
        raise argparse.ArgumentTypeError(f"invalid count value: {arg}")
    if count < -1:
        raise argparse.ArgumentTypeError("count cannot be less than -1")
    return count


# Command line options
def parse_args():
    parser = argparse.ArgumentParser(
             description="Spam the contents of a text file in a chat")
    spam_input = parser.add_mutually_exclusive_group(required=True)

# Gets command line arguments
    spam_input.add_argument('-f', '--file', type=str, 
                            help='spam contents of a file')

    spam_input.add_argument('-s', '--string', type=str, 
                            help='spam a string')

    spam_input.add_argument('-m', '--menu', action='store_true',
                            help='show a menu to select file to spam (only displays text files)')

    parser.add_argument('-i', '--interval', type=float, default = INTERVAL_TIME,
                        help=f'interval between 2 messages (in seconds) (0 for minimum) [Default = {INTERVAL_TIME}]')

    parser.add_argument('-w', '--wait', type=int, default = WAIT_TIME,
                        help=f'time before spamming starts (in seconds) (0 to prevent waiting) [Default = {WAIT_TIME}]')

    parser.add_argument('-c', '--count', type=run_count, default = -1,
                        help='number of times repeat spamming (-1 to never stop) [Default = -1]')

    parser.add_argument('-d', '--directory', type=str, default = CURRENT_DIRECTORY,
                        help=f'directory to search for text files to display menu \
                        (only takes an absolute path) [Default - {CURRENT_DIRECTORY} (Current Directory)]')
    args = parser.parse_args()
    return args


def main(args):
    # Choose file from menu
    if args.menu:
        file = get_file(args.directory.strip())
        spammer_file = file
    else:
        spammer_file = args.file

    print('Put the text cursor at the desired message box')
    time.sleep(1)
    countdown(args.wait)

    # Spamming a string
    if args.string:
        string_spammer(args.string, args.interval, args.count)
    # Spamming contents of a file
    else:
        file_spammer(spammer_file, args.interval, args.count)

                
args = parse_args()
main(args)
