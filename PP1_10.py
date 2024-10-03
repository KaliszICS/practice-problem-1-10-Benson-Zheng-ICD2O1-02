import math

def q1(): 
  #Write Assignment code here

  user_input = input("Input a number: ")
  user_input = float(user_input)
  print (math.sqrt(user_input))


def q2(): 
  #Write Assignment code here
  user_input = input("Input a number: ")
  user_input = int(user_input)
  print (math.isqrt(user_input))


def q3(): 
  #Write Assignment code here
  user_input = input("Input a number: ")
  user_input = float(user_input)
  print (math.floor(user_input))


def q4(): 
  #Write Assignment code here
  user_input = input("Input a number: ")
  user_input = float(user_input)
  print (math.ceil(user_input))


def q5(): 
  #Write Assignment code here
  user_input = input("Input a number: ")
  user_input2 = input("Input another number: ")
  user_input = float(user_input)
  user_input2 = float(user_input2)
  product = (user_input*user_input2)/2
  print(math.trunc(product))




#Do not alter the following code
#Comment out the following code when running your tests

# q1()
# q2()
# q3()
# q4()
# q5()
