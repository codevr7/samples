# my own translator
languages = ['french','german','japanese']
pick_lang = input("pick the language you want to transalate color to , between french ,spanish and japanese. ")
colors = ['red','blue','green','black','orange']
pick_col = input("pick the color you want to transalate between red, orange, blue, black and green . ")


if pick_lang == 'french' :
    if pick_col == 'red' :
        print("red in french is called as ROUGE with the R silent")
    elif pick_col == 'green':
        print("green in french is called as VERTE with the TE silent")
    elif pick_col == 'blue' :
        print("blue in french is called as BLEU")
    elif pick_col == 'black' :
        print("black in french is called as NOAH")
    elif pick_col == 'orange' :
        print("orange in french is called as OOHANJ")
    else :
        print("invalid input.type again")


elif pick_lang == 'spanish':
    if pick_col == 'red':
        print("red in spanish is called as ROHO")
    elif pick_col == 'green':
        print("green in spanish is called as BERDE")
    elif pick_col == 'blue':
        print("blue in spanish is called as AZUL")
    elif pick_col == 'black' :
        print("black in spanish is called as NEGRO")
    elif pick_col == 'orange':
        print("orange in spanish is called as NARANJA")
    else:
        print("invalid input,type again")

elif pick_lang == 'japanese' :
    if pick_col == 'red': 
         print("red in japanese is called as AKA")
    elif pick_col == 'green':
         print("green in japanese is called as MIDORI")
    elif pick_col == 'blue':
         print("blue in japanese is called as AO")
    elif pick_col == 'black':
         print("black in japanese is called as KURO")
    elif pick_col == 'orange':
         print("orange in japanese is called as ORENJI")
    else:
        print("invalid input,type again")
else :
    print("wrong language")
