from WordList import WordList
import os

def getPath():
    files = os.listdir("textfiles")

    print("Please choose one of the following files:\n")

    for file in files:
        print("- " + file[:-4])

    filename = input() + ".txt"

    if filename not in files:
        print("File doesn't exist.")
        return getPath()

    return "textfiles/" + filename


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