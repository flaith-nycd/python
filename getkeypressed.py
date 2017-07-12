#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# from msvcrt import getch
from getch_all_os import *


def _(value):
    print(value, end='', flush=True)


def get_keypressed():
    key = ord(getch())

    if key == 27:  # ESC
        return 'ESC', key
    elif key == 8:  # Backspace
        return 'BACK', key
    elif key == 9:  # Tab
        return 'TAB', key
    elif key == 10:  # Ctrl+Enter
        return 'CTRL_ENTER', key
    elif key == 13:  # Enter
        return 'ENTER', key
    elif key == 32:  # Space
        return 'SPACE', key
    elif key == 0:  # f keys
        key = ord(getch())
        return 'FUNCTION', 2000 + key
    elif key == 224:  # Special keys (arrows, f11 & f12 keys, ins, del, etc.)
        key = ord(getch())

        if key == 80:  # Down arrow
            return 'DOWN', key
        elif key == 72:  # Up arrow
            return 'UP', key
        elif key == 75:  # Up arrow
            return 'LEFT', key
        elif key == 77:  # Up arrow
            return 'RIGHT', key
        else:
            return 'SPECIAL', 1000 + key
    else:
        return 'CHAR', chr(key)


message = str()
# adding end='' and flush at true: no newline
# print("Enter a key ('Esc' to quit): ", end='', flush=True)
_("Enter a key ('Esc' to quit): ")
while True:
    type_of_key, key = get_keypressed()

    if type_of_key == "ENTER":
        # print('Enter')
        break
    elif type_of_key == "ESC":
        _('Esc')
        break
    elif type_of_key == "BACK":
        _('Backspace')
    elif type_of_key == "TAB":
        _('Tab')
    elif type_of_key == "CTRL_ENTER":
        _('Control+Enter')
    elif type_of_key == "UP":
        _('Up')
    elif type_of_key == "DOWN":
        _('Down')
    elif type_of_key == "LEFT":
        _('Left')
    elif type_of_key == "RIGHT":
        _('Right')
    elif type_of_key == "CHAR":
        # Print the char, adding end='' and flush at true,
        # no newline at each keypressed
        print(key.upper(), end='', flush=True)
        message += key.upper()
    else:
        print(type_of_key, ':', key)

print("\nMessage: |{}|".format(message))
