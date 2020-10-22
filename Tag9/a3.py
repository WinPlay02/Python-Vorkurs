import time

def anagram_gen(text):
	
	text = text.lower()
	words = []
	with open("Tag9/deutsch2.txt") as file: # gekürzte Liste -> 0.3 Sekunden
		words = file.readlines()
	# with open("Tag9/deutsch2.txt", "w") as file:
	#	file.writelines(words)
	start = time.time()
	anagrams = []
	for word in words:
		word = word.strip().lower()
		do_append = True
		if(len(word) != len(text)): # 0.4 Sekunden
			continue
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
	print(f"Completed in only {delta} s")