#find the first non -reapeated character
#problem: given a string , find the first non-reapeated character

input_str = "teeteracdacd"


for char in input_str:
  print(char)
  if  input_str.count(char) == 1:
      print("Char is: " ,char)
      #break 
# break main pura end ho jata hain


