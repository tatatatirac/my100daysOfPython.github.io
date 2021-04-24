import random
x = random.randint(1, 10)        # nasumicni broj od 1 do (u ovom primeru 10)
w = random.random()              # nasumicni broj od 0 do 1 16 decimala
q = round(w,2)                   # nasumicni broj od 0 do 1 zaokruzen na 2 decimale
q = "{:.2f}".format(q)           # formatiranje okrugle cifre na dve cifre primer: 3,30
y = random.random() * 10         # nasumicni broj od 0 do 10 ne ukljucujuci broj 10 svih 16 decimala
z = round(y,2)                   # nasumicni broj od 0 do 10 ne ukljucujuci broj 10 zaokruzen na 2 decimale
z = "{:.2f}".format(z)           # formatiranje okrugle cifre na dve cifre primer: 3,30


print(x)       
print(w)        
print(q)        
print(y)        
print(z)        
