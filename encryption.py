message = input("what do you want to encrypt: ")#taking the input on what to encrypt
message = message.upper()#making the code easier by making all capital
for letter in message:#looping each letter
    if letter.isupper():#evaluating if message only consists of letters
        if ord(letter) < 78 :#evaluating if letter is lower than ord(78) which is N
            value = ord(letter)+(25-(ord(letter)-65)*2)#an equation for this encryption
            final = chr(value)#setting a variable for the final product by converting to a letter
            print(final)#returning the end product
        else:#if letter is more or equal to ord(78)
            value = ord(letter)-(25-(90-ord(letter))*2)#the equation for letters more than m
            final = chr(value)#converting to CHR value
            print(final)#returning final output
            
    else:#allowing only letters
        print("type in a message please")
