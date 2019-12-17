# Function returns sum of 2 numbers that are represented as a list
def add_num(n1, n2):
    result_1 = n1[2]+n2[2]
    if result_1 >= 10:
        n1[1] = n1[1]+1
        result_1 = (result_1)-10
    result_2 = n1[1]+n2[1]
    if result_2 >= 10:
        n1[0] = n1[0]+1
        result_2 = (result_2)-10
    result_3 = n1[0]+n2[0]
    if result_3 >= 10:
        result_3 = (result_3)-10
        final = [1,result_3,result_2,result_1]
    elif result_3 < 10:
        final = [result_3,result_2,result_1]
    return final
    
