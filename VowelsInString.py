'''vowel count in a string
what I think I know: letters to check for--> isolate letters-->
then count length and return the length
'''

get_vowels = list (input())
check_vowel = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
place_vowel = []

def get_vowel_count (get_vowels, check_vowel):
	for letter in get_vowels:
		for vowel in check_vowel:
			if letter == vowel:
				place_vowel.append(letter)
				make_join = ''.join(place_vowel)
				take_length = len(make_join)
	return take_length
	
print (get_vowel_count(get_vowels, check_vowel))	