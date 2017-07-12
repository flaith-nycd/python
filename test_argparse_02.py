#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import argparse
import sys

app_version = "0.01"

parser = argparse.ArgumentParser(usage="%(prog)s option filename", description="6502 Assembler/Disassembler/Simulator")
parser.add_argument("-a", "--assemble", action="store_true", dest="assemble", default=False,
                    help="assemble the code in FILE")
parser.add_argument("-d", "--disassemble", action="store_true", dest="disassemble", default=False,
                    help="disassemble the code in FILE")
parser.add_argument("-q", "--quiet", action="store_true", dest="quiet", default=False, help="quiet mode")
parser.add_argument("-t", "--trace", action="store_true", dest="trace", default=False, help="trace the code in FILE")
parser.add_argument("-x", "--execute", action="store_true", dest="execute", default=False,
                    help="execute the code in FILE")
parser.add_argument("-v", "--version", action="version", version="%(prog)s v" + app_version)
parser.add_argument("filename")
args = parser.parse_args()

infile = args.filename

if args.disassemble:
    if not args.quiet:
        print("Disassembling...")
    try:
        print('opening %s to disassemble' % infile)
        # f = open(infile, "r")
        # code = json.load(f)
        # f.close()
    except:
        print("Error: Could not decode input file: " + infile)
        sys.exit()
