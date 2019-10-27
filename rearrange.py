import random


def rearrange(*words):
	random_indexes_chosen = []
	word_list = [i for i in words]
	ans = ""
	c = 0
	while c != len(word_list):
		random_index = random.randint(0, len(word_list)-1)
		if word_list[random_index] not in ans:
			ans += " " + word_list[random_index]
			c += 1
	return print(ans)


sentence = "flying bats and scary cats"
words = sentence.split()

rearrange(*words)
