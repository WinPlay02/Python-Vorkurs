import time

def anagram_gen(text):
	
	text = text.lower()
	# words = []
	word_dict = {}
	rstart = time.time()
	with open("Tag9/deutsch2.txt") as file: # gekürzte Liste -> 0.3 Sekunden
		# words = file.readlines()
		for word in file.readlines():
			word = word.strip()
			wlen = len(word)
			if not wlen in word_dict:
				word_dict[wlen] = []
			word_dict[wlen].append(word.strip().lower())
	# print (word_dict)
	# with open("Tag9/deutsch2.txt", "w") as file:
	#	file.writelines(words)
	rend = time.time()
	rdelta = rend - rstart
	start = time.time()
	anagrams = []
	for word in word_dict[len(text)]:
		do_append = True
		for c in text:
			if text.count(c) != word.count(c):
				do_append = False
				break
		if not do_append:
			continue
		for c in word:
			if text.count(c) != word.count(c):
				do_append = False
				break
		if do_append:
			anagrams.append(word)
	end = time.time()
	delta = end - start
	print(set(anagrams))
	print(f"Reading completed in only {rdelta} s")
	print(f"Completed in only {delta} s")


anagram_gen(input("Text: "))