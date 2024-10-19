# Hemit Patel
# 781159
# MR VEERA 
# ICS3U0-4
# student grade classification
# 18 oct 2024

num_subjects = int(input("Enter the amount of subjects:"))
grades = input("Enter the grades, sepearted by a space:")

# Split the grades into a list 
# split function turns the string into a list, seperating into items based on a character 
# in this case an empty space

grades_list = grades.split()

total = 0

# Double checking if the amount of grades listed is the same as the amount of subjects
if (num_subjects == len(grades_list)):
  
  for grade in grades_list:
    
    # The grades are strings so we must convert them to ints to be able to do math
    total += int(grade)

  average = total / num_subjects

  # using the ranges to find the grade
  if (average <= 90):
    print("Honours")

  elif (75 <= average < 90):
    print("Disinction")

  elif (50 <= average < 75):
    print("Pass")

  elif (average < 50):
    print("Fail")

else:
  print("You can only have the amount of grades specified in your amount of subjects")