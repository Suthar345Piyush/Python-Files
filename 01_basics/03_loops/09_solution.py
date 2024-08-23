#list uniqueness checker
# problem : check if all elements in  a list are uniqe . if a duplicate is found exit the loop and point the duplication

items = ["apple" , "banana" , "orange" , "banana" , "mango"]

unique_item = set()

# for set we use .add() to add something to the place
# dor list we use .append() to add

for item in items:
  if item in unique_item:
    print("Duplicate: " , item)
    break 

  unique_item.append(item)
