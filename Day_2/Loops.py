#-----------------------------------------------------------------------------------
## Conditional statements 
#--------------------------------------------------------------
## if statement = a block of code that will execute when it's condition is true

# age  = int(input("Enter yur age: "))


# if age == 100:
#     print("you are a century old!")
# elif age >= 18:
#     print("You are an adult")
# elif age <0:
#     print("You haven't born yet!!")
# else:
#     print("You are a child!")

#---------------------------------------------------------------------------
# Logical operators along with conditional statements - used to check if 2 or more conditional statements are true
# and , or , not - used all 3 in below examples

# temp = int(input("Enter temperature: "))

# if not (temp >= 0 and temp <= 30):
#    print("temprature is bad today, Stay Home!!")
# elif  not (temp < 0 or temp >30):
#     print("Temperature is good totday, Go Outside")

#-------------------------------------------------------------

# While Loop - a statement that will execute it's block of code , as long as it's conditions remains true

# while 1 == 1:
#     print("Help, I'm stuck in a loop!") 
#----------------------------------------------------------------
# name = ""

# while len(name) ==0:
#     name = input("Enter your name: ")
# print("Hello " +name)
#-----------------------------------------------------------
# name = ""

# while not name:
#     name = input("Enter your name: ")
# print("Hello " +name)
#--------------------------------------------------------------------

#For loop - a statement that will execute it's block of code for a limited period of time

##  While Loop  - Unlimited
## For Loop - Limited
# syntax - Start, stop, step

# for i in range(10):
#     print(i+1)

# for i in range (50, 100+1):
#     print(i )


# for i in range (50, 100+1, 2):
#     print(i)
#-----------------------------------------------
#Counter - counting for 10 seconds and then printing something
    
# import time
# for seconds in range(10,0,-1):
#     print(seconds)
#     time.sleep(1)
# print("Happy New Year")

#---------------------------------------------------------------------

# nested loops - the "inner loop" will finish all of its iterations before finishing one iteration of the "outer loop"

# rows   = int(input("How many rows? "))
# columns   =int(input("How many columns? "))
# symbol =input("Enter symbol to use: ")

# for i in range(rows):
#     for j in range(columns):
#         print(symbol, end="")
#     print()
#--------------------------------------------------------------------------------
#Loop control statements - Change a loops execution from its normal sequence

# break - used to terminate the loop entirely
#Continue - skips to the next iteration of the loop
#pass - just a placeholder

# while True:
#     name = input("Enter your name: ")
#     if name != "":
#         break
#-------------------------------------------------------------------------------------------------------

 # Initialize a variable to store the total steps
# total_steps = 0
    
#     # Iterate over each day of the week
# for day in range(1, 8):
#         # Ask the user to enter the number of steps for the current day
#     steps = int(input(f"Enter the number of steps walked on day {day}: "))
        
#         # Add the steps walked on the current day to the total steps
#     total_steps += steps
    
#     # Display the total number of steps walked in the week
# print(f"Total number of steps walked in the week: {total_steps}")

#--------------------------------------------------------------------------------------
# # Ask the user to input marks for three subjects
# marks_subject1 = int(input("Enter marks for subject 1 (out of 100): "))
# marks_subject2 = int(input("Enter marks for subject 2 (out of 100): "))
# marks_subject3 = int(input("Enter marks for subject 3 (out of 100): "))

# # Calculate the average mark
# average_mark = (marks_subject1 + marks_subject2 + marks_subject3) / 3

# # Determine the corresponding grade based on the average mark
# if average_mark >= 90:
#     grade = 'A'
# elif average_mark >= 80:
#     grade = 'B'
# elif average_mark >= 70:
#     grade = 'C'
# elif average_mark >= 60:
#     grade = 'D'
# else:
#     grade = 'F'

# # Print the average mark and corresponding grade
# print(f"Average mark: {average_mark}")
# print(f"Grade: {grade}")

#-----------------------------
# Prompt the user to enter a single integer
# number = int(input("Enter a single integer: "))

# # Check if the number is positive, negative, or zero and print the corresponding message
# if number > 0:
#     print("Positive")
# elif number < 0:
#     print("Negative")
# else:
#     print("Zero")

#-----------------------------------------

# color = input("please enter the color : 1)Red 2) Green 3)Yellow : ")
# if color  == "Red":
#     print("Stop")
# elif color  == "Green":
#     print("GO")
# elif color  == "Yellow":
#     print("Caution")
# else:
#     print("Please choose Red, Green or Yellow")



#-------------------------------------------------
# USD  = float(input("Enter the USD value: "))
# Euros = USD * 0.85
# print(str(Euros) + " Euros")
#----------------------------------------------------

total_Seconds  = int(input("Enter the value: "))

hours = total_Seconds//3600
minutes = (total_Seconds%3600)//60
seconds = total_Seconds%60

print(f"{total_Seconds} is equal to {hours} hour, {minutes} minute, and {seconds} seconds")


