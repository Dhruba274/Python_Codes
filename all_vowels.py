
def check(string):
	vowels = "aeiou" 
	if all(vowel in string.lower() for vowel in vowels):
		return "Accepted"
	return "Not accepted"

string = "SEEquoiaL"

print(check(string))
