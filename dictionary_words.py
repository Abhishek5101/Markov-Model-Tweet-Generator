import random


def get_random_words(n):
	random_words = []
	with open('/usr/share/dict/words') as word_file:
		data = word_file.readlines()
		for i in range(int(n)):
			random_words.append(random.choice(data))
	random_words = [word.rstrip() for word in random_words]
	sentence = ' '.join(random_words)
	return sentence


