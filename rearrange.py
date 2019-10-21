import random


def rearrange(*words):
	word_list = [i for i in words]
	ans = ""
	c = 0
	while c != len(word_list):
		random_word = random.randint(0, len(word_list)-1)
		if word_list[random_word] not in ans:
			ans += " " + word_list[random_word]
			c += 1
	return print(ans)


rearrange("hey", "now", "brown", "cow")
