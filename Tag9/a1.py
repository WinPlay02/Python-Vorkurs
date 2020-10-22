#.- .-.. .-..  -.-- --- ..- .-.  -... .- ... .  .- .-. .  -... . .-.. --- -. --.  - ---  ..- ... https://pastebin.com/raw/EJyJpxPP

Morsecode = {
	'a': '.-',
	'b': '-...',
	'c': '-.-.',
	'd': '-..',
	'e': '.',
	'f': '..-.',
	'g': '--.',
	'h': '....',
	'i': '..',
	'j': '.---',
	'k': '-.-',
	'l': '.-..',
	'm': '--',
	'n': '-.',
	'o': '---',
	'p': '.--.',
	'q': '--.-',
	'r': '.-.',
	's': '...',
	't': '-',
	'u': '..-',
	'v': '...-',
	'w': '.--',
	'x': '-..-',
	'y': '-.--',
	'z': '--..',
}

#a)
def str_to_mc(text):
	code = list(text.lower())
	dt = list(Morsecode.items())
	mc = []
	for i in range(len(code)):
		for j in range(len(Morsecode)):
			if code[i] == dt[j][0]:
				mc.append(dt[j][1])
				break
			elif code[i] == ' ':
				mc[-1] = mc[-1] + " "
				break
			else:
				continue
	return " ".join(mc)

#b) + c)
def mc_to_str(mtext):
	code = mtext.split(" ")
	dt = list(Morsecode.items())
	text = []
	for i in range(len(code)):
		if len(code[i]) == 0:
			text[-1] = text[-1] + " "
			continue
		for j in range(len(Morsecode)):
			if code[i] == dt[j][1]:
				text.append(dt[j][0])
				break
			else:
				continue
	return "".join(text)
