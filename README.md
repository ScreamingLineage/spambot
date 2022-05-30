# spambot
A Python script which can spam the contents of a file or word(s) repeatedly to any chat.

## Contents
  1.  [Introduction](#introduction)
  2.  [Usage](#usage)
      - [Choosing an Input Option](#input-options)
      - [Adding Further Options](#other-options)
      - [Miscellaneous Options](#miscellaneous-options)

---

## Introduction

The bot goes through a file line by line and spams its contents wherever the text cursor is placed. A line break in the text file is considered to be "Enter" or the send message key.

For example if you want this to be spammed in some chat
```
message 1: just watched an insane video
message 1: you guys should see it
message 1: heres the link
message 1: https://www.youtube.com/watch?v=dBv9BMSPaA8
```
the text file (`spam_vid.txt` in this case) should be formatted like 
```
just watched an insane video
you guys should see it
heres the link
https://www.youtube.com/watch?v=dBv9BMSPaA8
```
and the command would be `spambot -f spam_vid.txt` 

## Usage
```usage: spambot [-h] (-f FILE | -s STRING | -m) [-i INTERVAL] [-w WAIT] [-c COUNT] [-d DIRECTORY]

Spam the contents of a text file in a chat

options:
  -h, --help            show this help message and exit
  -f FILE, --file FILE  spam contents of a file
  -s STRING, --string STRING
                        spam a string
  -m, --menu            show a menu to select file to spam (only displays text files)
  -i INTERVAL, --interval INTERVAL
                        interval between 2 messages (in seconds) (0 for minimum) [Default = 3]
  -w WAIT, --wait WAIT  time before spamming starts (in seconds) (0 to prevent waiting) [Default = 10]
  -c COUNT, --count COUNT
                        number of times repeat spamming (-1 to never stop) [Default = -1]
  -d DIRECTORY, --directory DIRECTORY
                        directory to search for text files to display menu (only takes an absolute path)
                        [Default - Current Directory]
```
### Input Options
#### `--file`, `--string` and `--menu`

Either of the above options can be used to give the bot some text to spam.
However only one of them can be used at at a time.

  - `-f`, `--file` - denote a file to be spammed (if the file contains spaces or some special characters then it is recommended to place it within quotes)
  - `-s`, `--string` - denote a word or a sentence (enclosed within quotes) 

Examples - 

`spambot -f spam.txt`

`spambot -s "This is a spam message"`

  - `-m`, `--menu` - displays a menu to choose a text file from the current directory

Example - `spambot -m` will display a menu similar to the one below
```
Detected Text Files in Directory:-

[1] Abuse.txt
[2] s1.txt
[3] s2.txt
[4] test.txt

Choose File to Spam:
```
### Other Options
#### `--interval`, `--wait` and `--count`

These options can be used to further fine tune the spambot

  - `-i`, `--interval` - set the time delay between 2 successive messages (in **seconds**) (**0** for the minimum possible interval) [Default: **3**]
  - `-w`, `--wait` - change the time the bot waits before spamming begins (in **seconds**) (**0** to skip waiting entirely) [Default: **10**]
  - `-c`, `--count` - set the total number of times the text or file contents are spammed (for a file, it will be spammed again from the beginning once it reaches the end) (**-1** to keep spamming infinitely) [Default: **-1**]

Example -

  - `spambot -f "test.txt" -c 2 -i 1 -w 3` - This will spam the contents of `test.txt`, **2** times with **1** second between each message. The bot also waits for **3** seconds after the command is executed before starting to spam

### Miscellaneous Options
#### `-d`, `--directory`

This is a sub-command for `--menu` and is useless without the latter. It can used to set the directory which the bot searches for text files to display in the menu. By default `--menu` searches the current directory where the terminal is open (**NOT** the directory where the `spambot` script is placed).
The `--directory` option also requires an absolute path and wont work with a relative one.

Example - `spambot -m -d "/path/to/text/files"` - will search for files to display in `/path/to/text/files`

