# Trying to work out this function. No success yet, but trying to figure it out.

def disemvowel(word):
	vowels = "aeiouAEIOU"
	a_list = list(word)
	for letter in word:
		if letter in a_list:
			a_list.remove(letter)
	word = ''.join(a_list)
	print(word)