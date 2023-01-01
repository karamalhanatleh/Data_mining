# compute Euclidean distance
# point a
x1 = 2
y1 = 3
# point b
x2 = 5
y2 = 7
# distance b/w a and b
distance = ((x1 - x2)**2 + (y1 - y2)**2)**0.5
# display the result
print("Euclidean Distance between points (x1,y1) and (x1,y1) is", distance)

# As a function:
def get_distance(x1,y1,x2,y2):
    distance = ((x1 - x2)**2 + (y1 - y2)**2)**0.5
    return distance

print("Euclidean Distance using function", get_distance(2,3,5,7))

print("-------------------------")
# For loops with lists
xs = [8, 23, 45]
for x in xs:   # Python's for loops are a "for each" loop 
    print(x)
    
print("-------------------------")
print("enu")
for idx, x in enumerate(xs): # for iterating index
    print(idx, x)
    
print("-------------------------")   
index = 0            # Python's indexing starts at zero
for x in xs:   # Python's for loops are a "for each" loop 
    print(index, x)
    index += 1

print("-------------------------")     
# Passing a list to a function:
def my_function(list2):
  for x in list2:
    print(x)

my_function(xs)

    
    
