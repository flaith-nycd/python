#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import argparse
from math import pi

# Init the parser
parser = argparse.ArgumentParser(description="An argparse example")

# Add any arguments
parser.add_argument('-p', '--print', default='hello', help='print help')
parser.add_argument('-s', '--show-pi', default=pi, help='Show PI value')

# Handle the arguments' parser
# The object you get back from parse_args() is a 'Namespace' object:
# An object whose member variables are named after your command-line arguments.
# The Namespace object is how you access your arguments and the values associated with them:
args = parser.parse_args()
print(args.print)
print(args.show_pi)
