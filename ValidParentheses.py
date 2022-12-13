def isValid(s: str) -> bool:
	while "()" in s or "[]" in s or "{}" in s:
		s = s.replace("()","")
		s = s.replace("[]","")
		s = s.replace("{}","")
	if not s:
		return True
	else:
		return False

print(isValid("()"))
print(isValid("()[]{}"))
print(isValid("(]"))
