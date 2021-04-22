#1. Create a greeting for your program.

#2. Ask the user for the city that they grew up in.

#3. Ask the user for the name of a pet.

#4. Combine the name of their city and pet and show them their band name.

#5. Make sure the input cursor shows on a new line, see the example at:
#   https://band-name-generator-end.appbrewery.repl.run/

x = input("What is your NAME?  ")
print("Hello " + str.title(x))
y = input((x)+"..." +"What is the city that you grew up in? ")
print("OK you grew up in " + str.title(y))
z = input( str.title(x) + "...What is your pet? ")
print("OK your pet is " + (z))
print("OK"+ str.title(x) + "...Generated name for your band is: \t" + (z) + (y) ) 