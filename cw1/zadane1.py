import json
import string

with open("teksty.json", "r") as file:
    dane = json.load(file)

tekst = ""
for i in range(0,len(dane["teksty"])):
    tekst += dane["teksty"][i][f'tekst{i+1}']
    tekst= tekst.lower()


#print(tekst)

wyrazy = tekst.translate(str.maketrans("", "", string.punctuation)).split()
wyrazy = [wyraz[:-1] + wyraz[-1].upper() for wyraz in wyrazy]
wyrazy = [wyraz for wyraz in wyrazy if 'a' in wyraz or 'A' in wyraz]
unikatowe_wyrazy = set(wyrazy)
print(unikatowe_wyrazy)
ilosc_wystapien = {wyraz: wyrazy.count(wyraz) for wyraz in unikatowe_wyrazy}
print(ilosc_wystapien)

with open("wyniki.json", "w") as file:
    json.dump({
        "tekst": tekst,
        "wyrazy": wyrazy,
        "unikatowe_wyrazy": list(unikatowe_wyrazy),
        "ilosc_wystapien": ilosc_wystapien
    }, file, indent=4)