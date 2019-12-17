# A function for finding palindrome
def upside(word):
    rev = list(word)# Converting string input to a list 
    l = len(rev)# Input's length
    final = []# Empty list and also the output
    
    for i in range(1, l):# Setting a range for 1 to length of input
        final.insert(0, rev[0])# Adding 1st element of input list to output
        rev[0] = rev[i]# Setting 1st element as the range
    final.insert(0, rev[0])# Finally adding last item of input to output

    if final == rev:
        print("The word",word,"is a palindrome")
    else:
        print("The word",word,"is not a palindrome")
    
    return final # Returning output
                
word = input("Type in the word you want to turn upside down: ")# An input
upside(word)
   
