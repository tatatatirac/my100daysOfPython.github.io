welcome = "Welcome to the tip calculator!"          #pozdravna poruka
print(welcome)

bill = float(input("What is your tatal bill?  $"))                  #koliko je racun
people = int(input("Total people will split the bill?  "))              # koliko ljudi deli racun
percent = int(input("Total percentage tip you would like to give?\n10, 12 or 15?   "))      #procenat baksisa
split = bill / people                           # podeljen racun bez baksisa
eachPercent = split * (percent/100)             # izracunavanje baksisa po osobi
pay = split + eachPercent                       #koliko da plati svaka osoba
pay = round(pay,2)                              #zaokruzivanje na broj sa dve decimale
pay = "{:.2f}".format(pay)                      #formatiranje na broj sa dve decimale ako je druga decimala 0 (nula)
print(str(f"Each person shuld pay: {pay}"))     #printanje  sa f funkcijom koja prebacuje sa FLOAT / INTIGER na STRING
