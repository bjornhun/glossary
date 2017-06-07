from WordList import WordList
import os

supportedLanguages = os.listdir("textfiles")

def getPath():
	while True:
		print("Choose language: ")
		for supportedLanguage in supportedLanguages:
			print(supportedLanguage)

		chosenLanguage = input()
		if chosenLanguage not in supportedLanguages:
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

	return content

def run():
	path = getPath()
	content = readFile(path)
	wordlist = WordList(content)

	print("\nWelcome! Let's begin!")
	print("\nType [e] for elimination run.")
	mode = input()

	if (mode == "e"):
		wordlist.elimination()

	if wordlist:
		wordlist.test()

	finish = input("\nWell done! Press enter to quit.")

run()