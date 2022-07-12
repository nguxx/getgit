# python3 code to  
# illustrate the  
# difference between 
# == and is operator 
# [] is an empty list 
list1 = [] 
list2 = [] 
list3=list1 

a = 1
b = 1
  
if (a == b): 
    print("True") 
else: 
    print("False") 
  
if (a is b): 
    print("True") 
else: 
    print("False") 
  
if (list1 is list3): 
    print("True") 
else:     
    print("False") 