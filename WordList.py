from collections import UserDict
import random

class WordList(UserDict):
	def __init__(self, content):
		UserDict.__init__(self)
		self.loadContent(content)

	def loadContent(self, content):
		for line in content:
			words = line.split("|")
			jword = words[0]
			eword = words[1]

			# Initialize num of correct guesses required as 3
			self[eword] = [jword, 3]

	def askQuestion(self, eword):
		ans = input("\n" + eword + "\n")
		return ans

	def checkAnswer(self, ans, eword):
		jword = self[eword][0]

		if (ans.replace(" ", "") == jword.replace(" ", "")):
			print("Correct!")
			return True

		print("False! Correct answer is %s." % jword)
		return False

	def elimination(self):
		print("\nThis is the elimination run.")
		ewords = list(self.keys())
		random.shuffle(ewords)

		for eword in ewords:
			ans = self.askQuestion(eword)

			if self.checkAnswer(ans, eword):
				del self[eword]

		with open("textfiles/temp.txt", "w") as tempfile:
			for eword in list(self.keys()):
				tempfile.write("%s|%s\n" % (self[eword][0], eword))

		if self:
			print("\nYou need to learn the following words:")
			for eword in list(self.keys()):
				print("- %s" % self[eword][0])

		else:
			print("\nYou know all the words!")

	def interrogate(self, eword):
		print("Write it three times!")
		ctr = 3
		while ctr:
			ans = self.askQuestion(eword)

			if self.checkAnswer(ans, eword):
				ctr -= 1
			else:
				print("Start over!")
				ctr = 3
		print("Back to the test!")

	def test(self):
		print("\nThis is the test!")
		while self:
			eword = random.choice(list(self.keys()))
			ans = self.askQuestion(eword)

			if self.checkAnswer(ans, eword):
				self[eword][1] -= 1

				if self[eword][1] == 0:
					del self[eword]
					print("You have %i words left." % len(self))

			else:
				self.interrogate(eword)