# THERE SHOULD BE ONE CONDITION FOR EACH OUTPUT
# IF THERE IS MORE THAN ONE CONDITION NEEDED USE BOOLEAN OPERATORS TO LINK THEM 

# for example if you are above jan 3 print wow

day = int(input())
month = int(input())

# here we have 2 conditions that would give us wow 
# if month is larger then 1 or if the day in the month is larger than 3

if (month > 1) or (month == 1 and day > 3):
  print("wow")
