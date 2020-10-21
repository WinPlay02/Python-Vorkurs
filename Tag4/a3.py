import requests 
import json

# LIaSudG3, pmZ2Q0gU, AeUNgdAb

def main():
    pastebin("LIaSudG3")
    pastebin("pmZ2Q0gU")
    pastebin("AeUNgdAb")

def pastebin(pastebin_id):
    #pastebin_id = 'LIaSudG3'
    pastebin = requests.get(f'https://pastebin.com/raw/{pastebin_id}')
    try:
        pastebin.raise_for_status()
    except requests.exceptions.HTTPError as error:
        print(f"{pastebin_id} HTTP Error {error}\n")
		
    try:
        dict = pastebin.json()
    except json.decoder.JSONDecodeError as error:
        print(f"{pastebin_id} JSON Error {error}\n")
    else:
        for i in range(0, 10):
            try:
                print(dict[str(i)],'\n')
            except KeyError as error: #geht jetzt wieder <3
                    print(f"{pastebin_id} Index Fehler {i}: {error}\n")
