def isPalindrome(x: int) -> bool:
	if x < 0:
		return False
	elif x == 0:
		return True
	else:
		count = True
		i = 1
		intToList = []
		while count:
		    intToList.append((x % 10**i)//10**(i-1))
		    x = x - x % 10**i
		    i = i + 1
		    if x == 0:
		        count = False
		if intToList == intToList[::-1]:
			return True
		else:
			return False

print(isPalindrome(121))
print(isPalindrome(10))
print(isPalindrome(-121))