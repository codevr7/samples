# A function for area of a triangle 
def area(x1,y1,x2,y2,x3,y3):
    p_x = [x1,x2,x3]# Adding the X coordinates in a list
    high_x = max(p_x)# Finding the highest among the X coordinates
    low_x = min(p_x)# Lowest of the X coordinates
    move_x = high_x - low_x# Finding the x movement and storing it in move_x

    p_y = [y1,y2,y3]# Doing the same with the Y coordinates 
    high_y = max(p_y)
    low_y = min(p_y)
    move_y = high_y - low_y    


    final = (move_x * move_y)/ 2# The equation for area of a triangle
    return final# Returning the output

