def read_file(file):
	with open(file) as book:
		data = book.readlines()
	
	words = [word.strip() for word in data]
	text_to_use = ' '.join(words)
	
	words_list = text_to_use.split(' ')
	return words_list


def calculate_histogram(source_text):
	words_list = read_file(source_text)
	
	text_dict = {}
	for word in words_list:
		text_dict[word] = 0
	for word in words_list:
		text_dict[word] += 1
	return text_dict


def unique_words(histogram):
	return len(histogram)


def frequency(word, histogram):
	if histogram[word]:
		return histogram[word]
	else:
		return f'No Such Word'


print(calculate_histogram('opticks.txt'))