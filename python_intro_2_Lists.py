# Lists []
# List is the most basic Data Structure in python
l2 = [4,1,3,9,7] 
print(l2)
l3 = ['a','ab', 'abc','ab', 44] 
print(l3)
print("Length of list (l2)is:", len(l2))

#List Methods
l2.sort()       # Sort 
l2.append(12)   # Add an element at the end 
sum(l2)         # Sum all the elements 
max(l2)         # Find the maximum element 
min(l2)         # Find the minimum element        
l2.count('ab')  # Count occurrences of element 
l2.reverse()    # Reverse List 

print("------------------------------")
# Control Flow - if/else
count = 25 
if(count < 10): 
  print("Too Less") 
elif(count >= 10 and count < 30 ): 
  print("Just right") 
else: 
  print("Too much")

print("------------------------------")  
# For Loop
list1 = [1,2,3,4,5,6,7,8,9,10] 
print("list1 = ", list1) 
for list_item in list1: 
  print(list_item) 

# While Loop 
count = 0 
while count < 5: 
  print(count) 
  count += 1

# Break, Continue, Pass Statements
fruits = ["apple", "banana", "cherry", "dragonfruit", "mobile", "fig"] 
print("Available Fruits = ", fruits) 
for fruit in fruits: 
 if(fruit == "mobile"): 
   print("I cannot eat", fruit) 
   break 
 else: 
   print("I can eat", fruit)
   
