while True:
  try:
    i2=int(input("Have you been having shortness of breath? Enter 1 if you have, and any other number if you haven't been experiencing it.\n "))
  except:
    print ("You have entered an invalid input. Try again with a proper answer. \n")
  else:
    break


 
while True:
  try:
    i4=int(input("Have you been feeling chills? Enter 1 if you have and enter any other number  if you aren't.\n"))
  except:
    print ("You have entered an invalid input. Try again with a proper answer. \n")
  else:
    break


  

    
    
while True:
  try:
    i7=int(input("Has your skin been turning blue or changing colors? This is a very serious symptom. If you have, then enter 1, if not, then enter any other number .\n"))
  except:
    print ("You have entered an invalid input. Try again with a proper answer. \n")
  else:
    break

while True:
  try:
    i8=int(input("Have you been feeling fluid in your lungs? This is also a very  serious symptom. If yes, then enter 1, if not, then enter any other number.\n"))
  except:
    print ("You have entered an invalid input. Try again with a proper answer. \n")
  else:
    break

if i1 == 1 and i2 == 1 and i4 == 1 and i7 == 1 and i8 == 1:
  print("You must seek medical help right away. You have all of the symptoms of the Spanish Flu or a different virus or flu.")

 


if i1 != 1 and i2 != 1 and i4 != 1 and i7 != 1 and i8 != 1: 
  print("You don't have the Spanish Flu")

if i1 == 1:
  if (i2 == 1 and i4 != 1 and i7 != 1 and i8 != 1) or (i2 != 1 and i4 == 1 and i7 != 1 and i8 != 1):
    print("You have a 20% chance of having the Spanish Flu. You should take some precautions but not too many.") 
  
  elif (i7 == 1 and i2 != 1 and i4 != 1 and i8 != 1) or (i8 != 1 and i4 == 1 and i7 != 1 and i2 != 1):
    print("You have a 30% chance of having the Spanish Flu. You should take some precautions but not too many.") 

   
  
  elif i7 == 1 and i2 == 1 and i4 != 1 and i8 != 1:
    print("You have a 50% percent chance of having the Spanish Flu. You should take medial amount of precautions. ")
  
  elif i7 == 1 and i4 == 1 and i2 != 1 and i8 != 1:
    print("You have a 50% percent chance of having the Spanish Flu. You should take medial amount of precautions. ")

  elif i7 == 1 and i8 == 1 and i2 != 1 and i4 != 1:
    print("You have a 60% percent chance of having the Spanish Flu. You should take medial amount of precautions. ")

  elif i8 == 1 and i2 == 1 and i7 != 1 and i4 != 1:
    print("You have a 50% percent chance of having the Spanish Flu. You should take a medial amount of precautions. ")

  elif i8 == 1 and i4 == 1 and i7 != 1 and i2 != 1:
    print("You have a 50% percent chance of having the Spanish Flu. You should take a medial amount of precautions. ")

  elif i2 == 1 and i4 == 1 and i7 != 1 and i8 != 1:
    print("You have a 40% percent chance of having the Spanish Flu. You should take a medial amount of precautions. ")

  elif i2 != 1 and i4 == 1 and i7 == 1 and i8 == 1:
    print("You have a 80% chance of having the Spanish Flu. You should take mass precautions. ")

  elif i4 != 1 and i2 == 1 and i7 == 1 and i8 == 1:
    print("You have a 80% chance of having the Spanish Flu. You should take mass precautions. ")
  
  elif i7 != 1 and i4 == 1 and i2 == 1 and i8 == 1:
    print("You have a 70% chance of having the Spanish Flu. You should take mass precautions. ")
    
  elif i8 != 1 and i4 == 1 and i7 == 1 and i2 == 1:
    print("You have a 70% chance of having the Spanish Flu. You should take mass precautions. ")
  
  elif i2 == 2 and i4 == 2 and i7 == 2 and i8 == 2:
    print("You do not have the Spanish Flu. You only have a high temperature. If you have any other symptoms, you might have the common cold or other infections.")

elif i1 != 1:
  print("You do not have Spanish Flu. If you have more than two of these symptoms then you should be cautious. If you have more than three of these symptoms then you should check with you doctor.  ")   





