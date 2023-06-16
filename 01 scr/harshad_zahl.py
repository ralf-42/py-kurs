# %%
"""
# Beispiel Harshad-Zahl
---

Eine Harshad-Zahl oder Niven-Zahl ist eine natürliche Zahl, die durch ihre Quersumme, das heißt die Summe ihrer Ziffern (im Dezimalsystem mit Basis 10), teilbar ist.
"""

# %%
# Start
n = int(input("Bitte die Zahl n eingeben: "))
zahl = 1
while zahl < n:
                
        
    for i in range(zahl,n):
        neu = str(i) #aus der zahl i wird ein String gebildet...
        liste = list(neu) #... der jetzt in seine Einzelteile zerlegt und diese in einer Liste gespeichert werden ...
        summe = 0   
        
        for item in liste:
            item = int(item) #... und nun wird jedes Einzelteil zu int konvertiert
            summe += item #... damit alle Ziffern zur Quersumme addiert werden könen
            
        if i % summe  == 0:
            print (f"{i:3d} ist eine Harshad-zahl, QuerSumme: {summe:3d}")
          
        zahl+=1
        i+=1
    
print("Fertig")