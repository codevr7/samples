6#water content in your body
name = input("what is your name ? ")
weight = eval(input("what is your weight ? "))
person = input("are you a male or a  female ? ")
if person == 'male':
    low_content = weight * 50/100
    high_content = weight * 65/100
    print("for your weight your body water content should range from",low_content,"to",high_content)
    
elif person == 'female':
    lower_content = weight *45/100
    upper_content = weight * 60/100
    print("for your weight your body water content should range from ",lower_content,"to",upper_content)
        
else :
    print("wrong input")
