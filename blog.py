#!/usr/bin/env python

import os
import sys

os.system("i3-msg floating enable")
os.system("clear")

os.system("echo -------------------------------------------")
os.system("echo - Welcome Shaun, please choose an option? -")
os.system("echo -------------------------------------------")

os.system("echo 1 - Create a post ")
os.system("echo 2 - Exit ")

option = raw_input()

if option == "1":
	title = raw_input("Enter the Title: ")
	body = raw_input("Body: ")

	os.system('google blogger post --title "' + title + '" "' + body + '"')

elif option == "2":
	os.system("clear")
	sys.exit(0)

