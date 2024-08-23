# coffee customization

# problem : customize a coffe order: "Small" , "Medium" , "Large" with an option for "Extra shot" of espresso:

order_size  = "Medium"
extra_shot  = True


if extra_shot:
  coffee = order_size + " coffee with an extra shot"

else:
  coffee = order_size + " coffee"
   

print("order: " , coffee)