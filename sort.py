# A function for sorting a list, depending on input
def sort(n,order):
   l = len(n)
   for i in range(0, l):
       for j in range(i+1, l):
           if order == 'asc':
               if n[i] > n[j]:
                   n[i], n[j] = n[j],n[i]
           else:
               if n[i] < n[j]:
                   n[i], n[j] = n[j],n[i]
                              
   return n            
               
          
    
             
    
    
