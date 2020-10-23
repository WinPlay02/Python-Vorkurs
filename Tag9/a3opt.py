import time

def anagram_gen(text):
	
	text = text.lower()
	word_dict = {}
	rstart = time.time()
	with open("Tag9/deutsch2.txt") as file:
		for word in file.readlines():
			word = word.strip()
			wlen = len(word)
			if not wlen in word_dict:
				word_dict[wlen] = list()
			word_dict[wlen].append(word.strip().lower())
	rend = time.time()
	rdelta = rend - rstart
	start = time.time()
	anagrams = []
	text_set = set(text)
	text_counts = {c: text.count(c) for c in text_set}
	for word in word_dict[len(text)]:
		do_append = True
		for c in text_set:
			if text_counts[c] != word.count(c):
				do_append = False
				break
		if not do_append:
			continue
		if set(word) != text_set:
			continue
		anagrams.append(word)
	end = time.time()
	delta = end - start
	print(set(anagrams))
	print(f"Reading completed in only {rdelta} s")
	print(f"Completed in only {delta} s")

anagram_gen(input("Text: "))
