def romanToInt(s: str) -> int:
#Create dictionary
	roman_to_int = {'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000}
#Create list to save the implied value in order
	impliedvalue = []
	for i in s:
		impliedvalue.append(roman_to_int[i])
#Reverse the order of the list and do caculation from left to right
	impliedvalue.reverse()
	total = 0
	previous_value = 0
	for n in impliedvalue:
		if n >= previous_value:
			total = total + n
		else:
			total = total - n
		previous_value = n
	return total


print(romanToInt("III"))
print(romanToInt("LVIII"))
print(romanToInt("MCMXCIV"))