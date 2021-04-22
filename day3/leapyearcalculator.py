year = int(input("What year you want to check?  "))

if year % 4 == 0:
    if year % 100 == 0:
        if year % 400 == 0:
            print("leap year")
        else:
            print("not leap")
    else:        
        print("It\'s leap year")
            
else:
    print("It is not leap year")