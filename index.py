# Create an  empty  list called my list 
my_list = []

# Append the following elements into my_list:10,20,30,40
my_list.append (10)
my_list.append (20)
my_list.append (30)
my_list.append (40)

## Remove the last element from my_list
my_list.pop()

# Sort my_list in ascending order
my_list.sort()

# Find and print the index of the value 30 in my_list
index_of_30 = my_list.index(30)
print(f"The index of 30 in my_list is: {index_of_30}")

# You can also print the final list to see the result:
print(f"The final my_list is: {my_list}")