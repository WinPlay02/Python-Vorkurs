from typing import Generator, Tuple

def ngrams(count: int, text: str) -> Generator[Tuple[str, ...], None, None]:
	frags = text.replace(",", "").replace(".", "").replace("!", "").replace("\n", "").split(" ")
	for i in range(len(frags) - count + 1):
		elements = []
		for x in range(i, i + count):
			elements.append(frags[x])
		yield tuple(elements)
		
text = '...'   
for t in ngrams(2, text):
    print(t)