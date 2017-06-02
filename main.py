from WordList import WordList
import os

supportedLanguages = ["japanese", "korean"]

def getPath():
	while True:
		print("Do you want to practice Japanese or Korean?")
		language = input()
		if language not in supportedLanguages:
			print("Language is not supported.")
		else:
			break

	filepath = "textfiles/" + language + "/"
	files = os.listdir(filepath)


	while True:
		print("Please choose one of the following files:\n")

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

	print("\nKonnichi wa! Hajimemashou!")
	print("\nType [e] for elimination run.")
	mode = input()

	if (mode == "e"):
		wordlist.elimination()

	if wordlist:
		wordlist.test()

	finish = input("\nWell done! Press enter to quit.")

run()