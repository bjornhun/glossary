#!/usr/bin/env python
# -*- coding: utf-8 -*-

from WordList import WordList
import os
import random

supportedLanguages = os.listdir("textfiles")
supportedLanguages.remove("temp.txt")

def getPath():
	while True:
		print("Choose language: ")
		for supportedLanguage in supportedLanguages:
			print(supportedLanguage)

		chosenLanguage = input()
		if chosenLanguage.lower() not in [s.lower() for s in supportedLanguages]:
			print("Language is not supported.")
		else:
			break

	filepath = "textfiles/" + chosenLanguage + "/"
	files = os.listdir(filepath)


	while True:
		print("\nPlease choose one of the following files:\n")

		for file in files:
			print("- " + file[:-4])

		filename = input() + ".txt"

		if filename not in files:
			print("File doesn't exist.")
		else:
			break


	return filepath + filename


def readFile(path):
	with open(path) as f:
		content = f.read().splitlines()

	if path.endswith("50random.txt"):
		content = random.sample(content, 50)

	return content

def run():
	path = getPath()
	content = readFile(path)
	wordlist = WordList(content)

	print("\nWelcome! Let's begin!")

	wordlist.elimination()
	if wordlist:
		wordlist.test()

	while True:
		content = readFile("textfiles/temp.txt")
		wordlist = WordList(content)
		if wordlist:
			wordlist.elimination()
			if wordlist:
				wordlist.test()
		else:
			break


	more = input("\nWell done! Do you want to learn more words?")

	if (more.lower() == "y") or (more.lower() == "yes"): 
		run()

run()