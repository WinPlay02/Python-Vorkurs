import requests
import csv

#Teil a)

def download_csv():
    with open("Tag3/covid19-data.csv", "w") as file:
        r = requests.get('https://stadtplan.bonn.de/csv?OD=4379')
        file.write(r.text)


#Teil b)

def tage_groesser(anzahl):
    with open('Tag3/covid19-data.csv', newline='') as csvdatei:
        csvinhalt = csv.DictReader(csvdatei, delimiter=';')
        
        for tag in csvinhalt:
            if tag["akut_erkrankt"] and int(tag["akut_erkrankt"]) > anzahl:
              print(tag['datum'])

#Teil c)

def sortiere_datum():
    with open('Tag3/covid19-data.csv', newline='') as csvdatei:
        csvinhalt = csv.DictReader(csvdatei, delimiter=';')
        csvinhalt = sorted(csvinhalt, key=lambda tag: tag["datum"])
        for tag in csvinhalt:
            print(tag)

#Teild d)

def höchster_zuwachs():
    with open('Tag3/covid19-data.csv', newline='') as csvdatei:
        csvinhalt = csv.DictReader(csvdatei, delimiter=';')
        csvinhalt = sorted(csvinhalt, key=lambda tag: tag["datum"])
        csvinhalt[0]["zuwachs"] = 0
        for i in range(1, len(csvinhalt)):
            heute_infektionen = int(csvinhalt[i]["positiv_getest"])
            gestern_infektionen = int(csvinhalt[i - 1]["positiv_getest"])
            zuwachs = heute_infektionen - gestern_infektionen
            csvinhalt[i]["zuwachs"] = zuwachs
        csvinhalt = sorted(csvinhalt, key=lambda tag: tag["zuwachs"], reverse=True)
        #for tag in csvinhalt:
        #    print(tag)
        print(csvinhalt[0]["datum"])


        