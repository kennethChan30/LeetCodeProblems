def longestCommonPrefix(strs: list[str]) -> str:
#if it contains "", return ""
	if "" in strs:
		return ""
#if there is only one element, return the element
	if len(strs) == 1:
		return strs[0]
#check the first letter and so on of the first string to see if it match with other string
	n=1
	same = True
	prefix = ""
	while same:
		prefix_of_firststring = strs[0][0:n]
		for string in strs:
			if string[0:n] != prefix_of_firststring:
				return prefix
			if len(string) == n:
				same = False
		prefix = prefix_of_firststring
		n = n+1

	return prefix

		


print(longestCommonPrefix(["flower","flow","flight"]))
print(longestCommonPrefix(["dog","racecar","car"]))
