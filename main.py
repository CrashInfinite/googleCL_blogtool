#!/usr/bin/env python

import os
import sys

os.system("clear")

os.system("echo -------------------------------------------")
os.system("echo - Welcome $USER, please choose an option? -")
os.system("echo -------------------------------------------")

os.system("echo 1 - Create a blog post ")
os.system("echo 2 - List calendar events ")
os.system("echo 3 - Exit ")

option = input()

if option == "1":
	title = input("Enter the Title: ")
	body = input("Body: ")

	os.system('google blogger post --title "' + title + '" "' + body + '"')

elif option == "2":
	os.system('google calendar list')
	res = input("Press enter to exit")
	os.system("clear")
	
elif option == "3":
	os.system("clear")
	sys.exit(0)

