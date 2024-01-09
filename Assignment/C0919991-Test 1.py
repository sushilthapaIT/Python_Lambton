#CSD-1233-01
#Test 1
#Sushil Thapa
#October 19, 2023


#Provided Constants
MIN_GRADE = 0  #Constants for minimum grade
MAX_GRADE = 100 #Constants for maximum grade
DEAN_LIST_THRESHOLD = 90 #Constants for Dean's List threshold
PASS_LIST_THRESHOLD = 60 #Constants for Pass List threshold
 
#Initializing the variables
total_grades = 0 #Initialize the total grade
num_courses = 0 #Initialize the course count
 
 
#Asking the user for the number of courses to calculate the average
no_courses_to_average = int(input("Please enter the number of courses to average: "))
 
#Code for loop for the specified number of courses to calculate the average
for i in range(no_courses_to_average):
    while True:
            #Asking the User for grade obtained in each course in percentage
            grade = float(input("Please enter the grade (as a percentage): "))
        
            #Checking if the user have entered grade within correct range
            if (MIN_GRADE <= grade and grade <= MAX_GRADE):
                break
            else:
                print("Error! Grade must be between 0 and 100. Please Try Again.")
 
#Adding the grade to the total
total_grades += grade
num_courses += 1
 
# Calculating the average grade
average_grade = total_grades / num_courses
 
# Displaying the average grade
print(f"Average Grade: {average_grade:.2f}%")
 
# Displaying a message based on the average grade
if average_grade >= DEAN_LIST_THRESHOLD:
    print("Student has made the Dean's List")
elif average_grade >= PASS_LIST_THRESHOLD:
    print("Student has passed the program")
else:
    print("Student has not passed")


