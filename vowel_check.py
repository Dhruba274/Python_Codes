
def check(string):
	vowels = "aeiou" 
	for char in vowels:
		if char not in string.lower():
			return False
	return True

string = "ajeiefou"

if(check(string))==True:
    print("Accepted")
else:
    print("Rejected")


