#Oef 03 seconden naar d:u:m:s

aantalseconden = input("Geef het aantal seconden: ")
aantalseconden = float(aantalseconden)

dagen = (aantalseconden/60/60/24)
dagenklein = dagen - int (dagen)
uren = (dagenklein)*24
urenklein = uren - int(uren)
minuten = (urenklein)*60
minutenklein = minuten - int(minuten)
seconden = minutenklein*60

print("d:h:m:s -->" ,"{0: 0.0f} {1: 0.0f} {2: 0.0f} {3: 0.0f}".format(dagen,uren,minuten,seconden))