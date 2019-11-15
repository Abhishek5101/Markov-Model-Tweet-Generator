from dictogram import Dictogram
from random import choice

sample_text = " one fish two fish blue fish".split(' ')

markov = {}

for word in sample_text:
	markov[word] = Dictogram()

for index in range(len(sample_text) - 1):
	markov[sample_text[index]].add_count(sample_text[index + 1])

# print(markov['fish'].sample())
sentence = " "
word = choice(list(markov.keys()))
sentence += " " + word
for i in range(4):
	word = markov[word].sample()
	sentence += " " + word
print(sentence)