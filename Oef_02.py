#Oef 02 Aantal seconden

dagen = input("Geef het aantal dagen op: ")
uren = input("Geef het aantal uren op: ")
minuten = input("Geef het aantal minuten op: ")
seconden = input("Geef het aantal seconden op: ")

dagen = int(dagen)
uren = int(uren)
minuten = int(minuten)
seconden = int(seconden)

Totaal = dagen*24*60*60 + uren*60*60 + minuten*60 + seconden
Totaal = str(Totaal)
print("Het totale aantal seconden bedraagt: " + Totaal)