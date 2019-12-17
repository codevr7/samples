from HCF import hcf
# Find smallest values of x and y such that ax – by = 0
# A function for finding smallest Quadratic for given input
def ax_by(a,b):
    return lcm(a,b)

def lcm(inp_1, inp_2):
    multiple = inp_1*inp_2/hcf(inp_1*inp_2)
    return multiple
            
    
