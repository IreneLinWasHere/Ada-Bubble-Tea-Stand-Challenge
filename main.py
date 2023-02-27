import math

tea_base_options = {"milk": 4.35, "oolong": 4.60, "rose": 5.85, "mango": 5.47}

add_ons_options = {"boba": 0.50, "lychee": 0.75, "jelly": 0.65, "taro": 1.00, "chia": 0.35}

def bubble_tea_calculator(tea_base, add_ons, loyalty_discount):
  #tea base subtotal
  tea_base_total = tea_base_options[tea_base]

  #add ons subtotal
  add_ons_total = 0
  for items in add_ons:
    add_ons_total += add_ons_options[items]

  total = tea_base_total + add_ons_total
  
  if loyalty_discount == True:
    total -=1

  print (f"The cost is ${total:.2f}")


# You may call bubble_tea_calculator with your own arguments here.
# For example, if the following line is uncommented, and the Run button
# is clicked, it will call bubble_tea_calculator with the listed
# parameters. The supplied example uses the same arguments as the
# test Challenge01.
    
# bubble_tea_calculator("milk", ["boba", "jelly", "taro"], False)

# The challenges are provided as a set of tests that can be run 
# from the Tests panel at the left (the icon looks like a check 
# mark). Clicking the Run tests button will run the Challenge 
# inputs against your code, displaying either a success message, 
# or a message about what was expected and what was observed.
