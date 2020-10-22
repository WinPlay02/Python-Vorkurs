texts = "SNXG VFG, QNFF NYYRF VZ HAVIREFHZ RAGJRQRE RVAR XNEGBSSRY VFG BQRE AVPUG"

#a) + b)
def caesar(text: str, key: int, decrypt: bool = False) -> str:
	text_lower = text.lower()
	encrypted_text = ""
	if decrypt:
		key = -key
	for c in text_lower:
		if c.isalpha():
			encrypted_text += chr(ord('a') + ((ord(c) - ord('a')) + key) % (ord('z') - ord('a') + 1))
		else:
			encrypted_text += c
	return encrypted_text

#c)
#key = 13
def brute_force():
	texts = "SNXG VFG, QNFF NYYRF VZ HAVIREFHZ RAGJRQRE RVAR XNEGBSSRY VFG BQRE AVPUG"
	for i in range(26):
		print(i)
		print(caesar(texts, i, decrypt=True))