import random
import os

# Board
board = ['''
>>>>>>>>>>Hangman<<<<<<<<<<

+---+
|   |
	|
	|
	|
	|
=========''', '''

+---+
|   |
O   |
	|
	|
	|
=========''', '''

+---+
|   |
O   |
|   |
	|
	|
=========''', '''

 +---+
 |   |
 O   |
/|   |
	 |
	 |
=========''', '''

 +---+
 |   |
 O   |
/|\  |
	 |
	 |
=========''', '''

 +---+
 |   |
 O   |
/|\  |
/    |
	 |
=========''', '''

 +---+
 |   |
 O   |
/|\  |
/ \  |
	 |
=========''']

class Hangman:

	def __init__(self, word):
		self.word = word
		self.hideword = ''
		self.hide_word()
		self.contadorBoard = 0
		self.acertadas = []
		self.erradas = []
		
	def guess(self, letter):
		acertoerro = False
		string = ''
		for indice in (range(len(self.word))):
			if self.hideword[indice] == '_':
				if self.word[indice] == letter:
					string += letter
					acertoerro = True
				else:
					string += '_'
			else:
				string += self.hideword[indice]
		if acertoerro:
			self.acertadas.append(letter)
		else:
			self.contadorBoard += 1
			self.erradas.append(letter)
		self.hideword = string
		
	def hangman_over(self):
		if len(self.erradas) >= 6:
			return True
		else:
			return False
		
	def hangman_won(self):
		if '_' in self.hideword:
			return False
		else:
			return True

	def hide_word(self):
		for caracter in self.word:
			self.hideword += "_"

	def print_game_board(self):
		os.system('cls')
		print(board[self.contadorBoard])
		print("\nWord: %s" % self.hideword)
		print("\nWrong Letters: ")
		for caracter in self.erradas:
			print("%s" % caracter)
		print("\n")
		print("\nCorrect Letters:")
		for caracter in self.acertadas:
			print("%s" % caracter)
		print("\n\n")

	def print_game_status(self):
		if self.hangman_over():
			print("Game over!")
			print('The Word Was: %s\n' % self.word)

		if self.hangman_won():
			self.print_game_board()
			print('You Won!\n')


def rand_word():
	with open("palavras.txt", "rt") as f:
		bank = f.readlines()
		print(bank, len(bank))
		saida = bank[random.randint(0, len(bank) - 1)].strip()
	return saida

def main():
	while True:
		game = Hangman(rand_word())

		while not game.hangman_won():
			game.print_game_board()

			if len(game.erradas) >= 6:
				break
			else:
				palpite = input('Type a letter: ')

			if game.hangman_over():
				break
			else:
				game.guess(palpite)

		game.print_game_status()

		if (input('Wanna Play again (y/n)? ') != 'y'):
			break

if __name__ == "__main__":
	main()
