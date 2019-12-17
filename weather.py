rainy = input("how is the weather outside ? (y/n)") .lower()
cold = input("is it cold outside ? (y/n) ").lower()
if(rainy == 'y' and cold == 'y'):
    print("you should wear a raincoat cause it is raining")
elif(rainy == 'y' and cold == 'n'):
    print("carry an umbrella since it is drizzling")
elif(rainy == 'n' and cold == 'y') :
    print("put on a jacket ,it is very cold")
else:
    print("wear anything ,it is quite beautiful outside")
